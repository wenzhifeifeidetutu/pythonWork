
names = []
while True:

	name = input("input your name please ! q to quit")
	if name == 'q':
		break
	names.append(name)

with open('name.txt', 'a') as file_object:
		for name in names:
			file_object.write(name+"\n")

with open('name.txt') as file_object:
	content = file_object.read()
	print(content)
