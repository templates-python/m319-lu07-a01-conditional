def larger():
    num1 = int(input("Please enter an integer:\n"))
    num2 = int(input("Please enter an integer:\n"))

    # TODO: Please print the bigger number, only use one ternary-operator to do so


def boolean():
    value = True

    # problem:
    print(value)  # 'True' and 'False' will be printed instead of 'Wahr' and 'Falsch'

    # With if-else-statement
    if value:
        print('Wahr')
    else:
        print('Falsch')

    # TODO: Please print the boolean-value in german, only use one ternary-operator to do so


def modulo():
    x = int(input("Please enter an integer:\n"))

    # TODO: replace the if..else with a ternary-operator
    if x % 2 == 0:
        int_type = 'even'
    else:
        int_type = 'odd'

    print(f'You entered {x} which is an {int_type} integer.')


def nested():
    number = int(input('Enter number between -100 and +200'))

    # TODO: replace the if..else(if..else) with a ternary-operator
    if (number < 0):
        print('Less than zero')
    else:
        if number >= 0 and number <= 100:
            print('Between 0 and 100')
        else:
            print('Greater than 100')


if __name__ == '__main__':
    larger()
    boolean()
    modulo()
    nested()
