# 12章 日時操作
この章では日時操作について学習します。

## datetimeモジュール
datetimeモジュールは日付や時間を操作するためのモジュールです。
まずは現在日時を取得してみましょう。nowメソッドを使用します。

```python
from datetime import datetime

now = datetime.now()

print(now)   # 2018-12-01 12:47:30.639691
```

### 指定日時の作成
指定した日時のdatetimeインスタンスを生成してみましょう。
コンストラクタに日時分秒を指定することで生成します。

```python
from datetime import datetime

d1 = datetime(2018, 12, 2)
d2 = datetime(2018, 12, 2, 1, 2, 3)

print(d1)  # 2018-12-02 00:00:00
print(d2)  # 2018-12-02 01:02:03
```

### 曜日の取得
datetimeインスタンスから曜日を取得することができます。
weekdayメソッドを使用します。

```python
from datetime import datetime

d = datetime(2018, 12, 2)
w = d.weekday()

print(w)  # 6
```

曜日は数値で返ってきます。数値と曜日は以下のように対応しています。

|数値|曜日|
|-|-|
|0|月曜日|
|1|火曜日|
|2|水曜日|
|3|木曜日|
|4|金曜日|
|5|土曜日|
|6|日曜日|

<div style="page-break-before:always"></div>

### 日時を文字列に変換
日時を指定フォーマットの文字列に変換することができます。
strftimeメソッドを使用します。

```python
from datetime import datetime

d = datetime(2018, 12, 2)
date_string = d.strftime("%Y/%m/%d")

print(date_string)  # 2018/12/02
```

フォーマットの記号の詳細は公式ドキュメントを参照してください。  
https://docs.python.org/3.7/library/datetime.html#strftime-and-strptime-behavior

### 文字列を日時に変換
反対に文字列からdatetimeインスタンスを生成することができます。
strptimeメソッドを使用します。

```python
from datetime import datetime

d = datetime.strptime("2018/12/2", "%Y/%m/%d")

print(d)  # 2018-12-02 00:00:00
```

### timedeltaクラス
日付の加減算を行うにはtimedeltaクラスを使用します。

```python
from datetime import datetime, timedelta

d = datetime.now()
oneday = timedelta(days = 1)
yesterday = d - oneday

print(yesterday)  # 2018-11-30 13:14:42.034219
```

### dateクラス
日付までで時分秒の情報が必要ない場合はdateクラスを使用しましょう。

```python
from datetime import date

d1 = date.today()
d2 = date(2018, 12, 2)

print(d1)
print(d2)
```
