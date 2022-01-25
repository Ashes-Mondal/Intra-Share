model = (
"clients",
""" 
    clientID INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) BINARY NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    status BOOLEAN DEFAULT TRUE,
    ip VARCHAR(255) ,
    port1 INT,
    port2 INT,
    pubkey TEXT
"""
)

