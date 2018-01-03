flag = 1

while flag == 1:
	number = int (input("please input a number, I will tell you it if a ten, -1 to quit") )
	if number != -1:
		if number % 10  == 0:
			print("It is ")
		else:
			print("It is not ")
	else:
		flag = 0