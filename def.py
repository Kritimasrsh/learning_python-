def task_reminder(time_as_string):
    if time_as_string == "8:00 a.m.": 
        task = "Check overnight backup images"
    elif time_as_string == "11:30 a.m.":
        task = "Run TPS report"
    elif time_as_string == "5:30 p.m.":
        task = "Reboot servers"
    else:
        task = "Provide IT Support to employees" 
    return task
print(task_reminder("10:00 a.m.")) 



# Example 1
# Evaluate the output of this print statement
def product(a, b):
    return(a*b)
print(product(product(2,4), product(3,5)))


# Example 2 
# Evaluate the output of this print statement
def difference(a, b):
    return(a-b)
def sum(a, b):
    return(a+b)
print(difference(sum(2,2), sum(3,3)))


# Example 3
# Evaluate the Boolean output of this comparison
print((5 >= 2*4) and (5 <= 4*3))

# Example 4 
# Evaluate the value of the comparison in the if statement 
x = 3
if x+5 > x**2 or x % 4 != 0:
    print("This comparison is True")

# Example 5 
# Evaluate the output of this if-elif-else statement
number = 6
if number * 2 < 14:
    print(number * 6 % 3)
elif number > 7:
    print(100 / number)
else:
    print(7 - number)


def get_remainder(x, y):
  if x == 0 or y == 0 or x ==y:
    remainder = 0
  else:
    remainder = (x % y) / y
  return remainder
print(get_remainder(10, 3))



def speeding_ticket(speed):
    if speed > 85:
        ticket = "Reckless Driving"
    elif speed > 65:
        ticket = "Speeding"
    else:
        ticket = "Safe"
    return ticket
print(speeding_ticket(87)) #  print Reckless Driving
print(speeding_ticket(66)) #  print Speeding
print(speeding_ticket(65)) #  print Safe
print(speeding_ticket(85)) #  print Reckless Driving
print(speeding_ticket(35)) #  print Safe
print(speeding_ticket(77)) #  print Speeding


def letter_translator(letter):
    if letter == "a":
        letter_position = 1
    elif letter == "b":
        letter_position = 2
    elif letter == "c":
        letter_position = 3
    elif letter == "d":
        letter_position = 4
    else:
        letter_position = "unknown"
    return letter_position
print(letter_translator("a")) #  prints 1
print(letter_translator("b")) #  prints 2
print(letter_translator("c")) #  prints 3
print(letter_translator("d")) #  prints 4 
print(letter_translator("e")) # Prints unknown
print(letter_translator("A")) # Prints unknown
print(letter_translator("")) #  Prints unknown


def safe_division(numerator, denominator):
    
    if denominator == 0:
        result = 0
    else:
        result = numerator/denominator
    return result

print(safe_division(5, 5)) #  print 1.0
print(safe_division(5, 4)) #  print 1.25
print(safe_division(5, 0)) #  print 0
print(safe_division(0, 5)) #  print 0.0


def exam_grade(score):
    if score == 100:
        grade = "Top Score"
    elif score >= 60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade
print(exam_grade(65)) #  print Pass
print(exam_grade(55)) #  print Fail
print(exam_grade(60)) #  print Pass
print(exam_grade(95)) #  print Pass
print(exam_grade(100)) # print Top Score
print(exam_grade(0)) #  print Fail


def complementary_color(color):
    if color == "blue":
        complement = "orange"
    elif color == "yellow":
        complement = "purple"
    elif color == "red":
        complement = "green"
    else:
        complement = "unknown"
    return complement

print(complementary_color("blue")) #  print orange
print(complementary_color("yellow")) #  print purple
print(complementary_color("red")) #  print green
print(complementary_color("black")) #  print unknown
print(complementary_color("Blue")) #  print unknown
print(complementary_color("")) #  print unknown


def return_nonnegative(first_num, second_num):
    if first_num > second_num:
        result = first_num - second_num
    else:
        result = second_num - first_num
    return result
print(return_nonnegative(5, 5)) #  print 0
print(return_nonnegative(4, 5)) #  print 1
print(return_nonnegative(5, 3)) #  print 2
print(return_nonnegative(2, 5)) #  print 3
print(return_nonnegative(5, 0)) #  print 5
print(return_nonnegative(0, 5)) #  print 5


def clothing_type(temp):
    if temp >= 70:
        clothing = "T-Shirt"
    elif temp >= 55:
        clothing = "Sweatshirt"
    elif temp >= 45:
        clothing = "Jacket"
    else:
        clothing = "Heavy Coat"
    return clothing
print(clothing_type(72))  # T-Shirt
print(clothing_type(55))  # Sweatshirt
print(clothing_type(65))  # Sweatshirt
print(clothing_type(50))  # Jacket
print(clothing_type(45))  # Jacket
print(clothing_type(32))  # Heavy Coat
print(clothing_type(0))   # Heavy Coat


def complementary_color(color):
    if color == "blue":
        complement = "orange"
    elif color == "yellow":
        complement = "purple"
    elif color == "red":
        complement = "green"
    else:
        complement = "unknown"
    return complement
print(complementary_color("blue"))   # orange
print(complementary_color("yellow")) # purple
print(complementary_color("red"))    # green
print(complementary_color("black"))  # unknown
print(complementary_color("Blue"))   # unknown
print(complementary_color(""))       # unknown



def make_positive(number):
    if number < 0:
        result = number * -1 
    else:
        result = number
    return result
print(make_positive(-4))   # 4
print(make_positive(0))    # 0
print(make_positive(-.25)) # 0.25
print(make_positive(5))    # 5


def round_up(number):
  x = 10
  whole_number = number // x
  remainder = number % x
  if remainder >= 5:
    return x * (whole_number + 1)
  return x * whole_number
print(round_up(35))