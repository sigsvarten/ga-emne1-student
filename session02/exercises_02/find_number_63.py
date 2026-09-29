#Finne tall
sum = 0
for n in range (1, 101):
    if n % 3 == 0 and n > 20 and n < 80:
        print(f'{n} oppyfyller krava')
        sum += 1

print(sum)
