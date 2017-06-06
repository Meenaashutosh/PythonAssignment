#9. Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

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