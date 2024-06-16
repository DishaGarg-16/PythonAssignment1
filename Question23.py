'''23. Write a program that converts temperature from Celsius to Fahrenheit
and vice versa based on user input.'''
def celcius_to_f():
    c=int(input("Enter temperature in celcius "))
    f=((1.8)*c)+32
    print(f,"farhenheit")
    return 
celcius_to_f()

def farhenheit_to_c():
    f=int(input("Enter temperature in farhenheit "))
    c=(f-32)*(5/9)
    print(c,"celcius")
    return
farhenheit_to_c()