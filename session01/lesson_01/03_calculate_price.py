#calculate price

product_name = input('Name: ')
unit_price = float(input('Unit Price: '))
quantity = int(input('Quantity: '))

total = unit_price * quantity

print( f'{product_name}: {total}')
print( f'{product_name}: {total:.2f}')