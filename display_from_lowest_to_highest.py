# display from lowest to highest    
# this program will display the numbers from lowest to highest
# using a while loop and sort function

# initialize an empty list to store the numbers
input_num = []

# loop indefinitely until user enters something invalid 
while True:
    try:
        # get the user input
        number = int(input("Enter a number: ")) # attempt to convert the input to integer

        # add the number to the list
        input_num.append(number)
    except ValueError:
        break   # if the input is not an integer, break out of the loop

# check if any numbers were entered 
if number:
    input_num.sort()    # if so, sort the list in ascending order
    print(input_num)    # display the numbers from lowest to highest


