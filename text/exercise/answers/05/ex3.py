points = [80, 65, 75, 90, 80]

point_min = 100
for point in points:
    if(point_min > point):
        point_min = point

print(point_min)
