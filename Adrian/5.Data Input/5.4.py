###
# A program to calculate the VAT amount of a price

amount = float(input('Price: '))
vat = round(0.23 * amount, 2)
print(f'Your chosen amount is: {amount} and its vat of 23% is equal to: {vat}')
