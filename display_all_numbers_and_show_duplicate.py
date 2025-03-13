# display all numbers and show duplicates only once
# This program will display all numbers and show duplicates only once

# Initialize an empty list to store user input numbers
numbers = []

# Loop to ask the user for 10 numbers
for list_of_numbers in range(10):   # 10 numbers
    numbers.append(int(input("Enter a number: ")))  # Add the numbers to the list

# Use a set to keep track of numbers we have already input
# Initialize an empty list to store unique entries
# Loop through each number in the input list
# print the number if it is not in the unique list