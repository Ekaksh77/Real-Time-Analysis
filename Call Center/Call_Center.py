import datetime
import time
import random
import pyodbc


con = pyodbc.connect('Driver={SQL Server};'
                     'Server=Ekaksh\\SQLEXPRESS;'
                     'Database=Call_Center;'
                     'Trusted_Connection=yes;')

cursor = con.cursor()

while 1 == 1:
    date = datetime.date.today()
    location = random.randint(111, 201)
    company = random.randint(11, 30)
    issue = random.randint(111, 130)
    csr = random.randint(111, 210)
    rtime = random.randint(1, 300)
    ctime = random.randint(1, 600)
    status = random.randint(1, 4)

    if status< 75:
        status = 1

    elif status < 85:
        status = 2

    elif status < 90:
        status = 3

    else:
        status = 4
    
    if status == 1:
        rating = random.randint(5, 10)
    elif status == 2:
        rating = random.randint(3, 8)
    elif status == 3:
        rating = random.randint(1, 3)
    elif status == 4:
        rating = random.randint(1, 5)

    print(date)
    cursor.execute('insert into calls values(GETDATE(),'
                    + str(location)+','
                    + str(company)+','
                    + str(issue)+','
                    + str(csr)+','
                    + str(rtime)+','
                    + str(ctime)+','
                    + str(status)+','
                    + str(rating)+')'
                    )
    cursor.commit()
    time.sleep(1)
'''print(location)
    print(company)
    print(issue)
    print(csr)
    print(rtime)
    print(ctime)
    print(status)
    print(rating)'''
    

