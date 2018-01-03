users = ['wenergou', 'dashima', 'pdd', 'xiaoxiao', 'xika', 'admin']

for user in users:
	if user == 'admin':
		print("Hello admin, would you like to see a status report ?")
	else:
		print("hello "+ user.title() + "thank you for logging in again")


users = []

#if 'wenzhi' not in users:
#	print("wenzhi not in users!")
if users:
	print("")
else:
	print("we need to find some users")


current_name =  ['wenergou', 'dashima', 'pdd', 'xiaoxiao', 'xika']

new_name = ['Wenergou', 'haha', 'miaomao', 'Xiaoxiao', 'jnno']

# for name in new_name:
# 	for current_name1 in current_name:
# 		if name.lower() == current_name1.lower():
# 			print("you need input a new name ")
# 			break
# 	print("this name was not be used")

for name in new_name:
	if name.lower() not in current_name :
		print("this name was not be used")

	else:
		print("you need input a new name")