import sqlite3
import datetime

f=open('db.sqlite','w')

print("[",datetime.datetime.now(),"] Database created... db.sqlite")

conn=sqlite3.connect('db.sqlite')
print("[",datetime.datetime.now(),"] Database Connected... db.sqlite")

conn.execute('''CREATE TABLE `EXPENDS`
                ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT ,
                `AMOUNT` INTEGER ,
                `REASON` TEXT ,
                `DATE` DATE );
    ''')
conn.execute('''CREATE TABLE `INCOME`
                ( `ID` INTEGER PRIMARY KEY AUTOINCREMENT ,
                `AMOUNT` INTEGER ,
                `REASON` TEXT ,
                `DATE` DATE );
    ''')

print("[",datetime.datetime.now(),"] Database ACCOUNT creating... db.sqlite>ACCOUNT");
print("[",datetime.datetime.now(),"] Database table INCOME created... db.sqlite>ACCOUNT>INCOME");
print("[",datetime.datetime.now(),"] Database table EXPENDS creating... db.sqlite>ACCOUNT>EXPENDS");
print("All are ready. Now run main.py")
