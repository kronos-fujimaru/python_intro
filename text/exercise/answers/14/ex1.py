import requests, webbrowser, bs4

while(True):
  val = input('googling ')
  res = requests.get("https://www.google.co.jp/search?q=" + val)
  res.raise_for_status
  soup = bs4.BeautifulSoup(res.text)
  link_elems = soup.select(".r a")

  print(link_elems[0].get('href'))
  webbrowser.open("https://www.google.co.jp" + link_elems[0].get('href'))
