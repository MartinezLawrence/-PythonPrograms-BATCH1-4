# display highest number in while loop
# this program will display the highest number entered by the user

# initialize the variables
number_list = []

# use while loop to continously ask the user for a number
while True:
    try:
        number_list.append(int(input("Enter a number: ")))  # append the number to the list
    except ValueError:
        break     # break out the loop if the input is invalid

# print the maximum number entered by the user
print(max(number_list))