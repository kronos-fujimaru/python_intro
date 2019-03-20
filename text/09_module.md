# 9章 モジュール化
この章ではモジュール化について学習します。

## モジュール化とは
複雑なシステム機能を相互依存の強い部品同士で構成するのではなく、交換可能で独立した部品同士で構成するようにすることをモジュール化と言います。

### 機能ごとに別ファイルに分類する
計算機能を定義した`calculator.py`と、計算を実行するための`calculator_main.py`ファイルを別々に作成してみましょう。まず、以下の内容で`calculator.py`を作成します。

```python
def add(x, y):
  return x + y
```

次に`calculator_main.py`を作成します。別モジュールを使用するにはインポートという作業を行う必要があります。`import モジュール名`でインポートできます。

```python
import calculator

print(calculator.add(3, 4))
```

モジュールを作成したら、コマンドラインから`calculator_main.py`を実行します。

```
% python calculator_main.py
7
```

また、また、インポート文を`from モジュール名 import インポート対象`とすることで、参照時に省略が可能です。

```python
from calculator import add

print(add(3, 4))
```

### モジュールをパッケージ（フォルダ）ごとに分類する
モジュール化が進みファイルの数が増えてくると、今度はファイルの管理が難しくなってきます。ファイルが増えてきたらフォルダ分けしてファイルを管理しますよね。それと同様にしてモジュールもフォルダ分けして管理するようにします。このフォルダのことをパッケージと呼びます。先ほどの2ファイルを以下のようにフォルダ分けしてみましょう。

```
├── calculator_main.py
└── exercise
    └── calculator.py
```

<div style="page-break-before:always"></div>

## スクリプト化
以下の内容でexercise.greeterモジュールを作成してください。

```python
def greet():
  message = "Hello"
  print(message)

greet()
```
```
[ディレクトリ構成]
├── calculator_main.py
└── exercise
    ├── calculator.py
    └── greeter.py
```
greeterモジュールをcalculator_mainモジュールにインポートしてみましょう。

```python
from exercise.calculator import add
import exercise.greeter

print(add(3, 4))
```

作成できたら実行します。

```
% python calculator_main.py
Hello
7
```

calculator_mainモジュールではgreet関数は呼び出していませんが、Helloが出力されてしまっています。このようにグローバルスコープに書かれた内容はインポート時に自動的に実行されてしまいます。これを回避するには、スクリプト実行された場合のみgreet関数を呼び出すように、greeterモジュールを以下のように修正します。

```python
def greet():
  message = "Hello"
  print(message)

if __name__ == '__main__':
  greet()
```

修正したら実行します。

```
% python calculator_main.py
7
```

追記された__name__変数は特殊な変数で、import時にはモジュール名が自動的に代入され、スクリプト実行時には__main__が代入されます。
そのため、greeterモジュールをスクリプト実行するとHelloが出力されます。

```
% python exercise/greeter.py
Hello
```
