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
    number += 2 

def factorial(n):
    result = n
    start = n
    n -= 1
    while n > 0:  # while loop should execute as long as n is greater than 0
        result *= n  # Multiply the current result by the current value of n
        n -= 1  
    return result

print(factorial(3)) 
print(factorial(9)) 
print(factorial(1)) 

def sequence(low, high):
    # Outer loop runs twice
    for x in range(2): 
        # Inner loop counts from high down to low
        for y in range(high, low-1, -1): 
            if y == low:
                # Don’t print a comma after the last item
                print(str(y)) 
            else:
                print(str(y), end=", ") 
sequence(1, 3)


def countdown(start):
    x = start
    if x > 0:
        return_string = "Counting down to 0: "
        while x >= 0:  
            return_string += str(x)  # Add the numbers to the "return_string"
            if x > 0:
                return_string += ","
            x -= 1  # Decrement the variable
    else:
        return_string = "Cannot count down to 0"
    return return_string

print(countdown(10))
print(countdown(2))
print(countdown(0))


def odd_numbers(maximum):
    return_string = ""  # initializes variable as a string
    
    # loops through odd numbers up to maximum
    for num in range(1, maximum + 1, 2):

        # appends the odd number and a space
        return_string += str(num) + " "

    # removes the final space
    return return_string.strip()

print(odd_numbers(6))  
print(odd_numbers(10))  
print(odd_numbers(1))  
print(odd_numbers(3))  
print(odd_numbers(0))   

