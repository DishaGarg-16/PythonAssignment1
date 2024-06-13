#20. Write a python program that takes a list of numbers and returns their sum.
numbers=input("Enter the numbers ")  # give space between the numbers for this solution
list1=[]
for i in numbers.split():
    list1.append(int (i))
print(list1)
print(sum(list1))
'''
# Another solution
list2=[]
for i in numbers:
  list1.append(i)
for x in list1:
    list2.append(int(x))
print(list2)
print(sum(list2))
'''