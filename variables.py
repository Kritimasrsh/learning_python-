#Variables are containers for storing data values. In Python, we do not need to declare the type of variable, it is determined automatically based on the value assigned to it.
""" Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)"""


x = 5
y = "Hello, World!"
print(x)
print(y)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       
x = "Sudeep" 
print

#Casting is used to specify a variable type. In Python, we can use the following functions to cast data types:
x = int(3)   
y = float(3) 
z = str(3)   
print(x)
print(y)
print(z)

#get the type of a variable
x = 5
y = "Hello, World!"
print(type(x))
print(type(y))


a = "Hello"
b = 'Hello'
print(a)
print(b)

#Case-sensitive variables
a = 4
A = "Sudeep"
print(a)
print(A)

#Variable names can contain letters, numbers, and underscores, but cannot start with a number. For example:
my_variable = 10
myVariable = 20
my_variable2 = 30
print(my_variable)
print(myVariable)
print(my_variable2)

myvar = "Kritima"
my_var = "Kritima"
_my_var = "Sudeep"
myVar = "Levi"
MYVAR = "Mikasa"
myvar2 = "Hange"

#Multiwords variable names can be written in several ways:
#Camel Case: Each word, except the first, starts with a capital letter. Example:
myVariableName = "Sudeep"
#Pascal Case: Each word starts with a capital letter. Example:
MyVariableName = "Levi"
#Snake Case: Each word is separated by an underscore character. Example:
my_variable_name = "Kritima"


#Many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One value to multiple variables
x = y = z = "Grapes"
print(x)
print(y)
print(z)

#Unpack a collection
fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Python output variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


x = "Python"
y = "is"        
z = "awesome"
print(x + y +  z) 

#python global variables
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()


x = 10   # global variable
def show():
    print(x)
show()
print(x)

#Modifying a global variable inside a function
x = 10   # global variable
def show():
    global x
    x = 20  # modifying the global variable
    print(x)
show()
print(x)

#creating a global variable inside a function
def show():
    global x
    x = 30  # creating a global variable
    print(x)
show()
print(x)

#2
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)