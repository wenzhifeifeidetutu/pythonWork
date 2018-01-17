#python 多线程

# import random
# import time, threading

# #新线程执行的代码

# def thread_run(urls):
# 	print('Current {0} is running'.format(threading.current_thread().name))
# 	for url in urls:
# 		print('{0} --->{1}'.format(threading.current_thread().name, url))
# 		time.sleep(random.random())
# 	print('{0} ended.'.format(threading.current_thread().name))



# print('{0} is running'.format(threading.current_thread().name))

# t1 = threading.Thread(target = thread_run, name='Thread_1', args=(['url_1','url_2','url_3' ], ))
# t2 = threading.Thread(target = thread_run, name='Thread_2', args=(['url_4', 'url_5', 'url_6'], ))

# t1.start()
# t2.start()
# t1.join()
# t2.join()

# print('{0} ended'.format(threading.current_thread().name))


## 进程同步
import threading
mylock = threading.RLock()
num = 0

class myThread(threading.Thread):
	"""docstring for myThread"""
	def __init__(self, name):
		#threading.Thread.__init__(self, name = name)
		super().__init__(name = name)

	def run(self):
		#python里面修改全局变量之后会变成局部变量 需要用global引用
		global num
		while True:
			mylock.acquire()
			print('{0} locked, Number:{1}'.format(threading.current_thread().name, num))
			if num>=4:
				mylock.release()
				print('{0} released, Number:{1}'.format(threading.current_thread().name, num))
				break
			num+=1
			print('{0} released, Number:{1}'.format(threading.current_thread().name, num))
			mylock.release()

if __name__ == '__main__':
	thread1 = myThread('Thread_1')
	thread2 = myThread('Thread_2')
	thread1.start()
	thread2.start()	
		

