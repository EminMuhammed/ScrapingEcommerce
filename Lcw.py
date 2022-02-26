import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

base_url = "https://www.lcwaikiki.com/tr-TR/TR/kategori/erkek/jean?PageIndex=1"


# regex: .*/p/.*
# 24 ürün

def get_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/98.0.4758.102 Safari/537.36"}
    r = requests.get(url, headers=headers)
    print(r)
    soup = BeautifulSoup(r.content, "lxml")
    return soup


soup = get_content(base_url)

soup.find("div", attrs={"class":"product-grid"})

print(soup.prettify())






