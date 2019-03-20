points = {"math" : 80,
          "english" : 75,
          "science" : 90,
          "history" : 100}

print(points.get("english"))       # 75
# 取得できない場合はNoneとなる
print(points.get("geographic"))    # None
# 第二引数に値を設定することで、存在しない場合にその値を返す
print(points.get("geographic", 0)) # 0
