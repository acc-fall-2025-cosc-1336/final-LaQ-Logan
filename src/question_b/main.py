from question_b import run_menu, get_stock_list

def main():
    stocks = get_stock_list()  # Get the list of Stock objects
    run_menu(stocks)  # Start the menu loop with the stock list

if __name__ == "__main__":
    main()