# finne kvadrattall while

square_number = int(input('The number is: '))

for i in range(1, square_number +1):
    sum_round = i * i
    if sum_round < square_number:
        print(f'The sqaure number of {sum_round} is less than {square_number}')