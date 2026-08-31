#some calculations

cars = int(input ('How many cars? '))

price_car = 356941
service_fee = 2316

total_price = cars * price_car
subtotal = total_price +service_fee

price_per_car = subtotal  / cars

print(subtotal)
print(price_per_car)