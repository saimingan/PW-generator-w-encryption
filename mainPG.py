import string
import random


#random.shuffle(characters) <== dont forget to insert this back, taken from under print("Characters total count is greater...etc") line 22

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():

    length = int(input("Enter password length: "))

    alphabets_count = int(input("Enter alphabets count in password: "))
    digits_count = int(input("Enter digits count in password: "))
    special_characters_count = int(input("Enter special characters count in password: "))

    characters_count = alphabets_count + digits_count + special_characters_count

    if characters_count > length:
        print("Characters total count is greater than the password length")
        return


    password = []

    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    for i in range (digits_count):
        password.append(random.choice(digits))

    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))


    random.shuffle(password)

    print("".join(password))



generate_random_password()

ser_input = input('Do you want to encrypt the password? (yes/no): ')

if user_input.lower() == 'yes' :
    print('user typed yes') #Replace this linewith encrypt function
    
   
    
elif user_input.lower() == 'no' :
    print('User declined')
else:
    print('Type yes or no')

#TODO
#Ask user do you want to encrypt the passcode
#If yes then encrypt the string output
#If no then do nothing