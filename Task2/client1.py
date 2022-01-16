import socket
from threading import *
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT1 = 4456
PORT2 = 4467
PORT3 = 4468
ADDR = (IP, PORT1)
FORMAT = "utf-8"
SIZE = 1024
METADATA = ""
def __acceptConnectionsForData():
    client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[STARTING] client1 is starting")
    print(f"[LISTENING] client1 is listening on {IP}:{PORT3}.")
    client_server.bind((IP,PORT3))
    print(f"I am listening at PORT {PORT3}")
    client_server.listen()
    while True:
        conn, addr = client_server.accept()
        thread = threading.Thread(target=_give_Data, args=(conn, addr))
        thread.start()

def _give_Data(conn,addr):
    tempmessage="Hello You are now connected to client_server"
    conn.send(tempmessage.encode(FORMAT))
    while True:
        data = conn.recv(SIZE).decode(FORMAT)
        #here the client_client will send the filename@path which he wants 
        print(data)
        data = data.split("@")
        filename = data[0]
        path = data[1]

        f = open(path+filename,'rb')
        l = f.read(1024)
        while (l):
            conn.send(l)
            print('Sent ',repr(l))
            l = f.read(1024)
        f.close()

        # filepath = os.path.join(path, filename)
        #     with open(filepath, "w") as f:
        #         f.write(text)

def _requestForData():
    METADATA1 = METADATA.split("@")
    ADDR1=(METADATA1[1],int(METADATA1[5]))
    print(METADATA1[1])
    print(METADATA1[5])
    print("IN REQUESTFORDATA ")
    client_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("IN REQUESTFORDATA 1")
    client_client.connect(ADDR1)
    print("IN REQUESTFORDATA 2")
    askfile = METADATA1[3]+"@"+METADATA1[4]
    client_client.send(askfile.encode(FORMAT))
    with open('received_file\X.rar', 'wb') as f:
        while True:
            print('receiving data...')
            data = client_client.recv(1024)
            print('data=%s', (data))
            if not data:
                break
        # write data to a file
            f.write(data)
        f.close()

    

def main():
    global METADATA
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    t1 = Thread(target=__acceptConnectionsForData)
    t1.start();

    while True:
        data = "OK"
        x= client.recv(SIZE).decode(FORMAT)
        if(x):
            data=x
        cmd, msg = data.split("@")
        if cmd == "DISCONNECTED":
            print(f"[SERVER]: {msg}")
            break
        elif cmd == "OK":
            print(f"{msg}")

        data = input("> ")
        data = data.split("@")
        cmd = data[0]
        print(cmd)
        if cmd == "HELP":
            client.send(cmd.encode(FORMAT))
        elif cmd == "LOGOUT":
            client.send(cmd.encode(FORMAT))
            break
        elif cmd== "SENDMETADATA":
            print("pass 33")
            send_data=f"{cmd}@{data[1]}"
            print(send_data)
            client.send(send_data.encode(FORMAT))
            data1 = client.recv(SIZE).decode(FORMAT)
            print(data1)
            METADATA+=data1
            t2 = Thread(target=_requestForData)
            t2.start()

            
        elif cmd == "LIST":
            client.send(cmd.encode(FORMAT))
        elif cmd == "DELETE":
            client.send(f"{cmd}@{data[1]}".encode(FORMAT))
        elif cmd == "UPLOAD":
            ## UPLOAD@filename@text
            path = data[1]

            with open(f"{path}", "r") as f:
                text = f.read()

            filename = path.split("/")[-1]
            send_data = f"{cmd}@{filename}@{text}"
            client.send(send_data.encode(FORMAT))

    print("Disconnected from the server.")
    client.close()

if __name__ == "__main__":
    main()