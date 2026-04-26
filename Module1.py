
#Write a Python script that outputs "Automating with Python is fun!" to the screen.
#Remember that syntax precision is important in programming languages.
#A missing capital letter, spelling error, or punctuation mark can produce errors.

print("Automating with Python is fun!")

# What should be the output of the expression below? 
print(12/(1+2)+2**2) #8.0

# Assuming there are 60 minutes in an hour, write a program that calculates the number of minutes in a 24 hour day.
#Print the result on the screen. Note: Your result should be in the format of just a number, not a sentence.

print(60 * 24)

#In a passcode where each digit of the passcode is independent of the other digits and each digit can be any numeral from 0 through 9,
#the total number of combinations is the number of possibilities for each digit raised to the power of the length of the passcode. 
#So, for a 1-numeral passcode, there would be 10 possibilities; one for every numeral from 0 to 9.  
#For a 2-numeral passcode, each numeral is independent of the other, so there would be 10 times 10 possibilities. 

print(10**2) #100
print(10**3) #1000
print(10**4) #10000

# Fill in the blank to calculate how many sectors a given 16 GB (gigabyte) hard disk drive has.
# The given hard drive is divided into sectors of 512 bytes each. Divide the total bytes on the drive by the number of bytes in a sector 
# to calculate how many sectors this drive has.  Your result should be a number. Note: To calculate the total bytes on the disk drive,
#  multiply by multiples of 1024. In the code below,  you can calculate the "disk_size" of 16 GB by multiplying 16 by 1024 three times
#  to go from bytes, to kilobytes, to megabytes, and finally to gigabytes.

disk_size = 16 * 1024 * 1024 * 1024 #16 GB in bytes
sector_size = 512 #bytes    
sector_amount = disk_size / sector_size
print(sector_amount) #33554432.0