# numbers from 0 to 100 except numbers ending 0 and 5
# this program will display numbers from 0 to 100 except numbers ending 0 and 5

for number in range(101):   # range function will generate numbers from 0 to 100
    if number % 10 not in [0, 5]:    # if num is not divisible by 5 and 10 then print num
        print(number)   # print number