import random

characters = input("Enter Anything In Your Mind - ")
length = int(input("Enter The Length Of Password - "))
password = ' '
for p in range(length) :
    password += random.choice(characters)
print(password)

password_in_text = open("password.txt" , "a")
password_in_text.write(password)
password_in_text.close()

if length >= 12 :
    print("Your Generated Password Is Strong!")
else :
    print("Your Generated Password Is Weak!")