model = (
"clients",
""" 
    clientID INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    status BOOL DEFAULT TRUE,
    ip VARCHAR(255) ,
    port1 INT,
    port2 INT
"""
)

