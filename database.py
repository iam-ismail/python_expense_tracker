import mysql.connector

config = {
    "user" : "root",
    "password" : "toor",
    "host" : "localhost",
    "database" : "expenses"
}

# Since connects use keyword arguments and we use dictionary ** sign is used
db = mysql.connector.connect(**config)

# Pointer for executing queries 
cursor = db.cursor()
commit = db.commit



