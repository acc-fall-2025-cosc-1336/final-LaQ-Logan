def get_most_likely_ancestor_consensus(s, t): # gets positions of substring t in string s
    positions = [] #empty list to store positions
    len_of_sub = len(t) # length of substring t
    for i in range(len(s) - len_of_sub + 1): # iterate through s to find t 
        if s[i:i + len_of_sub] == t: # if substring in s matches t
            positions.append(i + 1)  #add position (1-based index) to list 
    return tuple(positions) # return positions as a tuple so it is immutable


def dna_consensus_finder(): # main function to find DNA consensus
    keep_going = 'y'
    while keep_going.lower() == 'y': # loop until user decides to stop
        
        while True:
            dna_string1 = input("Enter the first DNA string (9-16 characters): ").upper().strip() # Get first DNA string
            if 9 <= len(dna_string1) <= 16:
                break # valid length
            print("Invalid input. Try again with a length between 9 and 16.") # prompt for valid input

        
        while True:
            dna_string2 = input("Enter the second DNA string (exactly 4 characters): ").upper().strip() # Get second DNA string
            if len(dna_string2) == 4:
                break # valid length
            print("Invalid input. Try again with a length of exactly 4.") # prompt for valid input

        s = dna_string1 # assign first DNA string to s
        t = dna_string2 # assign second DNA string to t

        result = get_most_likely_ancestor_consensus(s, t) # get positions of t in s

        if result:
            print(f"The substring '{t}' is found at positions:", *result) # print positions if found as tuple unpacked
        else:
            print(f"The substring '{t}' is not found.") # print not found message

        while True:
            keep_going = input("Do you want to find another consensus? (y/n): ").lower()
            if keep_going == 'y':
                break  # repeat the loop
            elif keep_going == 'n':
                print("Goodbye!")  # exit program naturally
                return  # returning here ends the program if called from handle_choice
            else:
                print("Invalid input. Please enter 'y' or 'n'.") # prompt for valid input
    


def display_menu():
    print("\nDNA Consensus Finder Menu")
    print("1. Find Most Likely DNA Consensus")
    print("2. Exit")


def handle_choice(choice):
    if choice == '1':
        dna_consensus_finder()  # call main DNA consensus function
    elif choice == '2':
        print("Goodbye!")  # exits program
        return  # end program naturally
    else:
        print("Invalid choice. Please select 1 or 2.")  # prompt for valid input


def run_menu():
    display_menu() # display menu options
    choice = input("Please select an option (1 or 2): ").strip() # get user choice
    handle_choice(choice) # call handle_choice to process user input

