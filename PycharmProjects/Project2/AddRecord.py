__author__='Sam'
# Imports sqlite3 library for database use
import sqlite3
# Define the addRecord function
def addRecord():

    sqlite_file = 'NewDatabase.db'  # name of the sqlite database file
    # Connecting to the database
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    # Try adding a record as long as database and table exist
    while True:
        try:
            # Validates that input for product name is not blank
            while True:
                productName = str(input('\nEnter the name of the product: \n'))
                if productName == '':
                    print('\nProduct name cannot be blank.\n')
                else:
                    break
            # Validates that quantity is an integer and not blank
            while True:
                try:
                    quantity = int(input('\nEnter the quantity of the product in stock: \n'))
                except ValueError:
                    print('\nQuantity must be an integer, and cannot be blank.\n')
                else:
                    break
            # Validates that price is a float and not blank.
            while True:
                try:
                    price = float((input('\nEnter the price of the product: \n')))
                except ValueError:
                    print('\nPrice must be a dollar value and cannot be blank.\n')
                else:
                    # Rounds price entered to two decimal places
                    price = (round(price, 2))
                    break
            # Validates that weight is a float and not blank
            while True:
                try:
                    weight = float(input('\nEnter the weight of the product: '))
                except ValueError:
                    print('\nWeight must be a number and cannot be blank.\n')
                else:
                    break
            # Category can be blank so anything entered is acceptable
            category = str(input('\nEnter the product category or leave it blank: \n'))
            # Validates that sold value is an integer and not blank
            while True:
                try:
                    sold = int(input('\nEnter the amount sold: \n'))
                except ValueError:
                    print('\nSold amount must be an integer, and cannot be blank.\n')
                else:
                    break
            # Variables that contain the sql query and the paremters that will be used
            sql = "INSERT INTO PRODUCTS (PRODUCTNAME, QUANTITY, PRICE, WEIGHT, CATEGORY, SOLD) \
                         VALUES (?, ?, ?, ?, ?, ?)"
            arg = (productName, quantity, price, weight, category, sold)
            # Executes the insert
            c.execute(sql, arg)

        # Catches sqlite error if insert is attempted and the database and table haven't been created yet
        except sqlite3.OperationalError:
            print("\nPRODUCTS table does not exist\n")
            print("\nCreate the database first \n")
            break
        else:
            # Committing changes and closing the connection to the database file
            conn.commit()
            conn.close()

            print("\nRecord Added successfully\n")
            break





