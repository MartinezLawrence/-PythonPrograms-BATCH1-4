# display in between number
# this program will print all the numbers between the two numbers given by the user

# get the two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# swap the numbers if the first number is greater than the second number
if num1 > num2: 
    num1, num2 = num2, num1 

# add 1 in range because the second number is not included in the range
for numbers in range(num1 + 1, num2):
    print(numbers)     # print the numbers in between the two numbers
