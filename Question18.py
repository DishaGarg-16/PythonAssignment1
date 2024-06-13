#18. Write a python program that checks if two strings are anagrams of each other.
#using loops
str1="listen"
str2="silent"
list1=list(str1)
list2=list(str2)
for i in list1:
     for j in list2:
        if i==j:
          anagram=True
          break
if anagram:
    print("The strings are anagrams")

# Alternate using if-else conditional

set1=set(list1)
set2=set(list2)
if set1==set2:
    print("The string are anagrams of each other")
else:
    print("The strings are not anagrams of each other")    

