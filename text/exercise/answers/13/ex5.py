import json

with open("points.json", "r", encoding="utf-8") as f:
    points = json.load(f)

print(points["science"])
