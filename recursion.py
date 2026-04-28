def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        return number == 1
    # Recursive case
    return is_power_of(number/base, base)
print(is_power_of(8,2))    
print(is_power_of(64,4))    
print(is_power_of(70,10))   



# Sample group data and helper functions for the recursive count.
groups = {
    "sales": ["eric", "michael", "tom"],
    "design": ["derek", "john", "maria"],
    "engineering": ["sam", "paul", "robert", "joan", "chris", "design"],
    "hr": ["harry", "sally", "kate", "james", "ida", "lou"],
    "everyone": ["sales", "engineering", "hr", "ceo"],
}

def get_members(group):
    return groups.get(group, [])

def is_group(member):
    return member in groups

def count_users(group):
  count = 0
  for member in get_members(group):
    if is_group(member):
      count += count_users(member)
    else:
      count += 1
  return count
print(count_users("sales"))        
print(count_users("engineering"))  
print(count_users("everyone"))     




def sum_positive_numbers(n):
    if n < 1:
        return 0
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) 
print(sum_positive_numbers(5)) 