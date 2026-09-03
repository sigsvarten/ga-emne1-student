# guessing game

secret_number = 38
attempts = 5
guessed_correctly = False

#adding loop, then if, else

while attempts > 0 and not guessed_correctly:
    guess = int(input('Guess: (1-40) '))
    if guess == secret_number:
        print('Spot on!')
        guessed_correctly = True
    elif guess < secret_number:
        print( 'Too low!')
    else:
        print ('Too high!')
    attempts-= 1

if not guessed_correctly:
    print(f'The number was {secret_number}.')
