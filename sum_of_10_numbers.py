# sum of 10 numbers
# this program will take 10 numbers from the user and calculate the sum of those numbers   

# prompt the user to enter 10 numbers
sumnum = 0
for numbers in range(10):
    sumnum += float(input("Enter a number: "))

# display the sum of the 10 numbers
print(sumnum)