# A simple content aggregator from  Hacker News with the use of it's API
# Karima H - June 2023 - Updated April 2024


import requests
from tkinter import Tk, Label, Button
import webbrowser as wb


def callback(url):
    wb.open_new_tab(url)


window = Tk()
window.configure(background='black', width=250, height=300)
window.title("Hacker News Content")
url = 'https://hacker-news.firebaseio.com/v0/beststories.json'
result = requests.get(url)
news_ids = result.json()
news = []


for new_id in news_ids[:8]:
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

for index, new_info in enumerate(news):
    Label(window, text="Title: " + new_info['title'], foreground="white", background="black").grid(row=index, sticky="w")

    Label(window, text="Author: " + new_info['author'], foreground="white", background="black").grid(row=index, sticky="w")
    # Label(window, text="Link: " + new_info['url'], foreground="white", background="black").grid(sticky="e")
    Button(window, text="Open the url", command=lambda url=new_info['url']: callback(url)).grid(row=index,column=2, sticky="e")


Button(window, text="close", command=window.quit).grid()
window.mainloop()
