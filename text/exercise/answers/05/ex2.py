points = [80, 65, 75, 90, 80]

point_max = 0
for point in points:
    if(point_max < point):
        point_max = point

print(point_max)
