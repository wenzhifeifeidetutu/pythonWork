items = ['111', '222', '333', '444', '555']

print(items)


print("The first three items in the list are " )

for item  in items[:3]:
	print(item)


print("Three items from the middle of the list are")

for item in items[1:4]:
	print(item)

print("The last tree items in the list are")

for item in items[-3:]:
	print(item)


my_pizzas = ['fruit_pizza', 'beef_pizza', 'seafood_pizza']

friend_pizzas = my_pizzas[:]

my_pizzas.append('666_pizza')

friend_pizzas.insert(0, '777_pizza')

print("my favoriate pizza are ")

for my_pizza in my_pizzas:
	print(my_pizza)

print("my friend pizza are ")

for my_friend_pizza in friend_pizzas:
	print(my_friend_pizza)