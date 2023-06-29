import time
from threading import Thread

def do_this():
    print('Starting this thread-001!')
    time.sleep(2)
    print('Did this thread-001!')

def do_that():
    print('Starting that thread-002!')
    time.sleep(3)
    print('Did that thread-002!')


t1 = Thread(target=do_this)
t1.start()

t2 = Thread(target=do_that)
t2.start()

#without thread
# do_this()
# do_that()