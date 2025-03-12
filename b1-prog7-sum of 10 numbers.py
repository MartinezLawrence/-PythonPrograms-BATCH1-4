# sum of 10 numbers
# this program will take 10 numbers from the user and calculate the sum of those numbers
# prompt the user to enter 10 numbers
# add them all together and print

numbers = 0
for numbers in range(10):
    numbers += float(input("Enter a number: "))
print(numbers)