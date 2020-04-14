import multiprocessing
import time
import os
def input_Q(lock1,lock2,q):
    print("input_Q".center(30,"#"))
    time.sleep(1)
    print("dump into queue...")
    q.put("input_Q is running")
    q.put("everynody wait")
    q.put("let me finish work.")
    lock1.release()
    lock2.release()
    
def output_Q(lock,q):
    print('Oops')
    time.sleep(1)
    lock.acquire()
    print(str(os.getpid()).center(30,"#"))
    print(q.get())
    
    
if __name__ =="__main__":
    lock1 = multiprocessing.Lock()
    lock2 = multiprocessing.Lock()
    q = multiprocessing.Queue(1)
    p1 = multiprocessing.Process(target=output_Q,args=(lock1,q))
    p2 = multiprocessing.Process(target=output_Q,args=(lock2,q))
    p3 = multiprocessing.Process(target=input_Q,args=(lock1,lock2,q))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    
    # REMEMBER FIFO!!