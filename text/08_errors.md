# 8章 エラー処理
この章ではエラー処理について学習します。

## try-except

エラーを意図的に発生させてみましょう。

```python
points = [80, 75, 90, 100]

# エラーが発生
point = points[4]

# 以降の処理はスキップされる
print("Hello")
# IndexError: list index out of range
```
上記のコードでは`point = points[4]`で、リストの要素外にアクセスしており、そこで処理が終了してしまっています。そのため、`print("Hello")`は実行されません。

そこで、エラーが発生しそうなコードをtry-exceptで囲むことで、エラーを補足することができます。

```python
points = [80, 75, 90, 100]
try:
  # エラーが発生
  point = points[4]

  # 以降の処理はスキップされる
  print("Hello")

except:
  # try-except内でエラー発生時のみ実行される
  print("Need a points between 0 and ", len(points) - 1)

# 以降の処理はスキップされない
print("Hello")
```

上記のコードではtry-except内でエラーが発生した場合、それがどのようなエラーでも同じメッセージが表示されてしまいます。それでは、ユーザーに詳細な情報を届けることができません。エラーの種類によって処理を分けたい場合は、`except [exceptiontype] as [name]`という記述をします。

```python
points = [80, 75, 90, 100]

while(True):
  val = input('input number')

  if(val == "q"):
    break

  try:
    point = points[int(val)]
    print(point)
  except IndexError as err:
    # try-except内でIndexError発生時のみ実行される
    print("Need a points between 0 and ", len(points) - 1)

  except Exception as other:
    # try-except内でIndexError以外のエラー発生時のみ実行される
    print("something else", other)
```
>input関数はユーザーの入力を待つ関数です。戻り値はユーザーの入力値を文字列型で返します。
inputをwhileで繰り返すことで、何度もユーザーの入力を待つことができます。

エラーの種類に関しては公式ドキュメントを参考にしてください。  
https://docs.python.org/3.7/library/exceptions.html#exception-hierarchy

## try-except-else
try-exceptでエラーの補足ができることがわかりました。
これにelseを追加して、エラーが発生しなかった場合の処理を追加することができます。

```python
try:
  result = 1 / 0
except ZeroDivisionError:
  print("dvided by 0")
else:
  # エラーが発生しなかった場合のみ実行される
  print("finished")
```
else句はエラーが発生しなかった場合のみ実行されます。以下のように書き換えてみましょう。

```python
try:
  result = 1 / 1
except ZeroDivisionError:
  print("dvided by 0")
else:
  # エラーが発生しなかった場合のみ実行される
  print("finished")
```

<div style="page-break-before:always"></div>

## try-finally
except句はエラー発生時、else句はエラー非発生時に実行されました。finally句を追加することで、エラーが発生しても発生しなくても実行する処理を記述することができます。

```python
try:
  result = 1 / 1
finally:
  print("finally")
```
エラーが発生する場合も記述してみましょう。

```python
try:
  result = 1 / 0
finally:
  print("finally")
```
いずれの場合でもfinallyが出力されたと思います。
また、間にexcept句を記述することもできます。

```python
try:
  result = 1 / 1
except ZeroDivisionError:
  print("dvided by 0")
finally:
  print("finally")
```

## 独自エラー
エラーを独自に定義するにはExceptionクラスを継承したクラスを作成します。

```python
class OverAgeException(Exception):
  pass

ages = [10, 8 , 9, 19]

try:
  for age in ages:
    if(age > 15):
      raise OverAgeException(age)
except OverAgeException as err:
  print("only under 15 years old ", age)
```
