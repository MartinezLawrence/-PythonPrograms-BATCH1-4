# print 0 to 100 except number ending in 0
# This program will print numbers from 0 to 100 except numbers ending in 0

# range must be 101
# if the number is divisible by 10 do not print that number
for numbers in range(101):
    if numbers % 10 != 0:
        print(numbers)  # print numbers from 0 to 100 except numbers ending in 0