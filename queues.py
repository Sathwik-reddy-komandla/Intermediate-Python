# import queue
# q=queue.Queue()

# nums=[10,20,30,40,50,60,70,80,90]

# for num in nums:
#     q.put(num)


# import threading
# def getele():
#     global q
#     print(q.get(),end='\n')

# t1=threading.Thread(target=getele)
# t2=threading.Thread(target=getele)
# t3=threading.Thread(target=getele)


# t1.start()
# t2.start()
# t3.start()

# last in first out queue

import queue

# q=queue.LifoQueue()


# Priority queue
q=queue.PriorityQueue()
q.put((5,'bob'))

q.put((100,'sathwik'))
q.put((2,'Hello'))

while not q.empty():
    print(q.get())