from question_a import get_multiplication_table, display_multiplication_table

def main(): 
    keep_going = "y" #variable keep going will start a loop until user wants to quit
    while keep_going.lower() == "y": # while user wants to keep going
        table = get_multiplication_table(5, 10) # create a 5x10 multiplication table; 5 rows and 10 columns
        display_multiplication_table(table) # display the generated multiplication table
        keep_going = input("Do you want to run again? (y/n): ") #Does user want to run program again?
    print("Quitting Program, Goodbye!") 


if __name__ == "__main__":
    main()