import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

base_url = "https://www.defacto.com.tr/erkek-denim-pantolon?page="


# regex: .*/p/.*
# 24 ürün

headers = {
    'authority': 'www.defacto.com.tr',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.defacto.com.tr/erkek-denim-pantolon?page=1',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'DF.l144=h9JBjpqqRTpySQUFpos4oowU7yRjlpUdNUzETlkBwzaUA1jDmX15Bp97qYlQ6lqTU3Glfc1v9okH78PPaQrJyPbRSylWZnpQk3jnUMg2w6su/vjjTJ1qEb9Tqt0B0TzYVYo5XpeW3Bl1991lyEvfmy3nF0O/bkm7CeQufETJTbNJ6pnFMWsYhJgp9qvt+fTboOWyw3x2vMcn75CphMTcq9fGq2eynhqSWfnpd4luBYwk7hIC3Xn57uSWCkEOuPe9rv+4wVlXXUkjYJF5XnaGgw==; currentculture=tr-tr; _gcl_au=1.1.1566487073.1645269047; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%2209d4cdce-2d3c-4893-b27a-fa0f5e6d9ac3%22; OfferMiner_ID=YXEFONLIWYUIQBVB20220219141048; SelectedGender=L2Vya2Vr; SelectedGenderValue=MQ%253D%253D; scarab.visitor=%225A70659642EE5DE1%22; _hjSessionUser_2131605=eyJpZCI6IjliZWI3ZmQ5LWY0N2QtNTQ3MC04NGU1LTBjYzUwZjkyZTRmNyIsImNyZWF0ZWQiOjE2NDUyNjkwNDk5NzQsImV4aXN0aW5nIjp0cnVlfQ==; scarab.profile=%22M7666AZ22SPTR217%7C1645269093%22; SelectedMenuItem=L2Vya2Vr; DF.Customer.V2=e2cdee39-12ed-41bc-9021-b2413e13d6e0; source=www.google.com|www.google.com; _gid=GA1.3.463716086.1645902412; _hjSession_2131605=eyJpZCI6ImUyNGZjNWZmLTM0ZjYtNDMwNi04N2YxLWE3YzMzZjRjY2E1OSIsImNyZWF0ZWQiOjE2NDU5MDI0MTIxNzcsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; OM.lastCatUrl=/erkek-denim-pantolon; miniCartCount=0; _hjIncludedInSessionSample=0; direct_session=yes; _hjDonePolls=781585; PageNumber=5; _ga_1234567890=GS1.1.1645905724.3.1.1645906134.0; _ga=GA1.3.1537476175.1645269048; scarab.mayAdd=%5B%7B%22i%22%3A%22W6714AZ22SPNM29%22%7D%2C%7B%22i%22%3A%22X2427AZ22SPNM40%22%7D%2C%7B%22i%22%3A%22W6404AZ22SPWT34%22%7D%2C%7B%22i%22%3A%22W7082AZ22SPNM28%22%7D%5D; cto_bundle=41BrgF9qVHhKNVJSMjN2YTJnMVRVckVtbGphTiUyQkN2V3BaejR3QmhQZHBxTVMwanhvVTRsUmZobHcwdzhrQzdlVVpOa1p2ZVdqQ09RbllPck9VeXdLbmh3M2pyd3lrclRDRlBweFNCY2g0eTVQQkQ2VWtqSVZkMWhkRW1wVXhyODgyTGM1ZVhBZEtkRlZpek9POU05UU00eFJEUSUzRCUzRA; VL_CM_0=%7B%22Items%22%3A%5B%7B%22K%22%3A%22VL_LastPageViewTime%22%2C%22V%22%3A%222022-02-26%252023%253A08%253A55%22%2C%22E%22%3A%222024-02-16%2023%3A08%3A55%22%7D%2C%7B%22K%22%3A%22VL_TotalDuration%22%2C%22V%22%3A%22464%22%2C%22E%22%3A%222024-02-16%2023%3A08%3A55%22%7D%2C%7B%22K%22%3A%22VL_FirstVisitTime%22%2C%22V%22%3A%222022-02-19%252014%253A10%253A48%22%2C%22E%22%3A%222024-02-09%2014%3A10%3A48%22%7D%2C%7B%22K%22%3A%22VL_TotalPV%22%2C%22V%22%3A%2212%22%2C%22E%22%3A%222024-02-16%2023%3A08%3A55%22%7D%2C%7B%22K%22%3A%22VL_TotalVisit%22%2C%22V%22%3A%223%22%2C%22E%22%3A%222024-02-16%2023%3A02%3A05%22%7D%2C%7B%22K%22%3A%22OfferMiner_ID%22%2C%22V%22%3A%22YXEFONLIWYUIQBVB20220219141048%22%2C%22E%22%3A%222024-02-09%2014%3A10%3A48%22%7D%2C%7B%22K%22%3A%22OM_INW%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222024-02-09%2014%3A10%3A48%22%7D%2C%7B%22K%22%3A%22VL_FirstReferrer%22%2C%22V%22%3A%22https%253A%252F%252Fwww.google.com%252F%22%2C%22E%22%3A%222022-03-28%2022%3A06%3A52%22%7D%2C%7B%22K%22%3A%22OM_rDomain%22%2C%22V%22%3A%22https%253A%252F%252Fwww.defacto.com.tr%252Ferkek-denim-pantolon%22%2C%22E%22%3A%222024-02-16%2023%3A08%3A55%22%7D%2C%7B%22K%22%3A%22VLTVisitorC%22%2C%22V%22%3A%22%257B%2522data%2522%253A%257B%257D%257D%22%2C%22E%22%3A%222024-02-16%2023%3A08%3A57%22%7D%2C%7B%22K%22%3A%22OM_pv%22%2C%22V%22%3A%22W7082AZ22SPNM28%22%2C%22E%22%3A%222024-02-16%2023%3A08%3A55%22%7D%2C%7B%22K%22%3A%22OM_lpvs%22%2C%22V%22%3A%22W7082AZ22SPNM28%257C2022-02-26%252023%253A08%253A55~W6404AZ22SPWT34%257C2022-02-26%252023%253A08%253A43~X2427AZ22SPNM40%257C2022-02-26%252023%253A03%253A23~W6714AZ22SPNM29%257C2022-02-26%252023%253A02%253A05~W6229AZ22SPWT34%257C2022-02-19%252014%253A11%253A39~M7666AZ22SPTR217%257C2022-02-19%252014%253A11%253A32%22%2C%22E%22%3A%222024-02-16%2023%3A08%3A55%22%7D%2C%7B%22K%22%3A%22VL_LastVisitTime%22%2C%22V%22%3A%222022-02-26%252023%253A02%253A05%22%2C%22E%22%3A%222024-02-16%2023%3A02%3A05%22%7D%2C%7B%22K%22%3A%22VL_LastPVTimeForTD%22%2C%22V%22%3A%222022-02-26%252023%253A08%253A55%22%2C%22E%22%3A%222022-02-26%2023%3A38%3A55%22%7D%2C%7B%22K%22%3A%22VL_PVCountInVisit%22%2C%22V%22%3A%225%22%2C%22E%22%3A%222022-02-26%2023%3A38%3A55%22%7D%2C%7B%22K%22%3A%22VL_VisitStartTime%22%2C%22V%22%3A%222022-02-26%252023%253A02%253A05%22%2C%22E%22%3A%222022-02-26%2023%3A32%3A05%22%7D%2C%7B%22K%22%3A%22VL_PreviousVisitTime%22%2C%22V%22%3A%222022-02-26%252022%253A06%253A52%22%2C%22E%22%3A%222024-02-16%2023%3A02%3A05%22%7D%2C%7B%22K%22%3A%22VL_LastVisitResumes%22%2C%22V%22%3A%221%22%2C%22E%22%3A%222022-02-26%2023%3A32%3A05%22%7D%5D%7D; _hjCachedUserAttributes=eyJhdHRyaWJ1dGVzIjp7IkFkZHRvQ2FydCI6ZmFsc2UsIkZpcnN0IFNlc3Npb24gRGF0ZSI6IjI2LTAyLTIwMjIiLCJQYWdlTnVtYmVyIjo1LCJQcm9kdWN0VmlldyI6ImZhbHNlIn0sInVzZXJJZCI6ImUyY2RlZTM5LTEyZWQtNDFiYy05MDIxLWIyNDEzZTEzZDZlMCJ9; _ga_CJ64VY601G=GS1.1.1645905717.3.1.1645906374.59; plv=2367118,2431978,2464401,2064292',
}

def get_content(url):
    r = requests.get(url, headers=headers)
    print(r)
    soup = BeautifulSoup(r.content, "lxml")
    return soup


def parse_column_product(soup):
    products_area = soup.find("div", attrs={"class": "catalog-products"})
    a_tags = products_area.find_all("div", attrs={"class": "product-card"})

    return a_tags

def collect_url(base_url, page_number):
    product_list = []
    for i in range(1, page_number + 1):
        url = base_url + str(i)
        print(url)
        soup = get_content(url)
        a_tags = parse_column_product(soup)

        for i in a_tags:
            product_list.append(i.a.get("href"))

    return product_list



def get_unique_url(product_list):
    df = pd.DataFrame(product_list)
    df = df.dropna().reset_index()
    df = df.rename(columns={0: "data"})
    df = df["data"].unique()
    product_url_ful_list = ["https://www.defacto.com.tr" + i for i in df]

    return product_url_ful_list

def parse_content(url_list):
    product_content = []
    for url in url_list:
        print(url)
        soup = get_content(url)
        try:
            title = soup.find("h1", attrs={"class": "product-card__name"}).text.strip()

            price = soup.find("div",
                              attrs={"class": "product-card__price--new d-inline-flex align-items-baseline"}).text.strip()
        except:
            title = None
            price = None

        print(title)
        print(price)

        product_content.append([url, title, price])

    return product_content


def save_excel(data):
    df = pd.DataFrame(data)
    df.to_excel("Scraping/Mavi/Veriler/Defacto_erkek_jeans.xlsx")

product_list = collect_url(base_url, 2)

url_list = get_unique_url(product_list)
len(url_list)
product_content = parse_content(url_list)
save_excel(product_content)
