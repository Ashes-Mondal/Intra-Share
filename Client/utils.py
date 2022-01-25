import json
import os
import pickle
import sys
import threading
import tkinter as tk
from queue import Queue
from tkinter import filedialog

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64


def encodeJSON(input: dict):
    return str(json.dumps(input)).encode()

def getFiles():
    root = tk.Tk()
    root.withdraw()

    filepaths = filedialog.askopenfilenames()
    files = []
    for filepath in filepaths:
        filename = filepath.split("/")[-1]
        filesize = os.path.getsize(filepath)
        files.append((filename,filesize,filepath))
    return files

def getFile():
    root = tk.Tk()
    root.withdraw()

    filepath = filedialog.askopenfilename()
    filename = filepath.split("/")[-1]
    filesize = os.path.getsize(filepath)
    return (filename,filesize,filepath)

def getDownloadDiectory():
    root = tk.Tk()
    root.withdraw()

    dirpath = filedialog.askdirectory()
    return dirpath

class pickling_struct:
    def __init__(self,client):
        self.clientID = client.clientID
        self.username = client.username
        self.messages = list(client.messages.queue)
        self.filesTaking = client.filesTaking
    
    def debug(self):
        print(f'clientID: {self.clientID}')
        print(f'username: {self.username}')
        print(f'messages: {self.messages}')
        print(f'filesTaking: {self.filesTaking}')

def saveAppLastState(username,server_addr,activeClients: dict):
    filename = os.path.join(f'bin/app_{username}.bin')
    if os.path.isdir('bin') == False:
        os.mkdir("bin")
    with open(filename,mode='wb') as f:
        pickle.dump(server_addr,f)
        for k,client in activeClients.items():
            if len(client.messages.queue) == 0 and len(client.filesTaking) == 0:
                continue
            obj = pickling_struct(client)
            # obj.debug()
            pickle.dump(obj,f)

def getAppLastState(username,server_addr):
    filename = os.path.join(f'bin/app_{username}.bin')
    if os.path.isdir('bin') == False:
        os.mkdir("bin")
        return {}
    if os.path.isfile(filename) == False:
        return {}
    with open(filename,mode='rb') as f:
        nList = []
        addr = pickle.load(f)
        if server_addr==addr:
            while True:
                try:
                    obj = pickle.load(f)
                    # obj.debug()
                    q = Queue()
                    for msg in obj.messages:
                        q.put(msg)
                    obj.messages = q
                    nList.append(obj)
                except Exception as e:
                    break
    return nList

#!<--------------- Hybrid encryption (RSA + AES) ------------->!#
def generate_AES_key(size = 16):
    return get_random_bytes(size)

def generate_RSA_keys(username: str,size = 1024):
    key = RSA.generate(size)
    pubkey = key.publickey().export_key()
    privkey = key.export_key("PEM")
    
    folder_path = os.path.join(f'keys/{username}')
    publickey_path = os.path.join(folder_path,"public.pem")
    privatekey_path = os.path.join(folder_path,"private.pem")
    
    if os.path.exists(folder_path) == False:
        os.makedirs(folder_path)

    
    ##writing keys into PEM files
    with open(publickey_path,mode='wb') as f:
        f.write(pubkey)
        
    with open(privatekey_path,mode='wb') as f:
        f.write(privkey)
    return pubkey,privkey

def get_keys(username:str):
    ##check if keys exists
    folder_path = os.path.join(f'keys/{username}')
    publickey_path = os.path.join(folder_path,"public.pem")
    privatekey_path = os.path.join(folder_path,"private.pem")
    
    if os.path.exists(folder_path) == False:
        return None,None
    
    ##reading keys from PEM files
    with open(publickey_path,mode='rb') as f:
        pubkey = f.read()
        
    with open(privatekey_path,mode='rb') as f:
        privkey = f.read()
    return pubkey,privkey

#*********** Encryption **************#
def encrypt_AES_key(pubkey: bytes,aeskey):
    rsakey = RSA.import_key(pubkey)
    rsacipher = PKCS1_OAEP.new(rsakey)
    encrypted_aeskey = rsacipher.encrypt(aeskey)
    return encrypted_aeskey

def encrypt_message(pubkey,message:str):
    #Todo:returns bundle (e_aeskey,e_msg,tag,nonce)
    ##Generate aeskey and encrypt using recipient's pubkey
    aeskey = generate_AES_key()
    e_aeskey = encrypt_AES_key(pubkey, aeskey)
    
    ##Encrypt the message with above aeskey
    message = message.encode('utf-8')
    aescipher = AES.new(aeskey, AES.MODE_EAX)
    e_msg,tag = aescipher.encrypt_and_digest(message)
    nonce = aescipher.nonce
    
    ##encoding to base64 and then decode
    e_aeskey = base64.b64encode(e_aeskey).decode()
    e_msg = base64.b64encode(e_msg).decode()
    tag = base64.b64encode(tag).decode()
    nonce = base64.b64encode(nonce).decode()
    
    return (e_aeskey ,e_msg, tag, nonce)

#*********** decryption **************#
def decrypt_AES_key(username: str,e_aeskey):
    publickey,privatekey = get_keys(username=username)
    privkey = RSA.import_key(privatekey)
    rsacipher = PKCS1_OAEP.new(privkey)
    aeskey = rsacipher.decrypt(e_aeskey)
    return aeskey

def decrypt_message(username: str,bundle: list):
    e_aeskey,e_msg,tag,nonce = bundle
    
    ##encode and then decode
    e_aeskey = base64.b64decode(e_aeskey.encode())
    e_msg = base64.b64decode(e_msg.encode())
    tag = base64.b64decode(tag.encode())
    nonce = base64.b64decode(nonce.encode())
    
    aeskey = decrypt_AES_key(username,e_aeskey)
    aescipher = AES.new(aeskey, AES.MODE_EAX,nonce)
    msg = aescipher.decrypt_and_verify(e_msg, tag)
    return msg.decode()
#!<--------------- ****************** ------------->!#

if __name__=='__main__':
    username = "Ashes"
    ##sender
    message = "Hello world"
    
    #*encrypting aeskey with receiver's pubkey
    pubkey,privkey = get_keys(username)
    if privkey == None:
        pubkey,privkey = generate_RSA_keys(username)
        
    #*encrypting message with aeskey
    e_aeskey,e_msg,tag,nonce = encrypt_message(pubkey, message)
    request = {
            "type": "send_message",
            "data": {
                "sender": 1,
                "receiver": 2,
                "bundle": [e_aeskey,e_msg,tag,nonce]
            }
        }
    res = encodeJSON(request)
    res = json.loads(res)
    ##receiver
    msg = decrypt_message(username,res["data"]["bundle"])
    print(msg)