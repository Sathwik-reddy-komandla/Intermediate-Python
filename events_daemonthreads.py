# import threading

# event=threading.Event()

# def myfunction():
#     print("Waiting for the event to trigger...")
#     event.wait()
#     print('Performing action XYZ now...')

# t1=threading.Thread(target=myfunction)
# t1.start()

# x=input('Do you want to trgger the event (y/n)? ')
# if x=='y':
#     event.set()



# //Daemon Thread

import threading,time

path='text.txt'
text=''

def readFile():
    global text,path

    while True:
        with open('text.txt','r')as f:
            text=f.read()
        time.sleep(3)

def printloop():
    for x in range(20):
        print(text)
        time.sleep(1)

t1=threading.Thread(target=readFile,daemon=True)
t2=threading.Thread(target=printloop)

t1.start()
t2.start()
