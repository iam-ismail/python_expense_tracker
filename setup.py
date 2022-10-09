import mysql.connector
from mysql.connector import errorcode

# Import  cursor
from database import cursor

# Globals 
DB_NAME = 'expenses'

# Tables Dictionary
TABLES = {}

# Transactions
TABLES['transactions'] = (
    "CREATE TABLE `transactions`("
    "`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,"
    "`amount` FLOAT(10) NOT NULL,"
    "`description` TEXT NOT NULL,"
    "`created_at` DATETIME  NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "`updated_at` DATETIME  NOT NULL DEFAULT CURRENT_TIMESTAMP"
    ")ENGINE=InnoDB"
)


# Database
def create_database():
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(DB_NAME))
        print("Database {} is created".format(DB_NAME))
    except mysql.connector.Error as err:
        if err.errno ==  errorcode.ER_DB_CREATE_EXISTS:
            print('Database {} exists!'.format(DB_NAME))
        else: 
            print('Error : {}'.format(err.errno))

# Tables
def create_tables():
    cursor.execute("USE {}".format(DB_NAME))
    for table in TABLES:
        table_query = TABLES[table]
        try:
            print('creating ==> {}'.format(table), end="\n")
            # print(table_query, end="")
            cursor.execute(table_query)
            print('Success', end="\n")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table {} already exists".format(table))
            else:
                print("Error {}".format(err.msg))
        


# create a database
create_database()
create_tables()



