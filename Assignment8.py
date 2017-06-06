
#8. Define a function max() that takes two numbers as arguments and returns the largest of them.

def max(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None


if __name__ == "__main__":
    print max(2, 4)
    print max(4, 4)
    print max(4, 2)

    #output
    '''
    python Assignment8.py 
    4 
    None
    4'''
