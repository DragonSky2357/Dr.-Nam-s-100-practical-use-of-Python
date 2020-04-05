import requests
from bs4 import BeautifulSoup
import urllib.request
import pandas

url = "https://comic.naver.com/webtoon/weekdayList.nhn?week=fri"

r = requests.get(url)
bs = BeautifulSoup(r.text, "lxml")


MainCard = bs.select("ul.img_list > li")
results = []

for data in MainCard:
    Temp = data.select_one("div > a")
    link = Temp["href"]
    title = Temp["title"]

    author = data.select_one("dl > dd > a").text
    point = data.select("dl > dd")[1].select_one("strong").text

    results.append((title, author, point, link))

column = ["웹툰제목", "작가", "점수", "링크"]

dataframe = pandas.DataFrame(results, columns=column)
dataframe.to_excel("webtoon.xlsx", sheet_name="네이버웹툰", header=True, startrow=0)

# for data in MainCard:
#     urllib.request.urlretrieve(data["src"])
#     print("{} Done".format(data["src"]))
