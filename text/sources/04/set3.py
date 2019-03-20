points = {80, 75, 90, 100}

points.add("new element")

# 重複する値を追加しても無視される
points.add(80)

# {100, 75, 'new element', 80, 90}
print(points)
