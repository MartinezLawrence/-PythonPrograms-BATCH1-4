# display numbers without duplicate
# This program is to display numbers that has no duplicate

# Initialize an empty list to store user input numbers
numbers = []

# Loop to ask the user for 10 numbers
for list_of_numbers in range(10):   # 10 numbers
    numbers.append(int(input("Enter a number: ")))  # Add the numbers to the list
    
# Use list comprehension to find numbers that appear only once
unique_numbers = [num for num in numbers if numbers.count(num) == 1]

# Print the numbers without duplicates
print(unique_numbers)