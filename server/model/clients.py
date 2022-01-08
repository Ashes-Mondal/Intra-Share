model = (
"clients",
""" 
    clientID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    status BOOL NOT NULL DEFAULT FALSE,
    ip VARCHAR(255) NOT NULL,
    port1 INT NOT NULL,
    port2 INT NOT NULL
"""
)

