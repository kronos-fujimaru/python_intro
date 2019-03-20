points = {"math" : 80,
          "english" : 75,
          "science" : 90,
          "history" : 100}

for point in points.items():
    print("{0} score is {1}".format(*point))
