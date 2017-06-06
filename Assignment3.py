# 3.Write a python standalone program a. insert some values [eg. employee details]in db tab b. fetch the same data and print it on standard output.c. update specific employee info.d. delete specific employee and all the info. 


import sqlite3 
conn = sqlite3.connect('employee.db') 
print "Opened database successfully"; 
# prepare a cursor object using cursor() method 
cursor = conn.cursor()

# Create table as per requirement 
sql = """CREATE TABLE EMP1 ( 
         FIRST_NAME  CHAR(20) NOT NULL, 
         LAST_NAME  CHAR(20), 
         AGE INT,   
         SEX CHAR(1), 
         INCOME FLOAT )""" 
 
 
cursor.execute(sql) 
print "table create successfully" 
# insert value in table 
cursor.execute ("INSERT INTO EMP1(FIRST_NAME, LAST_NAME, AGE, SEX ,INCOME) \
 VALUES ('Ashutosh', 'Meena', 24, 'male', 25000.00 )"); 
print "Records insert successfully" 
 
 
 #display data here 
 cursor.execute ("SELECT FIRST_NAME, LAST_NAME, AGE, SEX ,INCOME from EMP1 ") 
 for row in cursor: 
    print "FIRST_NAME = ", row[0] 
    print "LAST_NAME = ", row[1] 
    print "AGE = ", row[2] 
    print "SEX = ", row[3] 
    print "INCOME= ", row[4],"\n" 
 conn.commit() 
 print "Operation done successfully" 
 
 
 #update data 
 cursor.execute("UPDATE EMP1 set INCOME=25000 where FIRST_NAME='Ashutosh'") 
 conn.commit() 
 #display data here after updation 
cursor.execute ("SELECT FIRST_NAME, LAST_NAME, AGE, SEX ,INCOME from EMP1 ") 
 for row in cursor: 
    print "FIRST_NAME = ", row[0] 
    print "LAST_NAME = ", row[1] 
    print "AGE = ", row[2] 
    print "SEX = ", row[3] 
    print "INCOME= ", row[4],"\n" 
conn.commit() 
print "Records update successfully";


 
 # insert value in table 
 cursor.execute ("INSERT INTO EMP1(FIRST_NAME, LAST_NAME, AGE, SEX ,INCOME) \ 
       VALUES ('vatsal', 'Meena', 20, 'male', 2000.00 )"); 
print "Records insert successfully" 
 
 
 # delete 
cursor.execute("DELETE from EMP1 where LAST_NAME = 'Meena'") 
conn.commit() 
 #display data here after updation 
cursor.execute ("SELECT FIRST_NAME, LAST_NAME, AGE, SEX ,INCOME from EMP1 ") 
 for row in cursor: 
    print "FIRST_NAME = ", row[0] 
    print "LAST_NAME = ", row[1] 
    print "AGE = ", row[2] 
    print "SEX = ", row[3] 
    print "INCOME= ", row[4],"\n" 
print "Records distroy successfully"; 
conn.close()
