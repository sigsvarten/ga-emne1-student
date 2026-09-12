#pris etter rabatt

def calculate_discounted_price(price, discount_percent):
    price_discount = (100 - discount_percent) / 100 * price
    return price_discount

total_price = calculate_discounted_price(100, 15)

total_price2 = calculate_discounted_price(65, 35)

print(f'The price after discount is: {total_price}')

print(f'The price after discount is: {total_price2}')