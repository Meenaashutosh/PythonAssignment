#6.Write a program that takes inputs from user their name and their age. And display the year in which they will turn 100 years old.

import time
import datetime
Name=raw_input("Enter your Name:")
Age=int(input("Enter your Age:"))
print 'Hi %s ,Your present Age is %d'%(Name,Age)  
#cd=time.strftime("%d/%m/%Y") 
#cd-age 
#print cd.year
cd1=datetime.datetime.now()
cdy=cd1.year
by=int(cdy-Age)
print 'Your Bday year is %d'%by
by1=int(by+100)
print 'Your age will be 100 years by %d'%by1


#output
'''
Enter your Name:Ashutosh
Enter your Age:24
Hi Ashutosh ,
Your present Age is 24
Your Bday year is 1993
Your age will be 100 years by 2093
'''
