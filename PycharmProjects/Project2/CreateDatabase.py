__author__='Sam'
# Imports sqlite3 library for database use
import sqlite3

# Define createDB function
def createDB():
        # Connect to the database file
        conn = sqlite3.connect('NewDatabase.db')

        print("\nOpened database successfully\n")

        while True:
                try:
                        # Query to create the PRODUCTS table
                        conn.execute("CREATE TABLE PRODUCTS \
                                     (ID INTEGER PRIMARY KEY NOT NULL, \
                                     PRODUCTNAME TEXT NOT NULL, \
                                     QUANTITY INT NOT NULL, \
                                     PRICE REAL NOT NULL, \
                                     WEIGHT REAL NOT NULL, \
                                     CATEGORY CHAR(50), \
                                     SOLD INT);")
                # Catch sqlite error if query is executed and table already exists
                except sqlite3.OperationalError:
                        print("\nTable already exists\n")
                else:
                        print("Table created successfully\n")
                        # Closing the connection to the database file
                        conn.close()
                break


