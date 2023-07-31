def larger():
    num1 = int(input("Please enter an integer:\n"))
    num2 = int(input("Please enter an integer:\n"))

    print(f'{num1} is greater') if (num1 > num2) else print(f'{num2} is greater')


def boolean():
    value = True

    print('Wahr' if value else 'Falsch')


def modulo():
    x = int(input("Please enter an integer:\n"))

    int_type = 'odd' if x % 2 else 'even'

    print(f'You entered {x} which is an {int_type} integer.')


def nested():
    number = int(input('Enter number between -100 and +200'))

    print('Less than zero' if number < 0 else 'Between 0 and 100' if number >= 0 and number <= 100 else 'Greater than 100')


if __name__ == '__main__':
    larger()
    boolean()
    modulo()
    nested()
