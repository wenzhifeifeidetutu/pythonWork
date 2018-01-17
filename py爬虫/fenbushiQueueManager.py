#分布式进程
#linux 版本

import random, time, Queue
from multiprocessing.managers import BaseManager

#第一步 建立task_queue 和result_queue, 用来存放任务和后果

task_queue = Queue.Queue()
result_queue = Queue.Queue()

class  Queuemanager(BaseManager):
	pass

#第二步把创建的两个队列注册在网络上， 利用register方法,
#callable参数关联了Queue对象
#将Queue对象在网络中暴露

Queuemanager.register('get_task_queue', callable = lambda:task_queue)
Queuemanager.register('get_result_queue', callable = lambda:result_queue)


#第三步：绑定8001，设置验证口令'right'相当于对象的初始化

manager = Queuemanager(address=('', 8001), authkey='right')

#第四步启动管理， 监听信息通道

manager.start()
