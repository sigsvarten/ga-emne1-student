# find pin code with three attemps

secret_pin = str ('2468')
attempts_left = int (3)
is_authenticated = False

while attempts_left > 0 and not is_authenticated:
    pin = input('Tape in pin ')
    if pin == secret_pin:
        is_authenticated = True
        print(f'Access granted')
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f'Access denied. You have {attempts_left} attemps left')
        else:
            attempts_left = 0
            print(f'Access denied')
