#insert row
import mysql.connector
config = {
    'user': 'root',
    'password': 'siamsiam69',
    'host': 'localhost',
    'database': 'pdb',
    'port': 3306
}

try:
    conn = mysql.connector.connect(**config)
    if conn.is_connected():
        print('Database connected')
except:
    print('Database not connected')
#sql='INSERT INTO student (name,roll,fees) VALUES("nirob",1006,6700.34)'
#here we see how can we store multiple values 
sql='INSERT INTO student (name,roll,fees) VALUES("mr.X",1007,6760.94),("rahi",1007,7899.43),("mahi",10089,56450.56)'
myc=conn.cursor()
try:
    
    myc.execute(sql)
    conn.commit()
    print('Row inserted')
except:
    conn.rollback()
    print('unable to insert data')
myc.close()
conn.close()
