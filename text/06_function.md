# 6章 関数
この章では関数について学習します。

## 関数とは
関数とは処理のかたまりに名前をつけたものです。
名前を"呼び出す"ことによって何度でも処理を実行させることができます。


## 関数の定義
関数の定義には`def`を使用します。

```python
def greet():
  print("Hello")
```

関数は定義するだけでは実行されません。
関数を実行するには関数を"呼び出す"必要があります。

```python
def greet():
  print("Hello")

#関数呼び出し
greet()  # Hello
greet()  # Hello
```
## 引数
関数には引数を指定することができます。
引数とは呼び出し側から関数へ値を受け渡す仕組みです。

```python
def add(x, y):
  print(x + y)

add(1, 2)   # 3
add(2, -3)  # -1
```

## 戻り値
関数には戻り値を指定することができます。
戻り値とは関数から呼び出し側へ値を返す仕組みです。

```python
def add(x, y):
  return x + y

result1 = add(1, 2)
result2 = add(2, -3)

print(result1)  # 3
print(result2)  # -1
```

<div style="page-break-before:always"></div>

## 高度な引数利用
### 引数のデフォルト値
引数にデフォルト値を定義することができます。

```python
def greet(hour=8):
  if(hour >= 6 and hour < 12):
    return 'Good Morning'
  elif(hour >=12 and hour < 18):
    return "Hello"
  else:
    return "Good Evening"

print(greet()) # Good Morning
print(greet(14))  # Hello
```

### キーワード付き引数
引数受け渡し時に、引数名を指定して値を渡すことができます。

```python
def add(x=10, y= 0):
  return x + y

print(add(y=100))  # 110
print(add(x=20, y=10))  # 30
```

### 引数をタプル形式で受け取る
`*`を使用し、0個以上の値をタプル形式で受け取ることができます。

```python
def add(*elements):
  print(elements)
  result = 0
  for element in elements:
    result += element
  return result

result1 = add(10, 10, 20, 30)
result2 = add(10, 10)

print(result1)  # 70
print(result2)  # 20
```

<div style="page-break-before:always"></div>

### 引数をディクショナリ形式で受け取る
`**`を使用し、0個以上の値をディクショナリ形式で受け取ることができます。

```python
def add(**elements):
  print(elements)
  result = 0
  for element in elements.values():
    result += element
  return result

result = add(x=10, y=20, z=30)
print(result)
```

## docstring
docstringの機能を使用することで関数に説明文をつけることができます。
docstringを参照するにはhelp関数や__doc__を使用する。

```python
def add(x, y):
  '''
  arg1 : x < 0 return false
  arg2 : y < 0 return false
  else : return x + y
  '''
  if(x < 0 or y < 0):
    return false
  return x + y

help(add)
print(add.__doc__)
```

IPythonを使用していれば、イントロスペクションの機能で参照することもできる。

```python
In [8]: def add(x, y):
   ...:   '''
   ...:   arg1 : x < 0 return false
   ...:   arg2 : y < 0 return false
   ...:   else : return x + y
   ...:   '''
   ...:   if(x < 0 or y < 0):
   ...:     return false
   ...:
   ...:   return x + y
   ...:

In [9]: add?
Signature: add(x, y)
Docstring:
arg1 : x < 0 return false
arg2 : y < 0 return false
else : return x + y
File:      ~/<ipython-input-8-616a4d0d9633>
Type:      function
```

<div style="page-break-before:always"></div>

## スコープ
スコープとは参照範囲のことを表します。

### ローカル変数
関数内で定義した変数はローカル変数と呼ばれ、関数外では参照できません。

```python
def greet():
  message = "Hello"

print(message) # NameError: name 'message' is not defined
```

### グローバル変数
関数外で定義した変数はグローバル変数と呼ばれ、関数内でも参照できます。

```python
message = "Hello"

def greet():
  print(message)

greet() # Hello
```

では以下のように記述した場合、どちらの変数が参照されるでしょうか。

```python
message = "Hello"

def greet():
  message = "Good Morning"

greet()
print(message)
```

関数内でグローバル変数と同じ名前のローカル変数が定義された場合、関数内ではローカル変数が優先されて参照されます。グローバル変数にアクセスしたい場合は、`global 変数名`を使用します。

```python
message = "Hello"

def greet():
  # greet関数内ではグローバル変数のmessageが参照される
  global message
  message = "Good Morning"

greet()
print(message)
```

<div style="page-break-before:always"></div>

## 関数オブジェクト
Pythonでは関数もオブジェクトとして扱うことができます。

```python
def greet():
  print("Hello")

def run_something(func):
  func()

run_something(greet)  # Hello
```

`()`が関数呼び出しを意味しているため、`()`が無い場合は関数もオブジェクトとして扱います。

```python
def greet():
  print("Hello")

print(type(greet))  # <class 'function'>
```

## 関数のネスト
関数内に別の関数を定義し、使用することができます。

```python
def multi(x, y):
  def add(x, y):
    return x + y

  result = 0
  for i in range(y):
    result = add(result, x)
  return result

multi(3, 4)
```

## クロージャ
クロージャとは、関数内部の変数を永続的に保持するための仕組みです。

```python
def gen_calc_circle_area(pi):
  def calc_circle_area(radius):
    return pi * radius ** 2
  return calc_circle_area

# 円周率を3で計算するクロージャを生成
calc_circle_area1 = gen_calc_circle_area(3)

print(calc_circle_area1(1)) # 3
print(calc_circle_area1(2)) # 12

# 円周率は3.14で計算するクロージャを生成
calc_circle_area2 = gen_calc_circle_area(3.14)

print(calc_circle_area2(1)) # 3.14
print(calc_circle_area2(2)) # 12.56
```

<div style="page-break-before:always"></div>

## ラムダ式
基本的に関数は関数名をつけて定義すると学習しましたが、ラムダ式の機能を利用することで、無名の関数を定義することができます。
主に、一時的に使用される関数や、動的に内容を変更する必要がある関数に用いられます。

```python
# 関数名をつけずに定義する
add = lambda x, y: x + y
print(type(add))  # <class 'function'>
print(add(2, 3))  # 5
```

ラムダ式はどのような時に使うのでしょうか。
filter関数を例にとって考えてみましょう。
filter関数は、第一引数に論理値を返す関数オブジェクト、第二引数にリストを受け取る関数です。
IPythonで確認してみましょう。

```python
In [25]: filter?
Init signature: filter(self, /, *args, **kwargs)
Docstring:
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
Type:           type
```

filter関数はリストの要素を一つずつ、第一引数の関数オブジェクトに渡して、論理値を受け取ります。
受け取った値がTrueのものだけ取得してくれます。

```python
points = [80, 75, 90, 100]

over80 = lambda point: point > 80

filter_over80 = filter(over80, points)

passings = list(filter_over80)

print(passings) # [90, 100]
```

省略して以下のように記述するのが一般的です。

```python
points = [80, 75, 90, 100]

passings = list(filter(lambda point: point > 80, points))

print(passings) # [90, 100]
```

<div style="page-break-before:always"></div>

## デコレータ
デコレータは関数内関数の機能を利用して、処理の前後に共通の処理を記述したい場合に用いる。

```python
def add(x, y):
  print("calculating...")
  return x + y

# デコレータ
def logging(func):
  def new_function(*args):
    print("start")
    result = func(*args)
    print("finished")
    return result
  return new_function

add = logging(add)
print(add(1, 2))
```

`@シンボル`を利用することで、シンプルにデコレータを関数に実装することができます。

```python
# デコレータ
def logging(func):
  def new_function(*args):
    print("start")
    result = func(*args)
    print("finished")
    return result
  return new_function

@logging
def add(x, y):
  print("calculating...")
  return x + y


print(add(1, 2))
```
