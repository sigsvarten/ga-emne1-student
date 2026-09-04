# potens , partall og oddetall

number = int(input ('What is the number here? '))

print (number ** 2)
print (number ** 3)

rest = number % 2
print (rest)

if rest % 2 == 0:
    print('Even number')
else:
    print('This is odd')