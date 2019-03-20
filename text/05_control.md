# 5章 制御構文
この章では制御構文について学習します。

## 条件分岐
条件分岐とは条件によって処理内容を変更する仕組みです。

### if
条件分岐をさせたい場合は、if文を使用します。

```python
point = 65
if(point > 60):
  # pointが60より大きい時のみ実行される
  print("success")
```

### if-else
if-else文を使用することで、条件が真の時の処理と、偽の時の処理をそれぞれ記述することができます。

```python
point = 65
if(point > 60):
  # pointが60より大きい時のみ実行される
  print("success")
else:
  # pointが60以下の時のみ実行される
  print("fail")
```

### elif
elif文を使用することで、分岐条件を追加することができます。

```python
point = 55
if(point > 80):
  # pointが80より大きい時のみ実行される
  print("success")
elif(point > 60):
  # pointが80以下で、かつ、60より大きい時のみ実行される
  print("good")
else:
  # pointが80以下で、かつ、60以下の時のみ実行される
  print("fail")
```

<div style="page-break-before:always"></div>

## 繰り返し
繰り返しとは同じ処理を繰り返す仕組みです。

### while文
繰り返しをしたい場合はwhile文条件に一致する内は、同じ処理を繰り返すことができます。

```python
count = 0
while(count < 5):
  # countが5になるまで繰り返す
  count += 1
  print(count)
```

#### continue
while文中に`continue`を記述すると、以降の処理はスキップされ、次の繰り返しが開始されます。

```python
count = 0

while(count < 5):
  count += 1
  if(count == 2):
    continue
  # countが2の時はスキップされる
  print(count)
```

#### break
while文中に`break`を記述すると、繰り返しを終了させることができます。

```python
count = 0

while(count < 10):
  count += 1
  if(count == 2):
    # countが2のときに繰り返しを終了する（以降は繰り返されない）
    break
  print(count)
```

#### while-else
while-else文を使用することで、while文が正常終了した時に処理を追加することができます。
正常終了とはbreakを使わずに終了することを表します。

```python
count = 0
while(count < 4):
  count += 1
  if(count == 5):
    break
  print(count)
else:
  # whileが正常終了した場合に、実行される
  print("success")
```

<div style="page-break-before:always"></div>

### for文
for文を使うと繰り返し可能なオブジェクトの要素数の数だけ、同じ処理を繰り返すことができます。
繰り返し可能なオブジェクトにはリスト、タプル、ディクショナリ、セット、文字列などがあります。

```python
points = [80, 75, 90, 100]

for point in points :
  # pointsの要素数の回数だけ繰り返される
  # pointにはpointsの要素が順番に代入される
  print(point)
```

#### continue
for文中に`continue`を記述すると、以降の処理はスキップされ、次の繰り返しが開始されます。

```python
points = {"math" : 80,
          "english" : 75,
          "science" : 90,
          "history" : 100}

for point in points.items():
  if(point[0] == "english"):
    continue
  # englishの時、スキップされる
  print(point)
```

#### break
for文中に`break`を記述すると、繰り返しを終了させることができます。

```python
points = {"math" : 80,
          "english" : 75,
          "science" : 90,
          "history" : 100}

for point in points.items():
  if(point[1] == 90):
    # 90がある時に、繰り返しを終了する
    break
  print(point)
```

<div style="page-break-before:always"></div>

#### for-else
for-else文を使用することで、for文が正常終了した時に処理を追加することができます。
正常終了とはbreakを使わずに終了することを表します。

```python
points = {"math" : 80,
          "english" : 75,
          "science" : 90,
          "history" : 100}

for point in points.items():
  if(point[1] == 85):
    break
  print(point)
else:
  # forが正常終了した場合に、実行される
  print("success")
```

#### range関数
range関数は、数値シーケンスを生成してくれます。

```python
# 1-9まで出力する
for i in range(1, 10):
  print(i)
```
