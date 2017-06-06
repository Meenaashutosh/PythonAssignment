#16.Write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

list = [5,6,77,45,22,12,24]
list = [x for x in list if x%2!=0]
print list

#output
'''
[5, 77, 45]
'''
