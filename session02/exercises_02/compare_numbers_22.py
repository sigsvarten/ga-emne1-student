# sammenligne artmetiske operatorer

first_number = int(input('What is the first number? '))
second_number = int(input('What is the second number? '))

sum_number = first_number + second_number
differance = first_number - second_number
division = first_number / second_number
division2 = first_number // second_number
rest_division = first_number % second_number

print (f' Sum of the numbers {sum_number}. '
       f'The differance is {differance}. The result of division: {division:.2f}'
       f' The second division: {division2:.2f}, and the rest is {rest_division:.2f} ')

# blir feilmelding når second number er 0 fordi det går ikkje å dele på 0

