#25. Write a program that copies the contents of one text file to another.
file1=open("D:/TextFile1.txt","r")
content=file1.read()
file2=open("D:/TextFile2.txt","w")
copy_to=file2.write(content)
file2=open("D:/TextFile2.txt","r")
print(file2.read())