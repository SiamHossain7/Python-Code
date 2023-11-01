import mysql.connector
config={ 
        'user':'root',
        'password':'siamsiam69',
        'host':'localhost',
        'port':3306
}
try:
    conn=mysql.connector.connect(**config)
    if(conn.is_connected()):
        print('connected successfully')
    
except:
    print('error')
sql='SHOW  DATABASES'
myc=conn.cursor()
myc.execute(sql)
for d in myc:
    print(d )

myc.close()
conn.close()