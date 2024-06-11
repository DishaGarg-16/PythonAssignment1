#11. Write a python program that generates the first n numbers in the Fibonacci sequence.
a,b=0,1
for i in range(1,11):
  print(a,end=" ")
  a,b=b,a+b