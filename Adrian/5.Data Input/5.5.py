###
# A program to calculate a discounted price of a product

price = float(input('Enter the price of your product: '))
discountprcnt = int(input('Enter the discount in %: '))
discount = float(1 - (discountprcnt/100))
print(f'The product without a discount costs: {price}, it has a discount of: {discountprcnt}%, so the price of the product after the discount is: {price*discount}, which is a reduction of {price - price*discount}')