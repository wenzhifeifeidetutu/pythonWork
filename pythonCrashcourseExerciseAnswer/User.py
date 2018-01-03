class User():

	def __init__(self, first_name, last_name, user_info):
		self.first_name = first_name
		self.last_name = last_name
		self.user_info = user_info
		self.name_title = self.first_name + " "+ self.last_name
		self.login_attempts = 0

		for key, value in user_info.items():
			self.user_info[key] = value


	def describe_user(self):
		name = self.first_name.title() + " " + self.last_name.title()
		print(name)
		return self.user_info

	def greet_user(self):
		print("hello "+ self.first_name+"sadas"+ self.last_name)
		print(self.name_title)

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

user = User('wen', 'zhi', {'sex' :'man'})	
print(user.describe_user())

user1 = User('wen', 'zhi', {'sex' :'man'})	
user2 = User('wen2', 'zhi2', {'sex' :'man'})	
user3 = User('wen3', 'zhi3', {'sex' :'man'})	
print(user1.describe_user())
print(user2.describe_user())
print(user3.describe_user())


user.greet_user()

print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)