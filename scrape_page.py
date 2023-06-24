import requests
from bs4 import BeautifulSoup as sp

my_url = "https://news.ycombinator.com/"
page = requests.get(my_url)

soup = sp(page.content, "lxml")
# print(soup)
news = soup.select('.titleline')[1]
# print(news_links.prettify())
links = news.select('a')[0]['href']
titles = soup.select('.storylink')
print(links)
print(titles)

