def display_menu(): #menu options user can select from
    print("Menu (Select an Option):")
    print("1. Display Stock Purchase History") 
    print("2. Exit")

def run_menu(stocks): #main menu loop
    menu_running = True
    while menu_running:
        display_menu()
        choice = input("Enter your choice from options (1-2): ")
        menu_running = handle_choice(choice, stocks)

def handle_choice(choice, stocks): #handle user menu choice
    if choice == '1':
        display_stock_list(stocks) #call function to display stock list
        print("")  # blank line for readability
        again = input("Do you want to return to the main menu? (y/n): ").lower() #ask user if they want to return to menu

        if again == 'y':
            return True  # keep menu loop running
        else:
            print("Exiting program. Goodbye!") #user quits program
            return False  # stop menu loop

    elif choice == '2':
        print("Exiting program. Goodbye!") #exit program
        return False

    else:
        print("Invalid choice. Please try again.")
        return True

def get_stock_list(): # Create list of Stock objects. stock is the class and symbol is an attribute, company name is another attribute
    return [
        Stock("AAPL", "Apple Inc"), #class( symbol, company_name)
        Stock("CAT", "Caterpillar"), #class( symbol, company_name)
        Stock("EK", "Eastman Kodak"), #class( symbol, company_name)
        Stock("GOOG", "Google"), #class( symbol, company_name)
        Stock("MSFT", "Microsoft") #class( symbol, company_name)
    ]

class Stock: # Stock class with symbol and company name attributes
    def __init__(self, symbol, company_name): #initialize symbol and company name as private attributes
        self.__symbol = symbol #private attribute 1
        self.__company_name = company_name #private attribute 2

    def get_symbol(self): #this will return the stock symbol
        return self.__symbol 

    def get_company_name(self): #this will return the company name
        return self.__company_name 

def display_stock_list(stocks): #print stock report header and stock list
    print("")  # blank line for readability
    print("Stock Report:")
    print("Company\t\tSymbol:")  # /t for tab space
    print("")  # blank line for readability

    for s in stocks: #loop through stocks list and print company name and symbol. for variable (s) in iteration of stocks list (stocks)
        print(f"{s.get_company_name():15} {s.get_symbol()}") # formatted print with 15 spaces for company name

