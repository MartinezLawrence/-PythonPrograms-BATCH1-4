# num1 minus 9numbers
# this program will print the result of the first number minus all of the remaining numbers

# prompt the user to enter the first number
num1 = float(input("Enter the first number: "))

for numbers in range(9):  # the range of the loop is 9 because we are going to ask the user to enter 9 numbers
    num1 -= float(input("Enter your number: ")) # enter the next 9 number and subtract it from the first number

# print the result of the first number minus all of the remaining numbers
print(num1)