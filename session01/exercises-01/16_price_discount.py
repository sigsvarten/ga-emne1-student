#pris med rabatt

#test 1
price = float (input('Type in the price of the goods: '))
discount_percent = float (input(' The discount is: '))

discount_amount =  price / 100 * discount_percent
total_price = price - discount_amount

print(f'{discount_amount}' + ' is the discount amount ')
print(f'{total_price}' + ' is the final price ')

#test 2
price2 = float (input('Type in the price of this goods: '))
discount_percent2 = float (input(' This discount is: '))

discount_amount2 =  price2 / 100 * discount_percent2
total_price2 = price2 - discount_amount2

print(f'{discount_amount2}' + ' is the discount amount here ')
print(f'{total_price2}' + ' is the final price here ')

#test 3
price3 = float (input('Type in this price: '))
discount_percent3 = float (input(' Here is the discount '))

discount_amount3 =  price3 / 100 * discount_percent3
total_price3 = price3 - discount_amount3

print(f'{discount_amount3}' + ' is the discount amount ')
print('The final price here is: ' + f'{total_price3}')