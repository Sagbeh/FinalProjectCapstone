__author__='Sam'
# Imports sqlite3 library for database use
import sqlite3
# Defines the deleteRecord function
def deleteRecord():

    sqlite_file = 'NewDatabase.db'  # name of the sqlite database file
    # Attempt to delete a record as long as database and table exist
    while True:
        try:
            # User deletes record based on product's ID
            while True:
                try:
                    productID = int(input('\nEnter the ID of the product you want to delete: \n'))
                except ValueError:
                    print('\nProdcut ID must be an integer and cannot be blank.\n')
                else:
                    # Connecting to the database
                    conn = sqlite3.connect(sqlite_file)
                    c = conn.cursor()
                    # variables to hold the query and paremters that will be executed
                    sql = "DELETE FROM PRODUCTS WHERE ID = ?"
                    arg = (productID,)

                    c.execute(sql, arg)
                    break
        # If table doesn't exist, informs user to create the database first
        except sqlite3.OperationalError:
            print("\nPRODUCTS table does not exist\n")
            print("\nCreate the database first \n")
            break

        else:
            # # Committing changes and closing the connection to the database file
            conn.commit()
            conn.close()

            print('\nRecord deleted successfully\n')
            break
