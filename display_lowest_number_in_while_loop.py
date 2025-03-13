# display lowest number in while loop
# this program will display the lowest number in a list of numbers

# Initialize an empty list to store user input numbers
input_num = [] 

# Loop indefinitely until the user enters something invalid
while True:
    try:
        # Get the user input
        number = int(input("Enter a number: "))  # attempt to convert the input to integer

        # Add the number to the list
        input_num.append(number)
    except ValueError:
        break       # if the input is not an integer, break out of the loop

# check if any numbers were entered
if number:
    print(min(input_num)) # if so, display the lowest number

