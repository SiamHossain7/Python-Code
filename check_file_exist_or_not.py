import os
if os.path.isfile('student.txt'):
    f=open('student.txt')
    print('File Opend')
    f.close()
else:
    print('file not found')
