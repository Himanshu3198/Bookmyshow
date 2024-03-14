print("Hello world")
# list in python can have different datatype element
# slicing of list in python
mylist = [1, 2, 3, 4, 5, 6, 7, 8]
a = mylist[1:5]
b = mylist[0:-1]
# c=mylist[-1:5]
# print(c)
if 12 in mylist:
    print("two is present")
else:
    print("not found")

# reverse a list
c = mylist[::-1]
# print(c)
#  create a new list
newlist1 = [i * 2 for i in mylist]
print(newlist1)
