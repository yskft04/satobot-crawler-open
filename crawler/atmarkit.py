from urllib import request  # urllib.requestモジュールをインポート
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート


def getLatestLinks():
    urls = []
    titles = []
    url = "https://atmarkit.itmedia.co.jp/ait/subtop/news/"
    response = request.urlopen(url)
    soup = BeautifulSoup(response)
    response.close()
    links = soup.find_all("div",class_="colBoxTitle")
    for li in links:
        #print(li)
        l = li.find("a")
        if l != None: #liに実態があれば
            url = l.get("href")
            title = li.text.replace( '\n' , '' )#何故か改行が入ってしまってる場合がある。
            #print(title)
            #print(url)
            titles.append(title)
            urls.append(url)
    return titles,urls