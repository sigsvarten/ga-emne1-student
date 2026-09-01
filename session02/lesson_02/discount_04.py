#discount task

amount = float (input('Type in the amount here: '))

if amount >= 1000:
   discount_amount =  0.80 * amount
elif amount >= 500:
    discount_amount =  0.90 * amount
else: discount_amount = 0


print(f'The total price is: {discount_amount}')