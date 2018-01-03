number = list( range(1, 6) )

print(number)


for value in range(5, 9) :
	print(str(value) +"\n")


for value in range(1,10, 2):
	print(value)



squares = []

for square in range(1, 11):
	#square = square ** 2
	squares.append(square ** 2)

print(squares)


digits = []

for value in range(1,11):
	digits.append(value)


minnumber  = min(digits)

print(minnumber)

maxnumber = max(digits)

print(maxnumber)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
numbers =[value ** 2 for  value in range(1, 11)] 

print(numbers)