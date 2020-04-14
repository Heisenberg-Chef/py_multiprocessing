import multiprocessing
import time

def Foo(i):
    time.sleep(2)
    return i + 100

def Bar(arg):
    print(arg)
    
if __name__ == '__main__':
    t_start = time.time()
    pool = multiprocessing.Pool(8)
    
    for i in range(10):
        #pool.apply_async(func=Foo,args=(i,),callback=Bar) # 维持执行的进程总数为processes，当一个进程执行王弼后添加新的进程进去。
        pool.apply(func=Foo,args=(i,))
    pool.close()
    
    pool.join()    #   进程池中进程执行完毕后再关闭，如果注释那么直接关闭程序了
    pool.terminate()
    t_end=time.time()
    t = t_end-t_start
    print("program time is %s"%t)