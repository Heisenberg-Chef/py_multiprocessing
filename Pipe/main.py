import multiprocessing

def proc1(pipe):
    pipe.send('hello')
    print('proc1 rec:',pipe.recv())

def proc2(pipe):
    print("pro2 rec:",pipe.recv())
    pipe.send('hello too')

#   build a pipe

pipe_obj = multiprocessing.Pipe()

#   main thread

if __name__ == '__main__':
    #   Pass an end of the Pipe to process 1
    p1 = multiprocessing.Process(target=proc1,args=(pipe_obj[0],))
    #   pass the other end of the pipe to process 2
    p2 = multiprocessing.Process(target=proc2,args=(pipe_obj[1],))

    print(pipe_obj)
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    """
    每次调用只有2端，可以定义一边发送一边接受
    """