# display average
# this program will display the average of the number inputted

# initialize an empty list
number_list = []

# use while loop to continuously get the input from the user
while True:
    try:
        number_list.append(int(input("Enter a number: ")))  # append the number to the list
    except ValueError:
        break  # break out the loop if the input is invalid

# calculate and print the average of the numbers in the list
print(sum(number_list) / len(number_list))  # sum of the list divided by the length of the list