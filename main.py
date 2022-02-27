import tweepy
import requests
from bs4 import BeautifulSoup

URL = "https://bulten.mserdark.com/issues/dunya-halleri-38-1048496"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
rows = soup.find_all("div", class_="revue-p")

for row in rows:
    tweets = []

    # divide text into twittable array
    words = row.text.split()
    content = ''
    for word in words:
        if len(content) + len(word) < 276:
            content += word + ' '
        else:
            content += '...'
            tweets.append(content.strip())
            content = ''

    if (len(content) > 0):
        tweets.append(content.strip())

    # add links at the end of the tweet series
    if (len(row("a")) > 0):
        links = row("a")

        for link in links:
            tweets.append(link.get("href").replace('?utm_campaign=D%C3%BCnya%20Halleri&utm_medium=email&utm_source=Revue%20newsletter', ''))

    # display tweets
    print(tweets)