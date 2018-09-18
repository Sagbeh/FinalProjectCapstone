__author__='Sam'
# Imports sqlite3 library for database use
import sqlite3
# Define the displayAllRecords function
def displayAllRecords():

    while True:
        try:
            sqlite_file = 'NewDatabase.db'  # name of the sqlite database file
            # Connecting to the database file
            conn = sqlite3.connect(sqlite_file)
            c = conn.cursor()

            # sql query to display all records
            c.execute("SELECT * FROM PRODUCTS")
        # If database and table don't exist, user is informed and prompted to create the database first
        except sqlite3.OperationalError:
            print("\nPRODUCTS table does not exist\n")
            print("\nCreate the database first \n")
            break
        else:
            # Displays the records using a for loop for is column
            for row in c:
                print("\nID = ", row[0])
                print("PRODUCTNAME = ", row[1])
                print("QUANTITY = ", row[2])
                print("PRICE = ", row[3])
                print("WEIGHT = ", row[4])
                print("CATEGORY = ", row[5])
                print("SOLD = ", row[6], "\n")
            # Commit changes and close connection
            conn.commit()
            conn.close()

            break

