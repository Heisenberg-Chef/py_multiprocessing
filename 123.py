import multiprocessing
lock = multiprocessing.Lock()
def func(lock):
    print('func'.center(30,'-'))
    lock.acquire()
    print('will not the printed')
    lock.release()
    
if __name__ == '__main__':
    p = multiprocessing.Process(target=func,args=(lock,))
    p.start()
    p.join()