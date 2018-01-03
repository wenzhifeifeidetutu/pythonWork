#!/usr/bin/python
# file_name = 'learing_python.txt'
file_name = 'books.txt'
try:
	with open(file_name) as file_obeject:
		content = file_obeject.read()

except FileNotFoundError:
	print(file_name+ " not Found!")

else:
	words = content.split()
	words_number = len(words)

	print("The artical belongs words is  "+ str(words_number) )
