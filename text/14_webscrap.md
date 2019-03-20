# 14章 Webスクレイピング
この章ではWebスクレイピングについて学習します。

## Webスクレイピングとは
Webスクレイピングとは、プログラムを使ってWebからコンテンツをダウンロードして処理することです。
以下のモジュールを使用します。

- webbrowser
- requests
- BeautifulSoup

## webbrowser
webbrowserモジュールはブラウザを操作します。

```python
import webbrowser

webbrowser.open("http://python.org")
```

入力した住所のGoogleMapを開くようにしてみましょう。

```python
import webbrowser

while(True):
  address = input('input address')
  print(address)
  webbrowser.open("https://www.google.co.jp/maps/place/" + address)
```

## requests
requestsモジュールはHTTPリクエストを送信するためのモジュールです。
Python付属のモジュールでないため、インストールする必要があります。
ここではpipというパッケージマネージャーを使用してインストールします。

```
% pip install requests
```

ではrequestsモジュールを使用してリクエストを送信してみましょう。

```python
import requests

res = requests.get("http://python.org")

print(type(res))
print(res.text)
print(res)
```

HTMLが取得できたと思います。

<div style="page-break-before:always"></div>

### エラーチェック
HTTPリクエストは様々な理由から常に正常にレスポンスが帰ってくるとは限りません。そのため、エラーのチェックが必要になります。raise_for_statusメソッドは正常にレスポンスであれば何もせず、異常がある場合のみ、例外を発生させます。

```python
import requests

res = requests.get("http://python.org")

res.raise_for_status()
```

この状態では何も起きません。あえてURLを間違えてみましょう。

```python
import requests

res = requests.get("http://python.xxx")

res.raise_for_status()
```

## BeautifulSoup
BeautifulSoupはHTMLから情報を抽出するモジュールです。
requestsモジュール同様、Pythonに付属していないのでpipでインストールします。

```
% pip install beautifulsoup4
```

WebサイトをBeautifulSoupに読み込ませてみましょう。

```python
import requests, bs4

res = requests.get("http://python.org")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
print(type(soup))
```

BeautifulSoupインスタンスが生成されたので、selectメソッドを使用して、要素を探します。
要素の検索にはCSSセレクタを使用します。メタタグを取得してみましょう。

```python
import requests, bs4

res = requests.get("http://python.org")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
elems = soup.select("meta")

print(elems)
print(str(elems[0))
print(elems[0].attrs)
print(elems[0].get("charset"))
```

これを応用して、Yahooの画像検索の結果を収集してみましょう。

```python
import requests, bs4, os

# 検索キーワードはApple
keyword = "Apple"

# 画像を保存するフォルダを作成
os.mkdir(keyword)

# 画像検索の結果のURLにリクエストを送信
res = requests.get("https://search.yahoo.co.jp/image/search?p={0}&ei=UTF-8&fr=top_ga1_sa".format(keyword))
res.raise_for_status()

# レスポンスからimgタグを取得する
soup = bs4.BeautifulSoup(res.text)
elems = soup.select("img")

# imgタグの個数だけ繰り返す
count = 0
for elem in elems:

  # imgタグのsrc属性から画像URLを取得
  image_url = elem.get("src")

  print("Downloading... {0}".format(image_url))

  # 画像URLにリクエストを送る
  image_res = requests.get(image_url)
  image_res.raise_for_status()

  # 画像ファイルの保存名生成
  filename = os.path.join(keyword, str(count) + ".png")
  count += 1

  # 画像ファイル保存（画像はバイナリデータなので"wb"
  with open(filename, "wb") as f:

    # レスポンスを保存する場合は、iter_contentメソッドを使用し、チャンクごとに保存する
    # 各チャンクはバイトデータ型で、最大バイト数を指定する（10KB)
    for chunk in image_res.iter_content(100000):
      f.write(chunk)
```
