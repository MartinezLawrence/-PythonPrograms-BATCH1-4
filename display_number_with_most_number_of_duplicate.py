# display number with most number of duplicate
# This program will display the number with the most number of duplicates

# Initialize the list
number_list = []

# use a while loop to get the input from the user until invalid input is entered
while True: 
    try:
        # attempt to convert the input to an integer
        number_list.append(int(input("Enter a number: ")))  # append the number to the list
    except ValueError:
        break       # break out the loop if the input is invalid

# find the maximum number of duplicates
max_count = max([number_list.count(number) for number in number_list])

# use list comprehension to get the number with the most number of duplicates
print([amount for amount in number_list if number_list.count(amount) == max_count])