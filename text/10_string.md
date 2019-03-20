# 10章 文字列操作
この章では文字列操作について学習します。

## フォーマット文字列の生成
フォーマット文字列は`%`を使用し文字列を生成する方法です。

```python
str1 = "%sは%sです" %("cat", "mammals")
str2 = "%(name)sは%(type)sです" %{"name":"dog", "type":"mammals"}

print(str1) # 猫は哺乳類です
print(str2) # 犬は哺乳類です
```

フォーマットの記号の詳細は公式ドキュメントを参照してください。  
https://docs.python.org/3.7/library/string.html#format-string-syntax

文字列クラスのformatメソッドを使用する方法もあります。

```python
str1 = "{0}は{1}です".format("cat", "mammals")

d = {"name":"dog", "type":"mammals"}
str2 = "{name}は{type}です".format(**d)

print(str1)
print(str2)
```
> 上記の**dはディクショナリ型を展開した上でformatメソッドに渡しています。

## 文字列の操作
### 文字列の検索
文字列内から文字を検索する方法をみてみましょう。
Pythonではリストの時に学習した、in演算子を使うことで文字列も検索することができます。

```python
exist = "cat" in "cat is mammals"
print(exist)  # True
```

### 文字列のインデックスの取得
検索した文字列が何番目に初めて出てくるかを調べることができます。
indexメソッドまたはfindメソッドを使用します。

```python
index1 = "cat is mammals".index("is")
print(index1) # 4
index2 = "cat is mammals".index("dog")  # ValueErrorが発生する
```

indexメソッドは検索文字列が存在しない場合はValueErrorが発生します。
findメソッドは検索文字列が存在しない場合、-1を返します。

```python
index1 = "cat is mammals".find("is")
print(index1) # 4
index2 = "cat is mammals".find("dog")
print(index2) # -1
```

<div style="page-break-before:always"></div>

### 開始文字列を調べる
文字列が指定の文字列で開始されているか調べることができます。
startswithメソッドを使用します。

```python
start_check1 = "cat is mammals".startswith("cat")
start_check2 = "cat is mammals".startswith("is")

print(start_check1) # True
print(start_check2) # False
```

### 終了文字列を調べる
文字列が指定の文字列で終了されているか調べることができます。
endswithメソッドを使用します。

```python
end_check1 = "cat is mammals".endswith("cat")
end_check2 = "cat is mammals".endswith("als")

print(end_check1) # False
print(end_check2) # True
```

### 英文字の確認
文字列がalphabeticのみで構成されているか確認することができます。
isalphaメソッドを使用します。

```python
alpha_check1 = "abc".isalpha()
alpha_check2 = "1ab".isalpha()
alpha_check3 = "あa".isalpha()

print(alpha_check1)   # True
print(alpha_check2)   # False
print(alpha_check3)   # True
```

### 英数字の確認
文字列がalphabetic、または、数値で構成されているか確認することができます。
isalnumメソッドを使用します。

```python
alnum_check1 = "abc".isalnum()
alnum_check2 = "1ab".isalnum()
alnum_check3 = "あa１".isalnum()

print(alnum_check1)   # True
print(alnum_check2)   # True
print(alnum_check3)   # True
```

<div style="page-break-before:always"></div>

### 数値の確認
文字列が数値のみで構成されているか確認することができます。
isdigitメソッド、または、isnumericメソッドを使用します。

```python
digit_check1 = "123.5".isdigit()
digit_check2 = "１２３".isdigit()
digit_check3 = "-3".isdigit()
digit_check4 = "ⅴ".isdigit()
digit_check5 = "ⅴ".isnumeric()

print(digit_check1) # False
print(digit_check2) # True
print(digit_check3) # False
print(digit_check4) # False
print(digit_check5) # True
```

### 文字列の分割
文字列を指定文字列で分割することができます。
splitメソッドを使います。
戻り値は分割された文字列のリストで返ってきます。

```python
split_strings1 = "a,b,c".split(",")
split_strings2 = "ab cd ef".split(" ")
split_strings3 = "ab cd ef".split(",")


print(split_strings1) # ['a', 'b', 'c']
print(split_strings2) # ['ab', 'cd', 'ef']
print(split_strings3) # ['ab cd ef']
```

### 文字列の置換
文字列を指定文字列で置換することができます。
replaceメソッドを使います。

```python
reaplaced1 = "Hello World".replace("l", "zz")
reaplaced2 = "Hello World".replace(" ", ",")

print(reaplaced1) # Hezzzzo Worzzd
print(reaplaced2) # Hello,World
```
