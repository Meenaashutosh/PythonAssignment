#1. Write a python script for creating directory,displaying its contents.

import os,sys
os.mkdir("Ashutosh")
os.chdir("Ashutosh")
os.system("touch file1")
os.system ("ls")
os.system("cat file1")

#output
'''
python Assignment1.py
file1'''

