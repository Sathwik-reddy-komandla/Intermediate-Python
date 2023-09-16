import threading
import time
semaphore=threading.BoundedSemaphore(value=2)

def access(thread_number):
    print('{} is trying to access'.format(thread_number))
    semaphore.acquire()
    print('**************************** {} ********** is granted access'.format(thread_number))
    time.sleep(6)
    print('*******{}****** is releasing'.format(thread_number))
    semaphore.release()

for x in range(1,11):
    t=threading.Thread(target=access,args=(x,))
    t.start()
    time.sleep(1)
