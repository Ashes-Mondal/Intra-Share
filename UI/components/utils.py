ext_ico_path = {
    "TXT": "images/extensions/txt.png",
    "EXE": "images/extensions/exe.png",
    "MP4": "images/extensions/mp4.png",
    "MP3": "images/extensions/mp3.png",
    "ISO": "images/extensions/iso.png",
    "ZIP": "images/extensions/zip.png",
    "RAR": "images/extensions/zip.png",
    "CSV": "images/extensions/csv.png",
    "PPT": "images/extensions/ppt.png",
    "XLS": "images/extensions/xls.png",
    "DOC": "images/extensions/doc.png",
    "AVI": "images/extensions/avi.png",
    "PDF": "images/extensions/pdf.png",
    "JPEG": "images/extensions/image.png",
    "PNG": "images/extensions/image.png",
    "MKV": "images/extensions/mkv.png",
    "file": "images/extensions/file.png"
}

def getSizeStr(size_bytes: int):
    MB = int(size_bytes)//1048576
    if MB // 1000:
        GB = round(MB/1000, 1)
        return str(GB) + "GB"
    KB = int(size_bytes)//1024
    if KB // 1000:
        MB = round(KB/1000, 1)
        return str(MB) + "MB"
    if KB == 0:
        return str(size_bytes) + "B"
    else:
        return str(KB) + "KB"


def recvall(conn, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = bytearray()
    while len(data) < n:
        packet = conn.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data

##!DUMMY DATA
usrData = [
    {"name": "Ashes"},
    {"name": "Utkarsh"},
    {"name": "Mondal"},
    {"name": "Agni"},
    {"name": "Ashes1"},
    {"name": "Utkarsh1"},
    {"name": "Mondal1"},
    {"name": "Agni1"},
    {"name": "Ashes2"},
    {"name": "Utkarsh2"},
    {"name": "Mondal2"},
    {"name": "Agni2"},
]

userFilesData = [
    {"type": "ZIP", "fileName": "ISI Dark Secrets", "fileSize": "50GB"},
    {"type": "DOC", "fileName": "US-Army Plans", "fileSize": "50GB"},
    {"type": "ZIP", "fileName": "ISI Dark Secrets1", "fileSize": "50GB"},
    {"type": "DOC", "fileName": "US-Army Plans1", "fileSize": "50GB"},
    {"type": "ZIP", "fileName": "ISI Dark Secrets2", "fileSize": "50GB"},
    {"type": "DOC", "fileName": "US-Army Plans2", "fileSize": "50GB"},
    {"type": "ZIP", "fileName": "ISI Dark Secrets3", "fileSize": "50GB"},
    {"type": "DOC", "fileName": "US-Army Plans3", "fileSize": "50GB"},
    {"type": "ZIP", "fileName": "ISI Dark Secrets4", "fileSize": "50GB"},
    {"type": "DOC", "fileName": "US-Army Plans4", "fileSize": "50GB"},
]

fileSrchData = [
    {"type": "TXT", "fileName": "Study Material :)",
     "owner": "Ashes", "size": "50GB"},
    {"type": "EXE", "fileName": "Road-Rash",
             "owner": "Utkarsh", "size": "40MB"},
    {"type": "MP4", "fileName": "Hotel.Transylvania.4.Transformania.2022.1080p.WEBRip.x264-RARBG/Hotel.Transylvania.4.Transformania.2022.1080p.WEBRip.x264-RARBG.mp4",
             "owner": "Utkarsh", "size": "40MB"},
    {"type": "MP3", "fileName": "Road-Rash",
             "owner": "Utkarsh", "size": "40MB"},
    {"type": "AVI", "fileName": "Road-Rash",
             "owner": "Utkarsh", "size": "40MB"},
    {"type": "ISO", "fileName": "Road-Rash",
             "owner": "Utkarsh", "size": "40MB"},
    {"type": "ZIP", "fileName": "Road-Rash",
             "owner": "Utkarsh", "size": "40MB"},
    {"type": "RAR", "fileName": "Road-Rash",
             "owner": "Utkarsh", "size": "40MB"},
    {"type": "CSV", "fileName": "Road-Rash",
             "owner": "Utkarsh", "size": "40MB"},
    {"type": "PPT", "fileName": "Road-Rash",
             "owner": "Utkarsh", "size": "40MB"},
    {"type": "XLS", "fileName": "Road-Rash",
             "owner": "Utkarsh", "size": "40MB"},
    {"type": "DOC", "fileName": "Road-Rash",
             "owner": "Utkarsh", "size": "40MB"},
    {"type": "PDF", "fileName": "Road-Rash",
             "owner": "Utkarsh", "size": "40MB"},
    {"type": "JPEG", "fileName": "Road-Rash",
             "owner": "Utkarsh", "size": "40MB"},
    {"type": "BIN", "fileName": "Road-Rash",
             "owner": "Utkarsh", "size": "40MB"},
    {"type": "MKV", "fileName": "Eternals.2021.2160p.WEB-DL.x265.10bit.SDR.DDP5.1.Atmos-NOGRP.mkv",
             "owner": "Utkarsh", "size": "40MB"}
]

downloadsList = [
    {"fileName": "Study Material :)", "owner": "Ashes", "size": "50GB"},
    {"fileName": "ISI Secrets", "owner": "Utkarsh", "size": "1TB"},
    {"fileName": "Study Material :)", "owner": "Ashes", "size": "50GB"},
    {"fileName": "ISI Secrets", "owner": "Utkarsh", "size": "1TB"},
    {"fileName": "Study Material :)", "owner": "Ashes", "size": "50GB"},
    {"fileName": "ISI Secrets", "owner": "Utkarsh", "size": "1TB"},
    {"fileName": "Study Material :)", "owner": "Ashes", "size": "50GB"},
    {"fileName": "ISI Secrets", "owner": "Utkarsh", "size": "1TB"}
]
