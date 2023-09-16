import threading
import time


x=8192

lock=threading.Lock()

def double():
    global x
    lock.acquire()
    while x<16384:
        x*=2
        print(x)
        time.sleep(2)
    print('reached max value')
    lock.release()


def half():
    global x
    lock.acquire()

    while x>1:
        x/=2
        print(x)

        time.sleep(1)

    print('minimum value reached')
    lock.release()


t1=threading.Thread(target=half)
t2=threading.Thread(target=double)

t1.start()
t2.start()



