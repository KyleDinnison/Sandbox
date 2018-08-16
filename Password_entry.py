'''Kyle'''
password = str(input('Password: '))
while len(password) < 5 or len(password) > 15:
    print('Invalid password')
    password = str(input('Password: '))

print('*' * len(password))


