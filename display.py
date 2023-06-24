import requests
import time
import colorama
import pyfiglet
from retrieve_news import *


# add colors to the printing

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Author: {submission_dict['author']}")
    print(f"URL: {submission_dict['hn_link']}")
    print(f"Article Score: {submission_dict['article_score']}")
    time.sleep(0.2)