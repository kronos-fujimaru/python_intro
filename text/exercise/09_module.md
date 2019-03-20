## 練習問題
### 問題1
modelディレクトリを作成し、以下の内容のcar.pyファイルを作成してください。

```python
class Car:
  def __init__(self, name, gas):
    self.name = name
    self.gas = gas

  def move(self):
    if(self.gas != 0):
      self.gas -= 1
      print("Move")
    else:
      print("Stop")
```

modelディレクトリの上の階層にmain.pyファイルを作成してください。

[ヒント]

```python
???

wagon = Car("wagon", 10)

for i in range(1, 3):
  wagon.move()
```

[出力結果]

```
Move
Move
```

### 問題2
car.pyをスクリプト実行した時だけ、main.pyと同じ内容が実行されるようにしてください。
