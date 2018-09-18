# Import the functions from the menu option files in the project
from CreateDatabase import *
from AddRecord import  *
from UpdateRecord import *
from DeleteRecord import  *
from DisplayAllRecords import *
from DisplaySingleRecord import *
# Defines the main function
def main():
    # Variable to quit out of program
    qt = False

    # Programs runs until qt is true aka user quits
    while qt == False:
        # Displays menu options for user
        print("Database Manager \n"
              "^^^^^^^^^^^^^^^^ \n"
              "1. Create the Database \n"
              "2. Add a Record \n"
              "3. Update a record \n"
              "4. Delete a record \n"
              "5. Display all records \n"
              "6. Display a single record \n"
              "7. Quit \n")
        # Validation to ensure menu option is an integer between 1 & 7
        while True:
            try:
                option = int(input("Enter the menu option number: "))
            except ValueError:
                print('\nError! Value must be an integer between 1 & 7. Try again.\n')
            else:
                if (option < 1 or option > 7):
                    print("\nMenu option must be between 1 & 7.\n")
                else:
                    break
        # Depending on menu option selection, different menu function is called
        if option ==1:
          createDB()

        elif option ==2:
            addRecord()

        elif option ==3:
            updaterecord()

        elif option == 4:
            deleteRecord()

        elif option == 5:
            displayAllRecords()

        elif option == 6:
            displaySingleRecord()
        # Quits the program
        elif option ==7:
            qt = True
# Call main function
main()
