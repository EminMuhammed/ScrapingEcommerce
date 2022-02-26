import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

base_url = "https://www.koton.com/tr/erkek/giyim/alt-giyim/jean-pantolon/c/M01-C01-N01-AK102-K100044?q=%3Arelevance" \
           "&psize=192&page="


# regex: .*/p/.*
# 24 ürün

def get_content(url):
    r = requests.get(url)
    print(r)
    soup = BeautifulSoup(r.content, "lxml")
    return soup


def collect_url(base_url, page_number):
    product_list = []
    for i in range(0, page_number + 1):
        url = base_url + str(i)
        print(url)
        soup = get_content(url)
        product_column = soup.find("div", attrs={"class": "product-list-container"})
        a_tags = product_column.find_all("a")

        for a in a_tags:
            product_list.append(re.findall(".*/p/.*", a.get("href")))

    return product_list


def get_unique_url(product_list):
    df = pd.DataFrame(product_list)
    df = df.dropna().reset_index()
    df = df.rename(columns={0: "data"})
    df = df["data"].unique()
    product_url_ful_list = ["https://www.koton.com" + i for i in df]

    return product_url_ful_list


def parse_content(url_list):
    product_content = []
    for url in url_list:
        print(url)
        soup = get_content(url)
        title = soup.find("h1").text.strip()
        if soup.find("span", attrs={"class": "newPrice"}) is not None:
            price = soup.find("span", attrs={"class": "newPrice"}).text.strip()
        elif soup.find("span", attrs={"class": "normalPrice"}) is not None:
            price = soup.find("span", attrs={"class": "normalPrice"}).text.strip()

        print(title)
        print(price)

        product_content.append([url, title, price])

    return product_content


def save_excel(data):
    df = pd.DataFrame(data)
    df.to_excel("Scraping/Mavi/Veriler/Koton_erkek_jeans.xlsx")


product_list = collect_url(base_url, 1)
len(product_list)
url_list = get_unique_url(product_list)
len(url_list)
product_content = parse_content(url_list)
save_excel(product_content)

