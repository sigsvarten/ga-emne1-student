# Price per person

total = int (input ('What is the total price? '))
total_persons = int(input('How many persons? '))

price_per_person = total / total_persons

print( f'The price per person is: {price_per_person:.2f}')

# f'...' creates an f-string, which allows you to embed variables directly inside a string.
# {price_per_person} inserts the value of the variable price_per_person.
# :.2f formats that value as a floating-point number with 2 digits after the decimal point.
# print() displays the resulting text.

