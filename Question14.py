"""14. Write a program that reads multiple lines of input from the user until they 
enter an empty line, then prints all the lines."""

str=input("Enter your lines: ")
while True:
    lines=input("Continue writing ")
    if lines==" ":
        break
    else:
        str=str +" "+lines
print(str)