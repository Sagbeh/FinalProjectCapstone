__author__='Sam'
# Imports sqlite3 library for database use
import sqlite3
# Defines displaySingleRecord function
def displaySingleRecord():

    while True:
        try:
            sqlite_file = 'NewDatabase.db'  # name of the sqlite database file

            # User enters product ID of the records they want to view
            while True:
                try:
                    productID = int(input('\nEnter the ID of the product you want to view: \n'))
                except ValueError:
                    print('\nProdcut ID must be an integer and cannot be blank.\n')
                else:
                    break
            # Connecting to database file
            conn = sqlite3.connect(sqlite_file)
            c = conn.cursor()
            # variables that contain the query and parameters used for the sql query
            sql = "SELECT * FROM PRODUCTS WHERE ID = ?"
            arg = (productID,)
            # executes the sql query
            c.execute(sql,arg)
        # If database doesn't exist, informs user and prompts them to create the database first
        except sqlite3.OperationalError:
            print("\nPRODUCTS table does not exist\n")
            print("\nCreate the database first \n")
            break
        else:
            # for loop used to display the specified record
            for row in c:
                print("\nID = ", row[0])
                print("PRODUCTNAME = ", row[1])
                print("QUANTITY = ", row[2])
                print("PRICE = ", row[3])
                print("WEIGHT = ", row[4])
                print("CATEGORY = ", row[5])
                print("SOLD = ", row[6], "\n")
            # Commit changes and close database connection
            conn.commit()
            conn.close()

            break
