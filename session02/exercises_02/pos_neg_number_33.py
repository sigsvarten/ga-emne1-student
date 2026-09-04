#positive , negative elle null tall

this_number = int(input('This number is: '))
rest_number = this_number % 2

if this_number > 0 and rest_number == 0:
    print('Positive number and even number')

elif this_number > 0 and rest_number != 0:
    print('Positive number and odd number')

elif this_number < 0 and rest_number == 0:
    print('Negative number and even number')

elif this_number < 0 and rest_number != 0:
    print('Negative number and odd number')

else:
    print('The number is 0')