#pris etter rabaatt

prices = [32.60, 39, 47, 87, 65.90]

for p in prices:
    discount = p * 0.80
    print(f'Price after discount:{discount:.2f}')

print()
print(f'Total sum before discount: {sum(prices):.2f}')
