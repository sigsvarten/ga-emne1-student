# Analysere ein tallverdi, oppgave 1.3
while True:
    try:
        first_number = input('Tap in your number here: ')
        last_number = input('Tap in the last number: ')

        first_number = int(first_number)
        last_number = int(last_number)

        if first_number > last_number:
            print('Wrong. The first number cannot be bigger than the last. '
              'Please try again')
            continue
        break
    except ValueError:
            print('Wrong! You must try again')

for counter in range (first_number, last_number):
    if counter % 2 == 0:
            print(f'{counter} is even number')
    if counter % 3 == 0:
        print(f'{counter} is divisible with 3')

total_sum = 0
for c in range(first_number, last_number):
        total_sum += c

print(f'The sum of all numbers: {total_sum}')

















