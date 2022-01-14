from ntpath import join
import random

alphabet = "abcdefghijklmnpqrstuvwxyz"
numbers = "1234567890"
symbol = "@$&!^"

all = alphabet + numbers + symbol

length = int(input("Enter the length of password : "))
 
password = "".join(random.sample(all, length))

print("Your password is : " + password)