## 練習問題
### 問題1
以下の仕様にしたがってCarクラスを作成してください。

|属性名|説明|
|-|-|
|name|車の名前|

|メソッド名|引数|戻り値|説明|
|-|-|-|-|
|move|なし|なし|画面に「Move」を出力する|


[ヒント]

```python
class Car:
  ???

wagon = Car("Wagon")
wagon.move()
```

[出力結果]

```
Move
```

### 問題2
問題1で作成したCarクラスを以下の仕様にしたがって修正してください。

|属性名|説明|
|-|-|
|name|車の名前|
|gas|ガソリン量（単位はL）|

|メソッド名|引数|戻り値|説明|
|-|-|-|-|
|move|なし|なし|ガソリンがある場合：ガソリンをマイナス1して、画面に「Move」を出力する<br>ガソリンが無い場合：画面に「Stop」を出力する|


```python
class Car:
  ???

wagon = Car("Wagon", 3)

for i in range(1, 6):
  wagon.move()
```

[出力結果]

```
Move
Move
Move
Stop
Stop
```

### 問題3
以下の仕様にしたがって、FireTruckクラス（消防車）を作成してください。

|属性名|説明|
|-|-|
|name|車の名前|
|gas|ガソリン量（単位はL）|
|water|放水に使う水の量（単位はL|

|メソッド名|引数|戻り値|説明|
|-|-|-|-|
|move|なし|なし|ガソリンがある場合：ガソリンをマイナス1して、画面に「Move」を出力する<br>ガソリンが無い場合：画面に「Stop」を出力する|
|spray_water|なし|なし|画面に「Spray Water」を出力し、水量をマイナス1する|

```python
class Car:
  ???

class ???
  ???

fire_truck = FireTruck("fire_truck", 10, 10)

for i in range(1, 3):
  fire_truck.move()

fire_truck.splay_water()
```

[出力結果]

```
Move
Move
Spray Water
```

### 問題4
インスタンスの数を返すメソッドを実装してください。

```python
class Car:
  ???

class ???
  ???

print(???)
wagon = Car("Wagon", 3)
print(???)
fire_truck = FireTruck("fire_truck", 10, 10)
print(???)
```

[出力結果]

```
0
1
2
```
