import os
import multiprocessing
import time
#------------------------
# input worker
def inputQ(queue):
    info = str(os.getpid()) + '(put)-->' + str(time.time())
    queue.put(info)

# output worker
def outputQ(queue,lock):
    info = queue.get()
    lock.acquire()
    print(str(os.getpid()) + ' get-->' + info)
    lock.release()

#-------------------
# main
record1 = []
record2 = []

lock = multiprocessing.Lock()   #   To prevent meesage print
queue = multiprocessing.Queue(3)

if __name__ == '__main__':
    #   input processes
    for i in range(10):
        process = multiprocessing.Process(target = inputQ,args = (queue,))
        process.start()
        record1.append(process)

    #   output process
    for i in range(10):
        process = multiprocessing.Process(target = outputQ,args = (queue,))
        process.start()
        record2.append(process)

    for p in record1:
        p.join()

    queue.close()

    for p in record2:
        p.join()