#16. Write a program in python that counts the frequency of each character in a string.
str="Welcome to my code"
characters=list(str)
for i in characters:
   print(i,":", characters.count(i))