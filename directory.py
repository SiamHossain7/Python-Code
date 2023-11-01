import os
#print(os.getcwd())
#output:C:\Users\touhi\Downloads\siam
#os.mkdir('mydir') #used for creating folder
#os.mkdir('mydir/child')# create child file 
'''
folder er moddhe folder tar moddhe folder  
er jonno nicher code
'''
#os.makedirs('parrentdir/childdir/grandchilddir')
#change directory
#print(os.getcwd())
#os.chdir('mydir')#ch=change directory
#print(os.getcwd())

#remane function

#fst write old directory name .then write new directory

#os.rename('mydir','yourdir')
#remove 

#os.rmdir('newdir')#rmdir use for remove directory
#we can also delete child file using this fucntoion
#os.rmdir('newdir/siu')
"""
if we want to remove parentdir,childdir,and grandchild 
then we need to use os.removedirs(parents/child/grandchild)
"""
#os.removedirs('newdir/siuu/cr7')
#walk()
w=os.walk('.')
for i in w:
    print(i)
