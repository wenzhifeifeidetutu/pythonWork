#进程间通信 Queue 和Pipe
'''

from multiprocessing import Process, Queue
import os, time, random

#写数据仅程执行代码:

def proc_write(q, urls):
	print('Process {0} is writing'.format(os.getpid()))
	for url in urls:
		q.put(url)
		print('Put {0} to queue'.format(url))
		time.sleep(random.random())


#读数据进程执行代码

def proc_read(q):
	print('Process {0} is reading....'.format(os.getpid()))
	while True:
		
		url = q.get(True)
		print('Get {0}'.format(url))


if __name__ == '__main__':
	#父进程创建Queue，并传给各个子进程
	q = Queue()
	proc_write_1 = Process(target = proc_write, args= (q, ['url_1', 'url_2','url_3' ]))
	proc_write_2 = Process(target = proc_write, args=(q, ['url_4', 'url_5', 'url_6']))

	proc_readder = Process(target = proc_read, args = (q,))

	#启动子进程proc_writer, 写入
	proc_write_1.start()
	proc_write_2.start()

	#启动子进程proc_reader 读取
	proc_readder.start()

	#等待proc_writer结束
	proc_write_1.join()
	proc_write_2.join()

	#proc_reader进程里面是死循环，无法等待结束，强行终止
	proc_readder.terminate()
'''

import multiprocessing
import random
import time, os

def proc_send(pipe, urls):
	for url in urls:
		print('Process {0} send: {1}'.format(os.getpid(), url))
		pipe.send(url)
		time.sleep(random.random())


def proc_recv(pipe):
	while True:
		print('Process {0} rev:{1}'.format(os.getpid(), pipe.recv()))		
		time.sleep(random.random())


if __name__ == '__main__':
	pipe = multiprocessing.ipe()
	p1 = multiprocessing.Process(target = proc_send, args=(pipe[0], ['url_'+str(i) for i in range(10)]))
	p2 = multiprocessing.Process(target = proc_recv, args = (pipe[1], ))
	p1.start()
	p2.start()
	p1.join()
	p2.join()





