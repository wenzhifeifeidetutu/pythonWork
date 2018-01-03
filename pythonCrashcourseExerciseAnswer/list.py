bicycle = ["trek", "cannondale", "redline", "specialized", 12]

print (bicycle)

index = 0

print(bicycle[index].title())

index = -1 

print(str(bicycle[index]).title())

index = -2

print(bicycle[index])


motorcycle = ['haojue', 'bmw', 'tt', '6666']

print(motorcycle)


motorcycle[0] = 'juejue'

print(motorcycle)

motorcycle.append('jijiji')

print(motorcycle)

motorcycle.insert(0, 'haohao')

print(motorcycle)

motorcycle.insert(-2, 'haohaowei')

print(motorcycle)

del motorcycle[-1]

print(motorcycle)


poped_motorcycle = motorcycle.pop(2)

print(poped_motorcycle)

print(motorcycle)

motorcycle.remove('tt')

print(motorcycle)
