'''Kyle'''


def main():
    password = get_password()

    print('*' * len(password))


def get_password():
    password = str(input('Password: '))
    while len(password) < 5 or len(password) > 15:
        print('Invalid password')
        password = str(input('Password: '))
    return password


main()