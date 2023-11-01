import pickle,class_obj

#open file for store object  in byte form
with open('student.dat',mode='wb') as f:#.dat form for binary mood
    stu1=class_obj.Student('Rahul',101,'Bahirgola')
    stu2=class_obj.Student('siam',1005,'vangabai')
#now we need to dumb stu1 object into srudent.dat file .
#dumb mean ,write these object into the file 
#first we need to convert file into byte stream,then we are able to write 
#we convert it into byte form using dump function
    pickle.dump(stu1,f)
    pickle.dump(stu2,f)
    print('pickling Done!')
    
with open ('student.dat',mode='rb') as f:
    #byte stream vonvert into class  object 
    obj1=pickle.load(f)
    obj2=pickle.load(f)
    print('Unpickling done')
    obj1.disp()
    obj2.disp()

        