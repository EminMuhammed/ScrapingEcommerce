from ScrapingEcommerce.Helpers.ScrapeHelpers import *



def parse_column_product(soup):
    products_area = soup.find("section", attrs={"class": "product-list-cards"})
    a_tags = products_area.find_all("div", attrs={"class": "product-card-end"})

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
    product_url_ful_list = ["https://www.mavi.com" + i for i in df]

    return product_url_ful_list


def parse_content(url_list):
    product_content = []
    for url in url_list:
        print(url)
        soup = get_content(url)
        title = soup.find("h1", attrs={"class": "product__title"}).text.strip()
        price = soup.find("span", attrs={"class": "price"}).text.strip()

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


base_url = "https://www.mavi.com/erkek/jean/c/2?page="

main(base_url, 1, "mavi3")