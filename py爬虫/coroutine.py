#coroutine 协程

from gevent import monkey;monkey.patch_all()

import gevent
import urllib.request
from gevent.pool import Pool


##使用urllib.request 在python3中 

def run_task(url):
	print('Visit -->{0}'.format(url))
	try:
		request = urllib.request.Request(url)
		response = urllib.request.urlopen(request)
		data = response.read()
		print('{0} bytes received from {1}.'.format(len(data), url))

	except Exception as e:
		print(e)

	return 'url:{0} ----> finish'.format(url)


if __name__ == '__main__':
	pool = Pool(1)
	urls = ['http://www.baidu.com', 'http://wenergou.top', 'http://www.baidu.com']
	# greenlets = [gevent.spawn(run_task, url) for url in urls ]
	# gevent.joinall(greenlets)	
	result = pool.map(run_task, urls)

	print(result)