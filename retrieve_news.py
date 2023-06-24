import requests
import time
import pyfiglet as pf


print('\033[1;33;40m',pf.figlet_format('Hackar News', font = "cybermedium"),'\033[1;37;40m')


url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
result = requests.get(url)

# Process Information About Each Submission
submission_ids = result.json()
submission_dicts = []
print("Fetching your articles...")


for submission_id in submission_ids[:5]:
    # Make a separate api call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    result = requests.get(url)
    response_dict = result.json()
        
    # Build  a dict for each article
    submission_dict = {
        'title': response_dict['title'],
        'author': response_dict['by'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'article_score': response_dict['score']
    }
    submission_dicts.append(submission_dict)



for submission_dict in submission_dicts:
    print(f"\033[1;34;40m\nTitle: {submission_dict['title']}\033[1;37;40m")
    print(f"Author: {submission_dict['author']}")
    print(f"URL: {submission_dict['hn_link']}")
    print(f"Article Score: {submission_dict['article_score']}")
    time.sleep(0.2)