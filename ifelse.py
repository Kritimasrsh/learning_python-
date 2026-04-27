def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    else:
        print("Username is valid.")

#not using else 
def is_even(number):
    if number % 2 == 0:
        return True
    return False

age = 20
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#elif - else if used when there are multiple conditions to check
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long.")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long.")
    else:
        print("Username is valid.")

