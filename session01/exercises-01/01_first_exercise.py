# 1. printer ut stringen Hey
# Output vises i terminalen
print('Hello')

# 2. lage ei helsing
first_name = 'Sigvart'
favorite_language = 'Norwegian'
second_language = 'English'

#2. Skiver ut ein setning med variabler og tekstverdier
print ('Hey ' + first_name + '. ' '' + favorite_language + ' is my language, ' + 'and ' + second_language +
       ' is my second language')

print ('Hey ' + first_name + '. ' '     ' + favorite_language + ' is my language, ' + ' ' + second_language +
      ' is my second language')
  # Om eg tar et anførselstegn lenger bort, blir det større mellomrom eller tar vekk strengen and , blir den borte


  #3. Navnehelsing og input

name = input ('What is your name?')
greeting = 'Hey hey'

print(f'{greeting}' + '' +  f'{name}!')
# print(f'{name}!')
# namnet vises

#4 favorittfarge med input
colour = input ('What is your favorite colour?')
colour_one = 'blue'
colour_two = 'yellow'
colour_three = 'pink'

colour_greeting = 'Your favorite colour is '

#print(f'{colour_greeting}' + colour_three + ' ' f'{colour_two}!')
print(f'{colour_greeting}'+colour)