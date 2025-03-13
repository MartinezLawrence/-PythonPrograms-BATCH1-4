# display number that have duplicate
# this program will display the number that have duplicate in the list

# # Initialize an empty list to store user input numbers
numbers = []

# loop 10 times to ask user to input number 10 times
for list_of_numbers in range(10):   # 10 numbers
    numbers.append(int(input("Enter a number: ")))  # Add the numbers to the list

# use list comprehension to get the number that have duplicate
duplicate = [n for n in numbers if numbers.count(n) > 1]

# display the number that have duplicate
print(duplicate)