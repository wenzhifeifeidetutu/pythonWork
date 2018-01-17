## python 中fock实现多线程


# import os 
#fock 调用一次返回两次， 在当前进程中复制一份子进程
#父进程中返回的是子进程的id 子进程中永远返回0

# if __name__ == '__main__':
# 	print("current Process is "+ str(os.getpid()))
	
# 	pid = os.fork()

# 	if pid < 0:
# 		print("error in fork")
# 	elif pid == 0:
# 		print("I am child Process "+ str(os.getpid()) + " my parrent Process is "+ str( os.getppid()) )

# 	else:
# 		print("I "+str(os.getpid())+ " created a child process" + str(pid))



# import os

# from multiprocessing import Process

# #子进程要执行的代码 创建子进程时候需要传入一个执行函数和函数的参数
#start 启动进程，join（）方法实现进程的同步

# def run_proc(name):
# 	print("child process "+ str(name) +str(os.getpid())+"Running" )

# 	if __name__ == '__main__':
# 		print("parrent process "+ str(os.getpid()))
# 		for i in range(5):
# 			p = Process(target = run_proc, args=(str(i),))
# 			print("Process will start")
# 			p.start()
# 		p.join()
# 		print("Process end!")	


# 进程池的应用
#pool中不满就可以使用，如果进程满了则请求等待

from multiprocessing import Pool
import os, time, random

def run_task(name):
	print("Task "+ str(name) + "(pid = " +str(os.getpid()) + ")is running...")
	time.sleep(random.random()*3)

	print("Task "+ str(name) + " end")


if __name__ == '__main__':
	print("current process is "+ str(os.getpid()))
	p = Pool(processes = 3)
	for i in range(5):
		#apply_async同步执行进程，允许多个进程同时进入池子，apply这是等待进程结束之后才进入池子
		p.apply_async(run_task, args =(str(i), ))
	print("Waiting for all subProcesses done....")
	p.close()
	p.join()
	print("All subProcesses done")	
