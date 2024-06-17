#3. Write a python program that calculates the factorial of a given number
fact=1
num=int(input('Enter a number to find factorial: '))
if num==0 or num==1:
    print("The factorial of 0 or 1 is 1")
else:
    while num>1:
     fact=fact*num
     num=num-1
    print(fact, "is the factorial")