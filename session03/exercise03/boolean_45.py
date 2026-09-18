#return boolean

def is_even():
    for n in range(1, 11):
        if n % 2 == 0:
            print(n, True)
        else:
            print(n, False)


is_even()