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
        # Add the number to the list
        input_num.append(number)
    except ValueError:
        break

# attempt to convert the input to an integer
# if the input is not an integer, break out of the loop
