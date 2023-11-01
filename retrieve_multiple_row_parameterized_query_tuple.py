import mysql.connector
config={'user':'root',
        'password':'siamsiam69',
        'database':'pdb',
        'host':'localhost',
        'port':3306
        
}
try:
    conn=mysql.connector.connect(**config)
    if conn.is_connected():
        print('Database connect successfully')
except:
    print('Unable to connect')
    
sql='SELECT * FROM student1 where roll =%s'
myc=conn.cursor()
n=int(input('Enter the roll number  want to display:'))
'''
আমারা while loop use করেছি ,যেনো এক নামে যত রোল আছে ,এক এক করে সবাই কে
retrive করতে পারে ।
এইখানে while loop user করার আরো কারন আছে, আমরা যানি না কত বার retrive হবে ,
তাই আমরা while llop use korechi/
'''
try:
    myc.execute(sql,(n,))
    row=myc.fetchone()
    while row is not None:
        print(row)
        row=myc.fetchone()
    print('Total Rows:',myc.rowcount)      
except:
    conn.rollback()
    print('Unable to Retrieve Data')
myc.close()
conn.close()