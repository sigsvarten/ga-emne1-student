# ber om et gyldig nummer

positive_number = int(input('What is the number? '))

while positive_number < 1:
        new_number = int (input('What is the number this time? '))

        if new_number >= 1:
            print (f'Vaild number is {new_number}')
        elif new_number >= 1:
            print(f'The valid number is: {new_number}')
        else:
            print('Not valid')

print(f'Valid number is {positive_number}')




