# 2.1 beregne drivtoffmengde og kostnad

distance = float(input('What is the distance? '))
fuel_per_100km = float(input('What is the usage per 100 km? '))

fuel_amount = distance / 100 * fuel_per_100km
fuel_price = fuel_amount * distance

print(f'The fuel amount: {fuel_amount:.2f}, and the price is {fuel_price:.2f}')

distance2 = float(input('What is this distance? '))
fuel_per_100km2 = float(input('What is the usage per 100 km? '))

fuel_amount2 = distance2 / 100 * fuel_per_100km2
fuel_price2 = fuel_amount2 * distance2

print(f'The fuel amount: {fuel_amount2:.2f}, and the price is {fuel_price2:.2f}')
