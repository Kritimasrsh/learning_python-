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

def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize // block_size
    partial_block_remainder = filesize % block_size
    
    if partial_block_remainder > 0:
        return (full_blocks + 1) * block_size
    return full_blocks * block_size

print(calculate_storage(1))    
print(calculate_storage(4096))
print(calculate_storage(4097)) 
print(calculate_storage(6000)) 