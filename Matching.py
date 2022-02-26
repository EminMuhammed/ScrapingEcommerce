import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)

def load_data():
    df_hb = pd.read_excel("Scraping/Mavi/Veriler/Mavi_hb_erkek_tisort.xlsx").iloc[:,1:]
    df_mavi = pd.read_excel("Scraping/Mavi/Veriler/Mavi_erkek_tisort_2.xlsx").iloc[:,1:]

    df_mavi = df_mavi.rename(columns={0: "url", 1: "title", 2: "price"})
    df_hb = df_hb.rename(columns={0: "url", 1: "title", 2: "price"})

    return df_hb, df_mavi


df_hb, df_mavi = load_data()


def add_product_code_mavi():
    product_code = [url.split("/p/")[1] for url in df_mavi.loc[:,"url"]]
    df_mavi["product_code"] = product_code


def add_product_code_hb():
    # code_list = []
    """
    for i in df_hb.loc[:, "title"]:
        print(i)
        if i.split(" ")[-1][0].isnumeric():
            # int(i.split(" ")[-1][0])
            code = i.split(" ")[-1]

        else:
            code = None

        code_list.append(code)
        print(code)
    """
    code_list = [i.split(" ")[-1] if i.split(" ")[-1][0].isnumeric() else None for i in df_hb.loc[:, "title"]]
    df_hb["product_code"] = code_list


add_product_code_hb()
add_product_code_mavi()


def save_excel(data):
    df = pd.DataFrame(data)
    df.to_excel("Scraping/Mavi/Veriler/Mavi_hb_erkek_tisort_code.xlsx")

save_excel(df_hb)

df_hb
df_mavi

df_hb.loc[:,["product_code"]]
df_mavi.loc[:,["product_code"]]


# eşleştirmeye buradan devam et


ddd = pd.merge(df_hb, df_mavi, on='product_code', how='left')

ddd.head()
df_mavi.head()
df_hb.head()
ddd

df_hb.head()

ddd.isnull().sum()

hhh = ddd.dropna()
hhh


