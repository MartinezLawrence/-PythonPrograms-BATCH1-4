# even num counter
# this program will count the number of even numbers

evennum = 0  # initialize the counter
for numbers in range(10):   # ask user to input 10 numbers
    if float(input("Enter a number: ")) % 2 == 0:   # check if the number is divisible by 2
        evennum += 1  # add 1 to the counter if the number is divisible by 2

# print the number of even numbers
print(evennum) 