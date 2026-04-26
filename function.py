def greetings(name):
    print("Welcome, " + name)
greetings("Kritima")

def greetings(name, age):
    print("Welcome, " + name + ". You are " + str(age) + " years old.")
greetings("Kritima", 25)

#Creating a function with a default parameter value
def my_function():
  print("Hello from a function")
my_function()

# Without a function = Repeated code
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

# With a function = Reusable code
def fahrenheit_to_celsius(temp):
    celsius = (temp - 32) * 5 / 9
    return celsius
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))
