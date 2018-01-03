while True:
	print("The movie tigats")
	number = input("what's you age is ")

	if number.lower() == "quit":
		break
	elif int(number) < 3:
		print("you are free!")
	elif int(number) < 12:
		print("you are $10!")
	elif int(number) >= 12:
		print("you are $15")

		