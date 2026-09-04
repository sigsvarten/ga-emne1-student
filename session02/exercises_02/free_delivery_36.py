   # bruk av boolean - or når et krav er tilstrekkelig

order_amount = 650
is_member = False

if order_amount >= 800 or is_member: #berre ein trenger være sann
    print('Free delivery!')
else:
    print('Not free! You must pay')
