# display "unique" or "duplicate" for each input
# this program will display "unique" if the input is unique
# and "duplicate" if the input is duplicate

# Initialize an empty list to store user input numbers
input_num = []

# Loop indefinitely until the user enters something invalid 
while True:
    try:
        # Get the user input
        number = int(input("Enter a number: "))
        
        # Check if the number is in the list
        if number in input_num:
            print("Duplicate") # Display "Duplicate" if the input is duplicate
        else: 
            print("Unique")    # Display "Unique" if the input is unique

        # Add the number to the list
        input_num.append(number)
    except ValueError:
        break       # if the input is not an integer, break out of the loop
