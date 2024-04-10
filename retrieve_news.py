# A simple content aggregator from  Hacker News with the use of it's API
# Karima H - June 2023 - Updated April 2024
from tkinter.font import Font

import requests
from tkinter import Tk, Label, Button, Frame
import webbrowser as wb


def callback(url):
    wb.open_new_tab(url)


window = Tk()
window.resizable(False, False)
window.configure(background='#4E51BA')
window.title("Hacker News Content")
bold_font = Font(family="Arial", size=15, weight="bold")
Label(window, text="     ", background="#7B7DB5").grid(columnspan=4, sticky='nsew')
Label(window, text="Hacker News Content", foreground="black", background="#7B7DB5", font=bold_font).grid(columnspan=4, sticky='nsew')

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
Label(window, text="Top 8 Best Stories", background="#7B7DB5", foreground='black', font="Arial, 15").grid(columnspan=4, sticky='nsew')
Label(window, text="     ", background="#7B7DB5").grid(columnspan=4, sticky='nsew')


for index, new_info in enumerate(news):
    Label(window, text=new_info['title'], foreground="white", background='#4E51BA', font=('Arial',11, 'bold')).grid(row=index+4, column=0, sticky='w')
    Label(window, text="by " + new_info['author'], foreground="white", background='#4E51BA', font='Arial, 9').grid(row=index+4, column=1, sticky='w')
    Label(window, text="score: " + str(new_info['article_score']), foreground="white", background='#4E51BA', font='Arial, 9').grid(row=index+4, column=2, sticky='w')
    Button(window, text="Read the full article", command=lambda url=new_info['url']: callback(url), font=('Arial', 9, 'bold'), background="#C3C8EE").grid(row=index+4, column=3,sticky='e')

window.mainloop()
