# finne fibonacci tall

number_limit = int(input('The limit number is: '))
last:int = 0
previous: int = 1
next: int = 1

if number_limit > 0:
    print(last)
if number_limit >= 1:
    print(previous)

    while next <= 1:
        print (next)
    last = previous
    previous = next
    next = last + previous