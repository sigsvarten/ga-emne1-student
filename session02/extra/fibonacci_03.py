# finne fibonacci tall

number_limit = int(input('The limit number is: '))
last:int = 0
previous: int = 1

for i in range(number_limit):
    print (last)
    last,previous = previous, last + previous

print()

while last<= number_limit:
    print(last)
    last, previous = previous, last + previous