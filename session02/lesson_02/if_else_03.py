# some if else

age = int (input('What is ypur age? '))

if  age <= 20:
    print ( 'You are under 20 year')
else:print ('you are not ')

# if testes først.
# elif testes bare hvis if var False.
# else brukes når ingen tidligere test var True.

points = int (input('What is the points? '))
#points = 54

if points >= 60:
    print ('Very good')
elif points >= 40:
    print ('Good enough')
else: print('You must go again! ')
