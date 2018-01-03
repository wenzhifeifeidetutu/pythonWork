sandwich_order = ['seafood', 'beef', 'patato', ]

finished_sandwich = []

while sandwich_order:
	current_sandwish = sandwich_order.pop()
	finished_sandwich.append(current_sandwish)
	print("I made your " + current_sandwish +  " sandwich !")

for sandwich in finished_sandwich:
	print(sandwich)

sandwich_order = ['seafood', 'beef', 'patato', 'pastrami', 'pastrami', 'pastrami']

print("The all pastrami was seled ovre")

while 'pastrami' in sandwich_order:
	sandwich_order.remove('pastrami')

print(sandwich_order)

while sandwich_order:
	current_sandwish = sandwich_order.pop()
	finished_sandwich.append(current_sandwish)
	print("I made your " + current_sandwish +  " sandwich !")

for sandwich in finished_sandwich:
	print(sandwich)
