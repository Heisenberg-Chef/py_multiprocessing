
import random
import multiprocessing
import time

import os

def run(name):
    print("%s child processes started,PID：%d"%(name,os.getpid()))
    start = time.time()
    time.sleep(random.choice([1,2,3,4]))
    end = time.time()
    print("%s child process ended,PID: %d.delay in 0.2%f"%(name,os.getpid(),end-start))
    
if __name__=='__main__':
    print('father process is engaging...')
    #   创建多个进程表示可以同时执行的进程数，默认大小是CPU的核心数量。
    pool = multiprocessing.Pool(processes = 4) #  VVVVVVIP
    for i in range(10):
        print('hello %d'%(i))
        #创建进程，放入进程池中，统一进程管理。
        pool.apply(run,args=(i,))       #  阻塞进程。一个一个处理
        pool.apply_async(run,args=(i,))#    async就是异步的意思，map map_async也是相同的感觉，使用join要不主进程end直接释放了儿子进程
        
    #   如果我们使用的是进程池，在调用join()之前必须要close()，并且在close()之后不能在继续向池子中添加
    #   否则会说pool is still running
    pool.close()
    #   进程池对象调用join，会等待进程池中的所有子进程结束之后再去结束父进程
    pool.join()
    print('father process ended....')
    '''
import random
from multiprocessing.pool import Pool
from time import sleep, time

import os


def run(name):
    print("%s子进程开始，进程ID：%d" % (name, os.getpid()))
    start = time()
    sleep(random.choice([1, 2, 3, 4]))
    end = time()
    print("%s子进程结束，进程ID：%d。耗时0.2%f" % (name, os.getpid(), end-start))


if __name__ == "__main__":
    print("父进程开始")
    # 创建多个进程，表示可以同时执行的进程数量。默认大小是CPU的核心数
    p = Pool(8)
    for i in range(10):
        # 创建进程，放入进程池统一管理
        p.apply_async(run, args=(i,))
    # 如果我们用的是进程池，在调用join()之前必须要先close()，并且在close()之后不能再继续往进程池添加新的进程
    p.close()
    # 进程池对象调用join，会等待进程吃中所有的子进程结束完毕再去结束父进程
    p.join()
    print("父进程结束。")
'''