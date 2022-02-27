import tweepy
import requests
from bs4 import BeautifulSoup


URL = "https://bulten.mserdark.com/issues/dunya-halleri-38-1048496"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

rows = soup.find_all("div", class_="revue-p")

for row in rows:
    print(row.text)