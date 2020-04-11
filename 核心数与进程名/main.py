import multiprocessing
import time

def process_(i):
    print(f"Process:{i}")
    
if __name__ == '__main__':
    for i in range(8):
        p = multiprocessing.Process(target=process_,args=(i,))
        p.start()
    print("CPU total %d"%(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child process name: %s PID:%d"%(p.name,p.pid))
    print('Main process ENDED....')