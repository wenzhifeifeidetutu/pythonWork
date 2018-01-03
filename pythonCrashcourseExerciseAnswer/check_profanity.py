#import urllib.request
import urllib

def read_text () :
	quotes = open("/Users/wenzhi/Documents/test.txt")
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	#text_to_check = "shit"
	# in python2
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+(text_to_check))
	# in python 3 use this!
	#with urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+urllib.parse.quote(text_to_check)) as connection:
	#	output = connection.read()
	#connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	print(output)
	connection.close()


read_text()	