import random
import string

print('Welcome to password generator!')

length = int(input('\nEnter the length of the password :'))

upper = string.ascii_uppercase
lower = string.ascii_lowercase
num = string.digits
spl = string.punctuation

all = upper+lower+num+spl

temp = random.sample(all,length)

password = "".join(temp)

print(password)
