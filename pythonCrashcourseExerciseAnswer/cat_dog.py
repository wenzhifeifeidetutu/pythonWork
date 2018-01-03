try:
	with open('cats.txt') as file_object:
		content = file_object.read()
		print(content)
	with open('dogs.txt') as file_object:
		content = file_object.read()
		print(content)

except FileNotFoundError:
	# print("not fond!")
	pass
else:
	print("Found!")