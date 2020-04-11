# -*-coding:utf-8 -*-
import multiprocessing
import time

def foo(i):
    time.sleep(1)
    print('ssay hi',i)
    time.sleep(1)
    
if __name__ == '__main__':
    p_list=[]
    for i in range(10):
        p = multiprocessing.Process(target=foo,args=(i,))
        p.daemon = True
        p_list.append(p)
        
    for p in p_list:
        p.start()
    for p in p_list:
        p.join
        
    print('Main process ended!')
        