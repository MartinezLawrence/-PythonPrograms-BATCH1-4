# all odd from 0 to 100
# this program will print all odd numbers from 0 to 100 using while loop

oddnum = 0              # initialize the variable
while oddnum <= 100:    # while loop will run until the value of number is less than 100
    if oddnum % 2: 
        print(oddnum)   # if the value of oddnum is not divisible by 2 then it will print the value of oddnum
    oddnum += 1         # increment the value of oddnum by 1