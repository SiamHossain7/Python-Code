import mysql.connector
config={'user':'root',
        'password':'siamsiam69',
        'host': 'localhost',
        'database': 'pdb', 
        'port':'3306'
}
try:
    conn=mysql.connector.connect(**config)
    if conn.is_connected():
        print('database connected')
except:
    print('database not connected')


sql='DELETE FROM student where student_id = 17'
myc=conn.cursor()

try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount,'Row deleted')
except:
    conn.rollback()

myc.close()
conn.close()
    