# billetter bestoilling


try:
    tickets = int(input('Tickets: '))
except ValueError:
    print('Please enter a whole number. ')
else:
    if tickets > 0 and tickets <= 8:
        print(f'Total is: {tickets * 120}')
    else:
        print('Wrong!')

