for basic in range(151):
    print(basic) #print 0-150

for fives in range(5,1001,5):
    print(fives) #printing multiple of 5 from 5-1000

for dojo in range(1,101):
    if ((dojo%5==0) and (dojo%10!=0)): #looks for num divisible by 5 and not by 10
        print("Coding")
    elif (dojo%10==0): #looks for num divisible by 10
        print("Coding Dojo")
    else: #prints everything else
        print(dojo)

sum = 0
for huge in range(500001):
    if (huge%2!=0): #only uses nums if they have a remainder when divided by 2
        sum = sum + huge #add to current sum
print(sum)

countdown = 2018
print(countdown)
while countdown > 2: 
    countdown -= 4 #subtract 4 from current countdown value
    print(countdown)

lowNum = 2
highNum = 15
mult = 4
for flex in range(lowNum,highNum):
    if (flex%mult==0):
        print(flex)