#20.Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
def palindrome_no(s):
   if len(s)<1:
	return true
   else:
	if s[0]==s[-1]:
	    return palindrome(s[1:-1])
	else:
	    return false
a=str(input("Enter string"))
if(palindrome(a)==true):
	print("string is palindrome..")
else:
	print("string is not a palindrome")
