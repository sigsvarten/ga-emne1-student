#tallanalyse

def read_number():
    return int (input('Tap in a number here: '))

def describe_sign(number):
    if  number > 0:
        return 'Positive number'
    elif number < 0:
        return 'Negative number'
    else:
        return 'Zero'

def is_even(number):
    return number % 2 == 0

def show_analysis(number, sign, even):
    even = 'Even' if even else ('Odd')
    print(f'The number {number} is {sign} and {even}')

def run_number_analyzer():
    number = read_number()
    sign = describe_sign(number)
    even = is_even(number)
    show_analysis(number, sign, even)

run_number_analyzer()