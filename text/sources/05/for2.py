points = {"math" : 80,
          "english" : 75,
          "science" : 90,
          "history" : 100}

for point in points.items():
    if(point[1] == 85):
        break

    print(point)
else:
    print("success")
