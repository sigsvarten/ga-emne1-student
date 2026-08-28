#Tester user input

name = input( 'What is your name? ')
course = 'python 1'

#f-string inkluderer variabler i tekst på ein ryddig måte
print( f'Hey, {name}!')
print( f'Welcome to {course}!')
#print(name)

#f-string alternativ:
#Printing komma seperasjon ting
print('Print', 'these','4', 'values')

#bokstaven f står framfor teksten
#Variabelnamn skrivast mellom krøllparanteser
# kan også bruke komma-separate veerdierr. Men den den andre metoden gir mest
# elegant oppsett

#input() gir alltid tekst
#konverter før du regner
age  = int(input('How old are you? '))

next_year = age + 1

print ((f'Next year I will be {next_year}'))