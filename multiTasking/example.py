# threads are python objects of threding.Thread() class.

import threading
print(threading.current_thread())
print(threading.current_thread().name)
print(threading.current_thread().ident)
print(threading.current_thread().is_alive())
# the threading.current_thread return main thread object

# current_thread()
# this return the current thread function

# import Thread class
from threading import Thread, current_thread
# create a function containing code to be executed parallaly
def display(n, msg):
    print("t1 thread ",current_thread())
    for i in range(n):
        print(msg)
# create new thread here
t1=Thread(target=display, args=(4,"hello"))
# start the new thread
t1.start()

for i in range(4):
    print("welcome")