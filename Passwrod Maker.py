import random

passrn = int(input("Enter the length of password that you need :"))
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*_-:;?+<>"

p = "".join(random.sample(s, passrn))
print("Your Password:",p)
