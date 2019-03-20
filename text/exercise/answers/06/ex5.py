prices = [1200, 2000, 1500, 1800]

over1500s = list(filter(lambda price: price > 1500, prices))

print(over1500s)
