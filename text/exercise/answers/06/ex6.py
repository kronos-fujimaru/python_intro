prices = [1200, 2000, 1500, 1800]

under1500s = list(filter(lambda price: price <= 1500, prices))

print(under1500s)
