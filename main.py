import requests
from bs4 import BeautifulSoup as bs
import lxml

domen = "https://aster.kz"

def pages_count(html_code):
    soup = bs(html_code, "lxml")
    num = soup.find("li", class_ = "page-item end").find("a").text
    return(num)

def get_urls(html_code):
    soup = bs(html_code, "lxml")
    url_lst = []
    for i in soup.find_all("a", class_ = "car__text car-link"):
        url_lst.append(domen + i.get("href"))
    return(url_lst)

def pars_page(html_code):
    discr = {
        "age": None,
        "eng_v": None,
        "eng_l": None,
        "mileage": None,
        "fuel_type": None,
        "transmission": None,
        "drive": None,
        "wheel": None
    }
    soup = bs(html_code, "lxml")
    soup.find("span", string = "Год выпуска").find_next_sibling()


#req = requests.get(url = domen + "/cars?page=1")
with open("test.html", "r", encoding = "utf-8") as f:
    code = f.read()
    pars_page(code)

