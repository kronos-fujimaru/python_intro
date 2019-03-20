# 15章 FaceAPI（補講）
この章ではFaceAPIの使用方法について学習します。

## FaceAPIとは
FaceAPIとは、Microsftが開発した顔検出、顔認証サービスです。
AIを使用して、写真から様々な情報を取得することができます。
以下の手順が必要になります。

1. サブスクリプションキーの取得
2. リクエスト情報の設定
3. リクエストの送信

## 1.サブスクリプションキーの取得
FaceAPIを使用するには、会員登録が必要になります。無料サブスクリプションであれば、クレジットカード情報などは不要ですが、7日間のみの使用となります。

https://azure.microsoft.com/ja-jp/try/cognitive-services/

APIキーを取得したら、変数に代入しておきます。

```python
subscription_key = "サブスクリプションキー"
```

## 2.リクエスト情報の設定

次にリクエストURLの設定をします。

```python
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'
```

次にサブスクリプションキーをヘッダー情報に追加します。

```python
header = {'Ocp-Apim-Subscription-Key': subscription_key }
```

画像のURLを渡すディクショナリを生成します。

```python
data = {"url" : "画像URL"}
```

取得したい情報を絞り込みます。

```python
params = {
'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
}
```

## 3.リクエストを送信

POSTでリクエストを送信し、レスポンスからJSONデータを取り出します。

```python
response = requests.post(face_api_url, params=params, headers=headers, json=data)
face_attributes = response.json()
```

最終的には以下のようなコードになります。

```python
import requests

subscription_key = "サブスクリプションキー"

face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

data = {"url" : "画像URL"}

params = {
'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
}

response = requests.post(face_api_url, params=params, headers=headers, json=data)
face_attributes = response.json()

print(face_attributes)
```

## matplotlib
matplotlibはグラフを簡単に描画してくれるライブラリです。
公式サイトは以下になります。  
https://matplotlib.org/

### matplotlibのインストール
pipを使用して、matplotlibをインストールします。

```
% pip install matplotlib
```

### グラフの描画
簡単な棒グラフを描画してみましょう。

```python
import matplotlib.pyplot as plt

menMeans = (20, 35, 30, 35, 27)
labels = ("a", "b", "c", "d", "e")

p1 = plt.bar(labels, menMeans)
plt.show()
```

他にも様々なグラフが描画できます。公式サイトを参考にしてください。  
https://matplotlib.org/gallery/index.html

## 問題
FaceAPIで取得した感情情報をmatplotlibでグラフ化してください。
