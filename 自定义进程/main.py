# -*-coding:utf-8 -*-
import multiprocessing
import time

def foo(i):
    print('say hi',i)
    
for i in range(10):
    p = multiprocessing.Process(target=foo,args=(i,))
    p.start()
    
