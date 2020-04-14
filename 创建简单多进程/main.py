import multiprocessing
import time

def foo(i):
    print('say hi',i)
    while 1:
        time.sleep(10)
        pass

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=foo,args=(i,))
        p.start()
        print(p.pid)