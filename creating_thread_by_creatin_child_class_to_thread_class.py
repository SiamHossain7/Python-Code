#run method.here run override  from thread
#from threading import Thread
#class Mythread(Thread):
   # def run(self):
       #print('Run Method')
#t=Mythread()
#t.start()
# join method
from threading import Thread

class Mythread(Thread):
    def run(self):
        for i in range(5):
            print('child Method')
t=Mythread()
t.start()
t.join()
for i in range(5):
    print('Main THread')