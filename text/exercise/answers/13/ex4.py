import json

points = {"math" : 80,
          "english" : 75,
          "science" : 90,
          "history" : 100}

with open("points.json", "w", encoding="utf-8") as f:
    json.dump(points, f)
