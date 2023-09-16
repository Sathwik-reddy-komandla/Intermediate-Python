import threading

def helloworld():
    for x in range(10):
        print('Hello world')


def hello():
    for x in range(10):
        print('Hello ',x)


t1=threading.Thread(target=helloworld)
t2=threading.Thread(target=hello)

t1.start()
t1.join()
t2.start()
