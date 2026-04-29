#A while loop keeps running as long as a condition is True.
#Condition-based 

x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))

def is_power_of_two(number):
  # Run the loop only if number is greater than 0
  while number > 0 and number % 2 == 0:
    number = number / 2
  # If number becomes 1, it is a power of two
  if number == 1:
    return True
  return False
# Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False


def sum_of_integers(n):
  if n < 1:
    return 0
  i = 1
  sum = 0
  while i <= n:
    sum = sum + i
    i = i + 1
  return sum
print(sum_of_integers(3))  # should print 6
print(sum_of_integers(4))  # should print 10
print(sum_of_integers(5))  # should print 15


def multiplication_table(number):
    multiplier = 1 #Initialization

    while multiplier <= 5: 
        result = number * multiplier 
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result)) #Prints results in format.
        
        multiplier += 1

multiplication_table(3) 
multiplication_table(5) 
multiplication_table(8)


number = 2  
while number <= 12: 
    print(number, end=" ")
    number += 2  # Increment the variable by 2

  

