import requests
from bs4 import BeautifulSoup

url = "https://playhearthstone.com/ko-kr/cards?set=standard&collectible=1"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
r = requests.get(url, headers=header)
bs = BeautifulSoup(r.text, "lxml")

data = bs.find("div", {"id": "MainCardGrid"})
print(data)
