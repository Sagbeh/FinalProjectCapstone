__author__='Sam'
# Imports sqlite3 library for database use
import sqlite3
# Defines the updateRecord function
def updaterecord():

    sqlite_file = 'NewDatabase.db'  # name of the sqlite database file
    # Queries variable is a dictionary that contains the query that will be used depending on which column will be updated
    queries = {'name': "UPDATE PRODUCTS SET PRODUCTNAME = ? WHERE ID = ?",
               'quantity': "UPDATE PRODUCTS SET QUANTITY = ? WHERE ID = ?",
                'price': "UPDATE PRODUCTS SET PRICE = ? WHERE ID = ?",
                'weight': "UPDATE PRODUCTS SET WEIGHT = ? WHERE ID = ?",
                'catetory': "UPDATE PRODUCTS SET CATEGORY = ? WHERE ID = ?",
                'sold': "UPDATE PRODUCTS SET SOLD = ? WHERE ID = ?"}
    # Attempt record update as long as database and table exist
    while True:
        try:
            # Validate that productID is an integer and not blank
            while True:
                try:
                    productID = int(input('\nEnter the ID of the product you want to update: \n'))
                except ValueError:
                    print('\nProdcut ID must be an integer and cannot be blank.\n')
                else:
                    break
            # Depending on column name that is to be updated, different input required from user
            while True:

                try:
                    # User chooses which column to update
                    columnQuestion = int((input('\nEnter the number for the column that you want to update\n'
                                                '1. Name \n'
                                                '2. Quantity \n'
                                                '3. Price \n'
                                                '4. Weight \n'
                                                '5. Category \n'
                                                '6. Sold')))
                except ValueError:
                    print('\nMenu option must be an integer between 1 & 6\n')
                else:
                    if (columnQuestion < 1 or columnQuestion > 6):
                        print("\nMenu option must be between 1 & 7.\n")
                    else:
                        # columnquestion variable determines which query is used and user enters new value. sql variable will store the query
                        if columnQuestion == 1:
                            sql = queries['name']
                            while True:
                                newValue = str(input('\nEnter the new name: \n'))
                                if newValue == '':
                                    print('\nProduct name cannot be blank.\n')
                                else:
                                    break

                        elif columnQuestion == 2:
                            sql = queries['quantity']
                            while True:
                                try:
                                    newValue = int(input('\nEnter the new quantity: \n'))
                                except ValueError:
                                    print('\nQuantity must be an integer, and cannot be blank.\n')
                                else:
                                    break


                        elif columnQuestion == 3:
                            sql = queries['price']
                            while True:
                                try:
                                    newValue = float(input('\nEnter the new price: \n'))
                                except ValueError:
                                    print('\nPrice must be a dollar value and cannot be blank.\n')
                                else:
                                    newValue = (round(newValue, 2))
                                    break

                        elif columnQuestion == 4:
                            sql = queries['weight']
                            while True:
                                try:
                                    newValue = float(input('\nEnter the new weight: \n'))
                                except ValueError:
                                    print('\nWeight must be a number and cannot be blank.\n')
                                else:
                                    break

                        elif columnQuestion == 5:
                            sql = queries['catetory']
                            newValue = str(input('\nEnter the new category or leave it blank: \n'))
                            break

                        elif columnQuestion == 6:
                            sql = queries['sold']
                            while True:
                                try:
                                    newValue = int(input('\nEnter the new amount sold: \n'))
                                except ValueError:
                                    print('\nSold amount must be an integer, and cannot be blank.\n')
                                else:
                                    break
                        break

            # Connecting to the database
            conn = sqlite3.connect(sqlite_file)
            c = conn.cursor()
            # arg contains the parameters for the sql query
            arg = (newValue, productID)
            # executes the query
            c.execute(sql,arg)
        # If database/table doesn't exist, informs user that database must be created first
        except sqlite3.OperationalError:
            print('\nPRODUCTS table does not exist\n')
            print('\nCreate the database first \n')
            break

        else:
            # Committing changes and closing the connection to the database file
            conn.commit()
            conn.close()

            print('\nRecord updated successfully\n')
            break
