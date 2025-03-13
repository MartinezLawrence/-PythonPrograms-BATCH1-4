# print remainder
# this program will print the remainder when the first number is divided by the second number

# prompt user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# print the remainder when the first number is divided by the second number
if num2:    # check if the second number is not zero
    print(num1 % num2)   # print the remainder