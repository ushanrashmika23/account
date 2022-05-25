import sqlite3 as sql
import sys
import datetime
from tabulate import tabulate

date=datetime.datetime.today().strftime('%Y-%m-%d')
print(date)

conn = sql.connect('db.sqlite')
cur = conn.cursor()

'''
-d : deposit
-t : takeover
'''

def banner():
    print("\33[92m    _    ____ ____   __  __")
    print("   / \  / ___/ ___| |  \/  | __ _ _ __   __ _  __ _  ___ _ __")
    print("  / _ \| |  | |     | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|")
    print(" / ___ \ |__| |___  | |  | | (_| | | | | (_| | (_| |  __/ |")
    print("/_/   \_\____\____| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|")
    print("                                              |___/")
    print("")
    print("\33[36m 1.Deposit\n 2.Take Back")
    print("")
    print(
        "\33[33mTo add record, Rerun main.py like as this :- \n \33[31m>>> python main.py [number of operatin] [amount of money] ['reason']")
    print("")


def deposit(amount,reason):
    amount=int(amount)
    reason=reason
    query=str("INSERT INTO INCOME (AMOUNT,REASON,DATE) VALUES ({0},'{1}','{2}')".format(amount,reason,date))
    print(query)
    cur.execute(query);
    print("Deposit Successful...")
    print(date)

def takeOver(amount,reason):
    amount=int(amount)
    reason=reason
    query=str("INSERT INTO EXPENDS (AMOUNT,REASON,DATE) VALUES ({0},'{1}','{2}')".format(amount,reason,date))
    print(query)
    cur.execute(query);
    print("Takeback successful...")

def explorer():

    balance()

    print("======")
    print("INCOME")
    print("======")
    table=[]
    cur.execute("SELECT * FROM INCOME")
    output = cur.fetchall()
    for row in output:
        line=[]
        for cell in row:
            line.append(cell)
        table.append(line)
    print(tabulate(table,headers=['ID','AMOUNT','REASON','DATE'],tablefmt="grid"))

    print("=======")
    print("EXPENDS")
    print("=======")
    table=[]
    cur.execute("SELECT * FROM EXPENDS")
    output = cur.fetchall()
    for row in output:
        line=[]
        for cell in row:
            line.append(cell)
        table.append(line)
    print(tabulate(table,headers=['ID','AMOUNT','REASON','DATE'],tablefmt="grid"))

def balance():
    table=[['INCOME','EXPENDS','BALANCE']]
    l=[]

    query0="SELECT SUM(AMOUNT) FROM INCOME"
    cur.execute(query0)
    output=cur.fetchall()
    incomeL=list(str(output[0][0]))
    income=''
    for i in incomeL:
        income=income+i
    l.append(income)

    query0="SELECT SUM(AMOUNT) FROM EXPENDS"
    cur.execute(query0)
    output=cur.fetchall()
    expendsL=list(str(output[0][0]))
    expends=''
    for i in expendsL:
        expends=expends+i
    l.append(expends)

    balance=str(int(income)-int(expends))
    l.append(balance)
    table.append(l)

    print(tabulate(table,tablefmt="pretty"))

def recArgs():
    print('\33[92m')
    args=sys.argv
    if(len(args)==1):
        balance()
    else:
        if(args[1]=='-d'):
            deposit(args[2],args[3])
        elif(args[1]=='-t'):
            takeOver(args[2],args[3])
        elif(args[1]=='-e'):
            explorer()


banner()
recArgs()
conn.commit()
conn.close()
print('\33[37m')