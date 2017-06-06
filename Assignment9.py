

#9.Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
def max_of_three(a,b,c):
    #DocString
    """ Function to find out the maximum of three numbers """
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
print ("Function finding the largest number among three numbers")
firstNum=int(input("Enter the first  number:"))
secondNum=int(input("Enter the second  number:"))
thirdNum =int(input("Enter the third  number:"))
print ("Largest number from  " +str(firstNum) +", " +str(secondNum) +", " +str(thirdNum) +" is " +str(max_of_three(firstNum,secondNum,thirdNum)))

#Output
'''
Function finding the largest number among three numbers
Enter the first  number: 45
Enter the second  number: 23
Enter the third  number: 26
Largest number from 45, 23, 26 is 45
'''
