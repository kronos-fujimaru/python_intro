## 練習問題

### 問題1
受け取った値の平均を返す関数averageを定義してください。

```python
def average(???):
  ???

result1 = average(10, 20, 30, 40)
result2 = average(100, 300, 200)

print(result1)
print(result2)
```

[出力結果]

```
25.0
200.0
```

### 問題2
三角形の面積を返す関数calc_tryangle_areaを定義してください。

```python
def calc_tryangle_area(???):
  ???

result1 = calc_tryangle_area(bottom=5, height=4)
result2 = calc_tryangle_area(height=3, bottom=6)
result3 = calc_tryangle_area(3)

print(result1)
print(result2)
print(result3)
```

[出力結果]

```
10.0
9.0
0.0
```

### 問題3
商品の値段を引数で受け取り、税込価格で返す関数to_tax関数を定義してください。

```python
def to_tax(???):
  ???

print(to_tax(1000))
print(to_tax(2000))
```

[出力結果]

```
1080
2160
```

### 問題4
問題3で作成したto_tax関数を消費税8%と10%どちらでも計算できるようにクロージャgen_to_taxを定義してください。

```python
def gen_to_tax(???):
  ???

to_tax8 = gen_to_tax(0.08)
to_tax10 = gen_to_tax(0.1)

print(to_tax8(1000))
print(to_tax8(2000))
print(to_tax10(1000))
print(to_tax10(2000))
```

[出力結果]

```
1080.0
2160.0
1100.0
2200.0
```

### 問題5
次のリストを作成してください。

```python
prices = [1200, 2000, 1500, 1800]
```

filter関数とラムダ式を使用して、1500円より高いもののみのリストにして画面に出力してください。

```python
prices = [1200, 2000, 1500, 1800]

over1500s = ???

print(over1500s)
```

[出力結果]

```
[2000, 1800]
```

### 問題6

次のリストを作成してください。

```python
prices = [1200, 2000, 1500, 1800]
```

filter関数とラムダ式を使用して、1500円以下のみのリストにして画面に出力してください。

```python
prices = [1200, 2000, 1500, 1800]

under1500s = ???

print(under1500s)
```

[出力結果]

```
[1200, 1500]
```

### 問題7
次のリストを作成してください。

```python
prices = [1200, 2000, 1500, 1800]
```

map関数とラムダ式を使用して、全ての金額を税込にして画面に出力してください。

> map関数はリストの要素を一つずつ、第一引数の関数オブジェクトに渡して、処理結果を受け取ります。結果はどのようなデータ型でも構いません。受け取った値をそのまま取得します。

```python
prices = [1200, 2000, 1500, 1800]

tax_in_prices = list(map(lambda price: ???, prices))

print(tax_in_prices)
```

[出力結果]

```
[1296.0, 2160.0, 1620.0, 1944.0000000000002]
```

### 問題8
処理を開始したら「processing...]、完了したら、「finished」と出力するデコレータprocessingを定義し、次の関数をデコレートしてください。

```python
def add_all_count(count):
    total = 0
    for i in range(count):
      total += i

    return total

total = add_all_count(10000000)
print(total)
```

[出力結果]

```
processing...
finished
49999995000000
```
