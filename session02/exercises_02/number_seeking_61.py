# søker nummer i løkke

numbers = input('This number is:')

for numbers in range(1, 21):
    if numbers % 2 == 0:
        print(f'{numbers} is even number')
    else:
        print(f'{numbers} is odd number')

