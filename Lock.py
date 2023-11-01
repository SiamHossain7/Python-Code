

from threading import * 
import time 

class Airplane:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.l=Lock()
        
     

    def reverse(self, need_seat, name):
        self.l.acquire(blocking=True,timeout=2)
        print(f'Available seats: {self.available_seat}')
       
        if self.available_seat >= need_seat:
                print(f'{need_seat} seat is allotted for {name}')
                self.available_seat -= need_seat
             
        else:
            print('Sorry, all seats are allotted  ')
        self.l.release()

f = Airplane(2)
t1 = Thread(target=f.reverse, args=(1, 'siam'), name='siam')
t2 = Thread(target=f.reverse, args=(1, 'nirob'), name='nirob')
t3 = Thread(target=f.reverse, args=(1, 'sam'), name='sam')

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print('Main Thread')
