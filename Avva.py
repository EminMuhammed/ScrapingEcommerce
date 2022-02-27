from ScrapingEcommerce.Helpers.ScrapeHelpers import *


def parse_column_product(soup):
    products_area = soup.find("div", attrs={"class": "ProductListContent"})
    a_tags = products_area.find_all("div", attrs={"class": "ItemOrj col-3"})

    return a_tags


def collect_url(base_url, page_number):
    product_list = []
    for i in range(1, page_number + 1):
        url = base_url + str(i)
        print(url)
        soup = get_content(url)
        a_tags = parse_column_product(soup)

        for i in a_tags:
            print(i.a.get("href"))
            product_list.append(i.a.get("href"))

    return product_list


def get_unique_url(product_list):
    df = pd.DataFrame(product_list)
    df = df.dropna().reset_index()
    df = df.rename(columns={0: "data"})
    df = df["data"].unique()
    product_url_ful_list = ["https://www.avva.com.tr" + i for i in df]

    return product_url_ful_list


def parse_content(url_list):
    product_content = []
    for url in url_list:
        print(url)
        soup = get_content(url)

        title = soup.find("h1").text.strip().split("\n")[0]
        try:
            price = soup.find("div", attrs={"class": "Formline IndirimliFiyatContent"}).find("span", attrs={
                "class": "spanFiyat"}).text.strip()
        except:
            price = None
        print(title)
        print(price)

        product_content.append([url, title, price])

    return product_content


def main(base_url, page_number, excel_name):
    product_list = collect_url(base_url, page_number)
    print("total product: ", len(product_list))
    url_list = get_unique_url(product_list)
    print("unique product: ", len(url_list))
    product_content = parse_content(url_list[:5])
    save_excel(product_content, excel_name)


base_url = "https://www.avva.com.tr/erkek-jean?sayfa="

main(base_url, 1, "avva")
