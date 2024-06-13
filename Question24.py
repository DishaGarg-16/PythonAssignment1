'''24. Write a program that acts as a simple calculator. It should take two
numbers and an operator (+, -, *, /) as input and print the result.'''
'''
# Simple Calculator
while True:
    num1=int(input("Enter 1st number: "))
    num2=int(input("Enter 2nd number: "))
    opr=input("Give an operator (+, -, *, /): ")
    if opr=="+":
       print("The sum is,",num1+num2)
       break
    elif opr=="-":
       print("The difference is,",num1-num2)
       break
    elif opr=="/":
       print("The division is,",num1/num2)
       break
    elif opr=="*":
       print("The multiplication is",num1*num2)
       break
    else:
       print("Invalid Input")    
'''
# The following program is for endless calculations until user enters q as operator
while True:
    num1=int(input("Enter 1st number: "))
    num2=int(input("Enter 2nd number: "))
    opr=input("Give an operator (+, -, *, /, q to quit): ")
    if opr=="+":
       print("The sum is,",num1+num2)
    elif opr=="-":
       print("The difference is,",num1-num2) 
    elif opr=="/":
       print("The division is,",num1/num2) 
    elif opr=="*":
       print("The multiplication is",num1*num2)
    elif opr=="q":
       break
    else:
       print("Invalid Input")
