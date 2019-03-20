prices = [1200, 2000, 1500, 1800]

tax_in_prices = list(map(lambda price: price * 1.08, prices))

print(tax_in_prices)
