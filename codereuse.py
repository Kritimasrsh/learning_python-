name = "Kritima"                    
number = len(name) * 7               # Find the length of the name and multiply it by 7 to get the lucky number
print("Hello " + name + ". Your lucky number is " + str(number))# Print a greeting message with the name and the lucky number(number is converted to string)
name = "levi"                       
number = len(name) * 7               # Calculate the lucky number again using the new name
print("Hello " + name + ". Your lucky number is " + str(number))  


def lucky_number(name):            
    number = len(name) * 9          # Calculate the lucky number by finding the length of the name and multiplying it by 9
    print("Hello " + name + ". Your lucky number is " + str(number))  # Print a greeting message with the person's name and lucky number
lucky_number("Kay")                 # Call the function and pass the name "Kay"
lucky_number("Cameron")             # Call the function again with the name "Cameron"