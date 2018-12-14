import select
import socket
from time import time
from threading import Thread

# Creating the socket is specifically to support Windows. Windows can't do
# a select call with an empty list.
def slow_systemcall():
    select.select([socket.socket()], [], [], 0.1)


# Example 7
start = time()
for _ in range(5):
    slow_systemcall()
end = time()
print('Took %.3f seconds' % (end - start))


# Example 8
start = time()
threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()
end = time()
print('Took %.3f seconds' % (end - start))