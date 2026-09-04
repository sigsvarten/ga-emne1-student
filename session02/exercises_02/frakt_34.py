# bergegne fraktkostnad

the_weight = float(input('What is weight in kilograms? '))

if the_weight < 2:
    print ('Price is 79 kroner')
elif the_weight >= 2 and the_weight < 5:
    print('This price is 129 kroner')
elif the_weight >= 5 and the_weight < 10:
    print('The price is 199 kroner')
else:
    print('We can not send this' )