#   多进程：multiprocessing
####    前言
+  unix/linux操作系统提供了一个fork()系统调用，它非常特殊，普通的函数调用，调用一次，返回一次，但是fork()调用一次返回两次，因为操作系统自动吧当前父进程复制了一个然后分别在父、子进程中返回。
      + 子进程永远返回0，而父进程返回子进程的ID，这样一个父进程可以fork出很多子进程， 
      + windows没有fork调用，而如果我们需要在windows上编写python多进程程序，我们需要使用multiprocessing
    
+   由于GIL的存在，python中的多线程其实并不是多线程，如果要充分的使用CPU资源，在python中大部分情况需要使用多进程，python提供了一个multiprocessing，只需要定义一个函数，python会完成其他所有事情，借助这个包，可以轻松完成从单进程到并发执行的转换。multiprocessing支持子进程、通信和共享数据，执行不同形式的同步。提供了
    +   Process
        +   multiprocessing 支持三种启动方式
            1.  spawn：父进程启动一个新的python解释器，子进程在开始时候只会运行run()方法所需的资源，特别是父进程中非必须的文件描述符和句柄是不会被集成的，相当于使用fork或者forkserver，这个方法启动进程特别慢。
            2.  os.fork()：这个api产生python解释器分叉，子进程在开始时实际与父进程是相同的，父进程的所有资源都被继承。
            3.  forkserver：将启动服务进程，将启动服务器进程。从那时起，每当需要一个新的进程时候，父进程就会连接到服务器请求一个分叉进程，分叉服务器时单线程的，因此使用os.fork()是安全的，没有不必要的资源继承问题。
    +   Queue
    +   Pipe
    +   Lock
+   multiprocessing包与Threading类似他可以利用multiprocessing.Process对象来创建一个进程。与线程函数threading类似，他可以利用start(),run(),join()的方法，类似于Lock\Event\Semaphore\Condition这些多线程对象，用以同步进程，其用法与threading包的同类明一致，所以multiprocessing的很大一般分与threading使用同一套API，只不过换到了多进程的请经理，但是在使用这些共享API时候需要注意：
    +   Unix平台上，当某个进程终结之后，该进程需要被其父进程调用wait，否则进程成为僵尸进程(Zombie)，所以有必要对每个Process对象调用join()方法（实际上是等同于wait），对于多线程来说，由于只有一个进程，所以不存在这个必要性。
    +   multiprocessing提供了threading包中没有的IPC(比如Pipe和Queue)，效率上更高。应优先考虑Pipe和Queue，避免使用Lock\Event\Semaphore\Condition等同步方法（他们占据的不是用户进程的资源）
    +   多进程应该避免共享资源，在多线程中，我们可以比较容易的共享资源，比如使用全局变量或者传递参数，在多进程情况下，由于每个进程有自己独立的内存空间，以上方法并不合适，此时我们可以通过共享内存和Manager方法来共享资源，这样做提高了程序的复杂度，因为同步的需要降低了程序的效率。
+   Process.PID中保存了PID，如果进程还没有start()，则PID为None。
+   **windows系统下需要注意，如果想要启动一个紫禁城，必须加上那句if __name__=='__main__':,继承相关的要写在这句下面

+   Process([group [, target [, name [, args [, kwargs]]]]])
    +   group线程组，目前还没有实现
    +   target：要执行的方法
    +   name：进程名字
    +   args,kwargs参数
    +   一些内置的方法：
        +   is_alive()：进程是否在运行
        +   join(timeout):阻塞当前上下文进程，直到调用进程结束
        +   start()开启线程
        +   run()：run()方法
        +   terminate()：无论是否完成，立即停止进程
    +   属性
        +   authkey
        +   daemon:和setDaemon功能一样，设置守护线程
        +   exitcode(运行时候为None，如果为-N，则表示有N信号时候退出)
        +   name
        +   pid：进程名字
+   使用cpu_count()方法和active_children()方法获得当前CPU的核心数以及目前所有的运行进程
+   全局变量再多个进程中不能共享：子进程对父进程中的全局变量进行修改是完全没有影响的，线程是隔离开的，内存数据都是独立开的。

####    pool类
+   进程池内部维护一个进程序列，当使用的时候，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进程，那么程序就一直会等待，知道进程池有可用进程位置。
+   pool([processes[,initilier[,initargs[,maxtasjsperchild[,context]]]]]) 类型的构造方法，
    +   processes：使用工作进程的数量，如果processes是None那么使用os.cpu_count()返回的数量。
    +   initializer：如果initalizer是None,那么每一个工作进程在开始的时候会调用initilizer(*initargs).
    +   maxtasksperchild:工作进程退出之前可以完成的任务数，完成后用一个新的工作进程来替代原进程，来让限制的资源被释放，默认的maxtasksperchild是None，意味着只要pool存在工作进程就会一直存活。
    +   context:用来指定启动时上下文，一般multiprocessing。Pool()或者一个context对象的pool方法出的池。
    +   实例方法：
        +   apply(func[,args[,kwds]):同步进程池
        +   apply_async(func[,args[,kwwds[,callback[,error_back]]]]):异步进程池。
        +   close()：关闭进程池，组织更多的任务提交到pool,待任务完成后，工作进程会退出
        +   terminate()：结束工作进程，不在处理未完成的任务。
        +   join()：wait工作线程的退出，在调用join钱必须调用close()或者terminate()，这样是因为被终止的进程需要被父进程wait，否则成为僵尸进程。pool.join()必须使用在pool.close()或者pool.terminate()之后。其中close()跟terminate()的区别在于close()会等待池中的worker进程执行结束再关闭pool,而terminate()则是直接关闭。
#####   补充说明
+   apply是阻塞形式的，首先住县城开始执行，碰到子进程，操作系统切换到子进程，然后等待子进程执行完毕之后再进程下一个，一直等到所有的程序都执行完毕最后切换到主进程，运行剩余的部分
+   apply_async是异步非阻塞的：首先进行开始运行，碰到子进程之后，主进程可能会说 让我执行个够。。。。。。所以需要使用join，要不直接都释放了。再这个API中，有callback选项，未回调函数，在执行完了子进程之后，调用一个回调函数，再执行其他进程，回调函数是由主进程执行的，可以用multiprocessing.getpid()打印一下就可以发现都是主进程的PID。
+   使用map(func,iterable):map方法自带close和join方法。func是进程执行的方法，iterable是把可迭代的对象一次传给函数。

#####    进程池的基本概念
+   为什么使用池：池子内什么时候装进程：并发密集型，如果启动大量的子进程的时候，可以使用进程池的方式来批量处理子进程。
    +   池子内为什么装线程：IO密集型
    +   concurrent并发---->同时发生的
    +   进程池的概念：
        +   效率问题
        +   每次开启进程，都需要开启属于这个进程的内存空间
        +   寄存器，堆栈
        +   进程过多，操作系统的调用
    +   进程池：
        +   python中的县创建一个属于进程的池子
        +   这个池子指定能存放多少线程
        +   现将这些线程创建好
+   使用进程池的好处：进程池内部文虎了一个进程序列，当使用时，在池子中获得一个可供使用的进程，程序会等待，直到池子有可用的进程为止，进程池的作用可以再多进程程序中有效的控制进程运行的个数，维护系统稳定。
####    进程之间的通信
#####   PIPE
+   正如我们在linux多线程的管道Pipe和消息队列message,queue，multiprocessing包中有pipe类和Queue类分别支持两种IPC机制.
+   Pipe:可以单工通信模式（half-duplex），也可以是双工(duplex)。我们可以通过Pipe(duplex=False)来定义单向的管道，一个进程从PIPE一端输入对象，然后PIPE另一端的进程接收，而双工允许从两端输入。
    +   Pipe对象建立的时候，返回一个含有两个元素的表，每个元素代表PIPE的一端。我们对Pipe的某一端调用send()方法来传送对象，在另一端使用recv()来接收。
#####   QUEUE
+   queue与pipe类似，都是先进先出的结构，但Queue允许多个进程放入，多个进程从队列去除，Queue使用multiprocessing.Queue(maxsize)创建，maxsize指的是存放的最大对象的数量。
    +   调用Queue.put("")的时候，将把数据入队，Queue.get()出队，FIFO。是一个队列数据结构。
#####   共享内存
+   在进程多进程并发时候，尽量避免共享状态。库提供了两种方法：
    +   Array
    +   Value
+   可以使用这2个API将数据存储在一个共享的内存映射之中，在初始化的时候创建Value\Array两个对象，设置他们的对象i , d , f等等，挺简单的，但是要防止进程抢占篡改内存数据对象。
#####   Manager
+   Manager是通过共享进程的方式共享数据。共享的数据类型有Value，Array,list,Lock,Semaphore,同时Manager还可以共享类的实例对象。
[参考资料](https://blog.csdn.net/ctwy291314/article/details/89358144)
