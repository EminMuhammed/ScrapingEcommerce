import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/98.0.4758.102 '
                         'Safari/537.36'}


def get_content(url, response=False):
    """
    Girilen url'in sayfa kaynağını alır.
    Parameters
    ----------
    url: String - sayfa linki
    response: True/False - başarılı bir şekilde sayfaya girilip girilmedi mi kontrolü yapar

    Returns
    -------
    sayfa kaynağını döndürür.
    """
    r = requests.get(url, headers=headers)
    if response:
        print(r)
    soup = BeautifulSoup(r.content, "lxml")
    return soup


def save_excel(data, name):
    """
    Dataframe i excel olarak kaydeder.
    Parameters
    ----------
    data: dataframe
    name: String - excel dosya ismi

    Returns
    -------
    None
    """
    df = pd.DataFrame(data)
    df.to_excel("Veriler/" + name + ".xlsx")
