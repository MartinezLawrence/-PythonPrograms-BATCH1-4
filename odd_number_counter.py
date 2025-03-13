# odd number counter
# Lawrence Andrew B. Martinez
# This program counts the number of odd numbers in 10 numbers

# prompt the user to input 10 numbers
oddnum = 0
for numbers in range(10):
    if float(input("Enter a number: ")) % 2:
        oddnum += 1

# display the number of odd numbers
print(oddnum)