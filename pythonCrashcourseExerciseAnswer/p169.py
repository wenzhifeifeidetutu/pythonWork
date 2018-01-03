filename = 'learing_python.txt'

with open(filename) as file_object:
	# content = file_object.read()
	lines = file_object.readlines()
	#print(content)
	


line_number = 0
for line in lines:
	print(line.replace('python', 'Java').rstrip() +" "+ str(line_number) )
	line_number += 1