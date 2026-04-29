#A for loop is used to repeat a block of code a fixed number of times
#count-based loop 

for x in range(5):
    print(x)

friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

values = [ 23, 52, 59, 37, 48 ] 
sum = 0 
length = 0 
for value in values: #Take each number from the list one by one
    sum += value #add current number to sum : 0+23 23+52=75 75+59=134 134+37=171 171+48=219
    length += 1 #increase length by 1 

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))


product = 1
for n in range(1,10): #1-9
  product = product * n #1*1=1 1*2=2 2*3=6 6*4=24 ... 40320*9=362880
print(product)


def to_celsius(x):
  return (x-32)*5/9
for x in range(0,101,10):
  print(x, to_celsius(x))


for n in range(1, 5, 6):  
    print(n)


for n in range(0,11,2):
    print(n)


for x in range(2, -2, -1):
    print(x)

for x in range(5, -1, -1): #start at 5, stop before -1, decreases by 1 each step 
    print(x)

for number in range(1, 6+1, 2):
    print(number * 3)

for n in range(6,18+1,3): # range becomes 6, 9, 12, 15, 18
  print(n*2)



for number in range(2,8):
    print(number**2)