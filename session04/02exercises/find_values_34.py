#finne bestemte verdier

numbers = [32, 60, 39, 47, 87, 65, 90, 50, 147]

counter = 0
for n in numbers:
    if n > 50:
        counter += 1
        print(n)

print(f'The sum numbers over 50: {counter}')


