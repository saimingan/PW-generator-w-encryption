user_input = input('Do you want to encrypt the password? (yes/no): ')

if user_input.lower() == 'yes', 'y':
    print('user typed yes')
    
    #Add function to encrypt after this line ^^^
    
elif user_input.lower() == 'no', 'n':
    print('User declined')
else:
    print('Type yes or no')
