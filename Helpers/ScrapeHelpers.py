import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/98.0.4758.102 '
                         'Safari/537.36'}


def get_content(url, r=False):
    r = requests.get(url, headers=headers)
    if r:
        print(r)
    soup = BeautifulSoup(r.content, "lxml")
    return soup


def save_excel(data, name):
    df = pd.DataFrame(data)
    df.to_excel("ScrapingEcommerce/Veriler/" + name + ".xlsx")
