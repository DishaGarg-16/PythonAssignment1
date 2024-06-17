#19. Write a python program that removes all punctuation from a given string.
str="Hello! This is my 'code', thank you."
punctuations="!:;.,?-''()"
for i in str:
    for j in punctuations:
       if i==j:
        str=str.replace(i,"")
print("After removing punctuations string is,",str)