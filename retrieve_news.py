# A simple job aggregator from  Hacker News with the use of it's API
# Karima H - June 2023


import requests
import time
import pyfiglet as pf

print('\033[1;33;40m')
print('\033[1;33;40m',pf.figlet_format('Hackar News', font = "cybermedium"),'\033[1;37;40m')
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
result = requests.get(url)
news_ids = result.json()
news = []
print("...Gathering your articles...")


for new_id in news_ids[:5]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{new_id}.json"
    result = requests.get(url)
    data_collected = result.json()
    new_info = {
        'title': data_collected['title'],
        'author': data_collected['by'],
        'hn_link': f"http://news.ycombinator.com/item?id={new_id}",
        'article_score': data_collected['score']
    }
    news.append(new_info)



for new_info in news:
    print(f"\033[1;34;40m\nTitle: {new_info['title']}\033[1;37;40m")
    print(f"Author: {new_info['author']}")
    print(f"URL: {new_info['hn_link']}")
    print(f"Article Score: {new_info['article_score']}")
    time.sleep(0.2)