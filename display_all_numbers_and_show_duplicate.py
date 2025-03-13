# display all numbers and show duplicates only once
# This program will display all numbers and show duplicates only once

# Initialize an empty list to store user input numbers
number_list = []

# Loop to ask the user for 10 numbers
for list_of_numbers in range(10):   # 10 numbers
    number_list.append(int(input("Enter a number: ")))  # Add the numbers to the list

# Use a set to keep track of numbers we have already input
done_input = set()

# Initialize an empty list to store unique entries
unique_entries = []

# Loop through each number in the input list
for number in number_list:
    # If the number has not been input before, add it to the unique list
    if number not in done_input:  # Check if the number has been input before
        
        # If not, add it to the unique entries and mark it as done input
        unique_entries.append(number) 
        done_input.add(number)

# print the unique entries
print(unique_entries)