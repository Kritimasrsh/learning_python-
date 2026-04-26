#return sends the value back to the caller.
#return sends the result of a function back to the place
# where the function was called.
def area_traingle(base,height):
    return base*height/2
area_a = area_traingle(10,5)
area_b = area_traingle(20,10)
sum = area_a + area_b
print("The area of the triangle is: " + str(sum))

def add(a, b):
    return a + b
result = add(2, 3)
print(result)  

#What happens:-
#add(2,3) runs the function.
#a + b becomes 5.
#return 5 sends 5 back.
#result stores 5.
#print(result) shows 5.

def get_info():
    return "Kritima", 25
name, age = get_info()
print(name, age)

#Returning nothing
def print_message(message):
    print(message)
print_message("Hello, world!")

def greet():
    print("Hello")
result = greet()
print(result)  # Output: None

#Conditional return
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


def check_even(num):
    if num % 2 == 0:
        return True
    return False


def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"
print(check_number(10))  # Output: Positive
print(check_number(-5))  # Output: Negative
print(check_number(0))   # Output: Zero
print(check_even(4))  # Output: True
print(check_even(5))  # Output: False

#To convert a total number of seconds into hours, minutes, and remaining seconds.
# Define a function named convert_seconds that takes one parameter called seconds
def convert_seconds(seconds):
    # Calculate how many full hours are in the given seconds
    hours = seconds // 3600
    # Find the remaining seconds after removing the hours
    remaining_seconds = seconds % 3600
    # Calculate how many full minutes are in the remaining time
    minutes = (seconds - hours * 3600) // 60
    # Calculate the final remaining seconds after removing hours and minutes
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    # Return the calculated hours, minutes, and remaining seconds as a tuple
    return hours, minutes, remaining_seconds
# Call the function with 3665 seconds and store the returned result in variable time
time = convert_seconds(3665)
# Print the result stored in time
print(time)  # Output will be (1, 1, 5)

