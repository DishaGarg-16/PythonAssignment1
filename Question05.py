#5. Write a program that takes a string input from the user and writes it to a text file.
Text=str(input("Enter a Text to the file: "))
NewFile=open("D:/downloads next/TextFile.txt","w")
print(Text, file=NewFile)