# A simple content aggregator from  Hacker News with the use of it's API
# Karima H - June 2023 - Updated April 2024


import requests
import time
import pyfiglet as pf
from tkinter import Tk, Label, Button, Text
import webbrowser as wb


def callback(url):
    wb.open_new_tab(url)


window = Tk()
window.configure(background='black', width=250, height=300)
window.title("Hacker News Content")
# print('\033[1;33;40m')
# print('\033[1;33;40m',pf.figlet_format('Hacker News', font = "cybermedium"),'\033[1;37;40m')
url = 'https://hacker-news.firebaseio.com/v0/beststories.json'
result = requests.get(url)
news_ids = result.json()
news = []
# print("...Gathering your articles...")


for new_id in news_ids[:3]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{new_id}.json"
    result = requests.get(url)
    data_collected = result.json()
    new_info = {
        'title': data_collected['title'],
        'author': data_collected['by'],
        'url': data_collected['url'],
        'hn_link': f"http://news.ycombinator.com/item?id={new_id}",
        'article_score': data_collected['score']
    }
    news.append(new_info)

for new_info in news:
    Label(window, text="Title: " + new_info['title'], foreground="white", background="black").grid()
    print(f"\033[1;34;40m\nTitle: {new_info['title']}\033[1;37;40m")
    Label(window, text="Author: " + new_info['author'], foreground="white", background="black").grid()
    Label(window, text="Link: " + new_info['url'], foreground="white", background="black").grid()
    Button(window, text="Open the url", command=lambda url=new_info['url']: callback(url)).grid()
    # print(f"Author: {new_info['author']}")
    # print(f"URL: {new_info['hn_link']}")
    # # print(f"Article Score: {new_info['article_score']}")
    # # time.sleep(0.2)


Button(window, text="close", command=window.quit).grid()
window.mainloop()
