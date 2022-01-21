model = (
"files",
""" 
    fileID INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL UNIQUE,
    filesize VARCHAR(255) NOT NULL,
    path VARCHAR(255),
    clientID INT NOT NULL,
    FOREIGN key (clientID) REFERENCES clients(clientID)
"""
)