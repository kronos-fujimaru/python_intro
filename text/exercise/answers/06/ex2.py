def calc_tryangle_area(bottom=0, height=0):
    return bottom * height / 2

result1 = calc_tryangle_area(bottom=5, height=4)
result2 = calc_tryangle_area(height=3, bottom=6)
result3 = calc_tryangle_area(3)

print(result1)
print(result2)
print(result3)
