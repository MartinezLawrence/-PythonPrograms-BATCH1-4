# display num by highest to lowest
# this program will display numbers entered by the user in descending order

# initialize list
number_list = []

# use while loop to get user input
while True:
    try:
        number_list.append(int(input("Enter a number: ")))  # append the number to the list
    except ValueError:
        break     # break out the loop if the input is invalid

# sort list in descending order
print(sorted(number_list, reverse=True))