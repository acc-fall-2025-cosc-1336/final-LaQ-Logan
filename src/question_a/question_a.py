#This program will create and display a multiplication table based on user-defined rows and columns

def get_multiplication_table(rows, cols): #will create the table rows and table columns  
    multiplication_table = [] # initialize an empty list to hold the multiplication table

    for r in range(0, rows):  # outer loop for rows
        row_list = [] # initialize an empty list for each row
        for c in range(0, cols):  # inner loop for columns
            row_list.append((r + 1) * (c + 1))  # multiply (row+1) * (col+1) and append to the row list, +1 to adjust for 0-indexing
        multiplication_table.append(row_list) # append the completed row to the multiplication table

    return multiplication_table 

def display_multiplication_table(table): # function to display the multiplication table (table is passed as an argument)
    for row in table: # iterate through each row in the table
        for value in row: # iterate through each value in the row
            print(value, end=" ")  # print values in same row with a space in between, end=" " keeps the cursor on the same line
        print()  # move to next line after each row

    
