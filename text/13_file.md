# 13章 ファイル操作
この章ではファイル操作について学習します。

## ファイルを読み込む
open関数を使用してファイルをプログラム上で開くことができます。
先にファイルを作成しましょう。users.csvというファイル名でカレントディレクトリに以下のファイルを作成します。

```csv
user1,pass1
user2,pass2
user3,pass3
```

次にopen関数を使用してusers.csvを読み込んでみましょう。

```python
f = open("users.csv", "r", encoding="utf-8")
text = f.read()

print(text)
'''
user1,pass1
user2,pass2
user3,pass3
'''

f.close()
```
open関数の第二引数の`r`はファイルを開くときのモードです。以下のような対応があります。

|文字|意味|
|-|-|
|r|読み込み（省略可)|
|w|書き込み|
|a|追加書き込み|
|b|バイナリモード|

> ファイルを閉じるにはcloseメソッドを使用します。

### 行毎に読み込む
ファイルの内容を行ごとに読み込むこともできます。
readlinesメソッドを使用します。

```python
f = open("users.csv", encoding="utf-8")

for line in f.readlines():
  print(line)

'''
user1,pass1

user2,pass2

user3,pass3
'''

f.close()
```

<div style="page-break-before:always"></div>

## ファイルに書き込む
ファイルにデータを書き込むにはwriteメソッドを使用します。

```python
f = open("writing.txt", "w", encoding="utf-8")

f.write("Hello World!")

f.close()
```

ファイルが作成されているので確認してみましょう。

```
% cat writing.txt
Hello World!
```

### 行毎に書き込む
writelinesメソッドを使用して、データを行毎に書き込むことができます。

```python
f = open("writing.txt", "w", encoding="utf-8")

f.writelines("Hello World 1\r\n")
f.writelines("Hello World 2\r\n")
f.writelines("Hello World 3\r\n")

f.close()
```
> 改行が必要な場合は改行コードも記述する必要があります。


### with
with文を使用することで、処理ブロックを抜けた時に自動的にファイルが閉じるようになります。
ファイルの閉じ忘れなどを防ぐことができます。

```python
with open("users.csv", "r", encoding="utf-8") as f:
  print(f.read())
```

<div style="page-break-before:always"></div>

## csvモジュール
CSVとはComma-Separated Valuesの略で、カンマ区切りのファイルのことです。
csvモジュールはCSVファイルを扱うためのモジュールです。
CSVファイルの読み込みをしてみましょう。

```python
import csv

with open("users.csv", "r", encoding="utf-8") as f:
  reader = csv.reader(f)
  for row in reader:
    print(row)
```

次にCSVファイルを作成してみましょう。CSVファイルに書き込むリストを用意します。

```python
import csv

new_users = [
          ["user4", "pass4"],
          ["user5", "pass5"],
          ["user6", "pass6"]
          ]

with open("users.csv", "a", encoding="utf-8") as f:
  writer = csv.writer(f)
  writer.writerows(new_users)
```

users.csvファイルを確認してみましょう。以下の内容が書き込まれていると思います。

```
user1,pass1
user2,pass2
user3,pass3
user4,pass4
user5,pass5
user6,pass6
```

<div style="page-break-before:always"></div>

## jsonモジュール
JSONとはJavaScript Object Notationの略で、キーと値をコロン、データをカンマで区切ったファイルのことです。
jsonモジュールはJSONファイルを扱うためのモジュールです。
JSONファイルを作成してみましょう。JSONファイルに書き込むディクショナリを用意します。

```python
import json

users = {"first_name" : "Taro",
         "last_name": "Tanaka",
         "age" : 20}

with open("users.json", "w", encoding="utf-8") as f:
  json.dump(users, f)
```

users.jsonファイルが作成され、以下の内容が書き込まれたと思います。

```
{"first_name": "Taro", "last_name": "Tanaka", "age": 20}
```

次にJSONファイルを読み込みます。

```python
import json

with open("users.json", "r", encoding="utf-8") as f:
  user = json.load(f)

print(user) # {'first_name': 'Taro', 'last_name': 'Tanaka', 'age': 20}
```

<div style="page-break-before:always"></div>

## パス構築
osモジュールを読み込んで、パスを生成することができます。
join関数を使用します。

```python
from os import path

p = path.join("path1", "path2", "path3")

print(p)  # path1/path2/path3
```

### 絶対パスを取得する
abspath関数で絶対パスを取得することができます。

```python
from os import path

p = path.abspath("users.csv")

print(p) # ~/Learning/python_introduction/text/sources/12/users.csv
```

### パスを分割する
split関数を使用して、パスを分割することができます。

```python
from os import path

p = path.split("~/Learning/python_introduction/text/sources/12/users.csv")

print(p) # ('/Learning/python_introduction/text/sources/12', 'users.csv')
```

### 存在チェック
exists関数を使用して、ファイル、ディレクトリが存在するか確認することができます。

```python
from os import path

exists1 = path.exists("users.csv")
exists2 = path.exists("XXX.csv")

print(exists1)  # True
print(exists2)  # False
```

### ファイルの削除
remove関数を使用してファイルを削除することができます。

```python
import os

os.remove("writing.txt")
```

<div style="page-break-before:always"></div>

### ディレクトリの作成と削除
ファイル同様、ディレクトリの作成と削除ができます。
作成する場合は、mkdir関数を使用します。
また、listdir関数でディレクトリの中身を確認することができます。

```python
import os

os.mkdir("dir1")
print(os.listdir("./"))   # ['users.csv', 'dir1']
```

削除する場合は、rmdir関数を使用します。

```python
import os

os.rmdir("dir1")
```
