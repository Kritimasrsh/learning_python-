#Slicing means getting a part (subset) of a string, list, or tuple.
#Syntax: variable[start:stop:step]

string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings” 
print(string1[:5])  # Prints “Greet”

# Prints “Earthlings” again
print(string1[-10:])

print(string1[0::2])
print(string1[::-1]) #negative stride prints string backwards


print("Hello" + " " + "world")

greetings = ["Hello", "world"]
print(" ".join(greetings)) 
name = "Kritima"
print("Hello, " + name + "!")

phonenum = '9874562147'
# The first 3 digits are the area code:
area_code = "(" + phonenum[:3] + ")"

exchange = phonenum[3:6]
line = phonenum[-4:]
area_code + " " + exchange + "-" + line


def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line
format_phone('9856478595')