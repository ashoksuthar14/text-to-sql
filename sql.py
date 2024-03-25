import sqlite3

#connect to sqlite
connection = sqlite3.connect("student.db")


#create a cursor object
cursor= connection.cursor()

#create the table
table_info="""
Create table STUDENT(NAME VARCHAR(23),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""

cursor.execute(table_info)

#insert some more records

cursor.execute('''Insert Into STUDENT values('Ramu','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Raju','Science','B',80)''')
cursor.execute('''Insert Into STUDENT values('Rara','Data','A',70)''')
cursor.execute('''Insert Into STUDENT values('Rapu','AI','B',96)''')
cursor.execute('''Insert Into STUDENT values('Rama','CSE','A',67)''')
cursor.execute('''Insert Into STUDENT values('Raka','CEE-AL','B',30)''')
cursor.execute('''Insert Into STUDENT values('kamu','CSE-AL','A',50)''')
cursor.execute('''Insert Into STUDENT values('Ashu','CSE-DS','B',20)''')


#DISPLAY THE Records
print("inserted records are")

data=cursor.execute('''select * from STUDENT''')

for row in data:
    print(row)


#close the connection

connection.commit()
connection.close()
