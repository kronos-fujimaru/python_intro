points = [80, 65, 75, 90, 80]

point_sum = 0
for point in points:
    if(point < 70):
        continue

    point_sum += point
    
print(point_sum)
