#12. Write a python program that calculates the sum of the digits of a given number.
str="421"
result=list(str)
list_num=[]
for i in result:
    list_num.append(int(i))
print("the sum of digits:", sum(list_num))