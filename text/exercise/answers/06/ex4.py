def gen_to_tax(tax_rate):
    def to_tax(price):
        return price * (1 + tax_rate)
    return to_tax

to_tax8 = gen_to_tax(0.08)
to_tax10 = gen_to_tax(0.1)

print(to_tax8(1000))
print(to_tax8(2000))
print(to_tax10(1000))
print(to_tax10(2000))
