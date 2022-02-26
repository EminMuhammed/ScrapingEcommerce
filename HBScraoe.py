import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

base_url = "https://www.hepsiburada.com/mavi/erkek-t-shirt-c-12087279?sayfa="

# regex: .*/p/.*
# 24 ürün

def get_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/98.0.4758.102 Safari/537.36"}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")
    return soup


def parse_column_product(soup):
    products_area = soup.find("ul", attrs={"class": "productListContent-wrapper productListContent-grid-0"})
    a_tags = products_area.find_all("li", attrs={"class":"productListContent-item"})

    return a_tags


def collect_url(base_url, page_number):
    product_list = []
    for i in range(1, page_number+1):
        url = base_url + str(i)
        print(url)
        soup = get_content(url)
        a_tags = parse_column_product(soup)

        for i in a_tags:
            print(i.a.get("href"))
            product_list.append(i.a.get("href"))

        # for a in a_tags:
        #    product_list.append(re.findall(".*-p-.*", a.get("href")))

    return product_list


def get_unique_url(product_list):
    df = pd.DataFrame(product_list)
    df = df.dropna().reset_index()
    df = df.rename(columns={0: "data"})
    len(df["data"].unique())
    df = df["data"].unique()
    product_url_ful_list = ["https://www.hepsiburada.com" + i for i in df]

    return product_url_ful_list


def parse_content(url_list):
    product_content = []
    for url in url_list:
        soup = get_content(url)
        title = soup.find("h1", attrs={"itemprop":"name"}).text.strip()
        price = soup.find("span", attrs={"itemprop": "price"}).text.strip().split("TL")[0].strip()

        print(url)
        print(title)
        print(price)

        product_content.append([url, title, price])

    return product_content


def save_excel(data):
    df = pd.DataFrame(data)
    df.to_excel("Scraping/Mavi/Veriler/Mavi_hb_erkek_tisort.xlsx")


product_list = collect_url(base_url, 15)
url_list = get_unique_url(product_list)
len(url_list)
product_content = parse_content(url_list)
save_excel(product_content)


