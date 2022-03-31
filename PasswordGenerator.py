#importing the random features

import random

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

lower_case = "abcdefghijklmnopqrstuvwxyz"

digits = "0123456789"

symbols = "@#$_&-+()/*:;!?,.~`|•√π÷×¶∆£¢€¥^°={}\][✓™®©%"

string = upper_case + lower_case + digits + symbols

#length depends upon the person. Although we can increase/decrease the length of the password

length = 25

#Here .join function is used to join the random function with string and length.

password ="".join(random.sample(string, length))

#Finally we can print the password

print ("Your Passwords are: " + password )
