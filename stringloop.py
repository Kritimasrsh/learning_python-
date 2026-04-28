greeting = 'Hello'
for char in greeting:
	print(char)

for i in range(len(greeting)):
	print(i)
	
greeting = 'Hello'
index = 0
while index < len(greeting):
	print(greeting[index])
	index += 1
	
greeting = 'Hello'
index = 0
while index < len(greeting):
	print(greeting[index:index+1])
	index += 1
	
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)