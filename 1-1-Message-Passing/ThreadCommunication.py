from queue import Queue
from threading import Thread

def sender(q):
    q.put("Hello from sender")

def receiver(q):
    msg = q.get()
    print("Received:", msg)

q = Queue()
t1 = Thread(target=sender, args=(q,))
t2 = Thread(target=receiver, args=(q,))
t1.start()
t2.start()
t1.join()
t2.join()