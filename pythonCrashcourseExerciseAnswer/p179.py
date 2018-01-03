#p179

try:
	number1 = int(input("please input first number "))
	number2 = int(input("please input second number "))
except ValueError:
	print("you should input number !")
else:
	print(str(number1 + number2) )


while True:
	try:
		number1 = int(input("please input first number "))
		number2 = int(input("please input second number "))
	except ValueError:
		print("you should input number !")
	else:
		print(str(number1 + number2) )

