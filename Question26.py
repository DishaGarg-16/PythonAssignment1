'''26. Write a program in python that checks if a string starts with a given prefix
or ends with a given suffix.'''
prefix=["un","in","re"]
suffix=["ee","ism","hood"]
str=input("enter a word with a prefix or suffix: ")
for i in prefix:
    if i in str[0:2]:        # sliced to avoid the prefix letters coming in between eg. landing, bun
        print("The prefix is",i,"in the word",str)
        break
    break
for j in suffix:
    if j in str:
        print("The suffix is",j,"in the word",str)
        break
else: 
    print("No prfix or suffix in this word")