import multiprocessing
import os
import time

def write_(q):
    print("Engaging Write process:%s"%os.getpid())
    for i in ['A','B','C','D']:
        q.put(i)
        time.sleep(1)
    print("finished building...")
    
def read_(q):
    print("Engaging Read process ")
    