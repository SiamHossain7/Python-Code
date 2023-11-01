import mysql.connector
config={'user':'root',
        'password':'siamsiam69',
        'host':'localhost',
        'database':'pdb',
        'port':3306
}

try:
    conn=mysql.connector.connect(**config)
    if conn.is_connected():
        print('database connected')
except:
    print('unable to connect')


sql='INSERT INTO student1 (name,roll,fees)VALUES(%s,%s,%s)'
myc=conn.cursor(prepared=True)
params=('rifat',86,5643)

try:
    myc.execute()
    conn.commit()
    print(myc.rowcoumt,'row inserted')
except:
    conn.rollback()
    print('Unable to connect')
myc.close()
conn.close()