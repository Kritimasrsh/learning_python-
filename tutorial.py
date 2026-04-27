print (4+5)
print(9*7)
print(-1/4)
print(1/3)
print(((2050/5)+3)/2)
print (2**3)
print(2**0.5)


#Python uses indentation to indicate a block of code. The standard is to use 4 spaces for each level of indentation. For example:
if 5 > 2:
  print("Five is greater than two!")

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!")

#python variables
x = 5
y = "Hello, World!"
print(x)
print(y)

#python many statements
print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!")

# We can use semicolon to separate multiple statements on the same line:
print("Hello World!"); print("Have a good day."); print("Learning Python is fun!")

#Print without a new line
print("Hello World!", end=" ")
print("Have a good day.", end=" ")
print("Learning Python is fun!")

#Python mix texts and numbers
age = 25
print("I am " + str(age) + " years old.")
#Python can also print multiple items separated by commas, which automatically adds a space between them:       
print("I am", 35, "years old.")

"""
This is a comment
written in
more than just one line
"""

""" This is also a comment
written in more than just one line
"""


name = "Marjery"
home_address = "1234 Mockingbird Lane"
print(name + " lives at her home address of " + home_address)