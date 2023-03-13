import requests
from bs4 import BeautifulSoup as bs
import lxml
import re

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
    discr["age"] = int(soup.find("span", string = "Год выпуска").find_next_sibling().text)
    discr["eng_v"] = float(re.findall(r"\S*", soup.find("span", string = "Двигатель").find_next_sibling().text)[0])
    discr["eng_l"] = float(re.findall(r"[(]\d*", soup.find("span", string = "Двигатель").find_next_sibling().text)[0][1:])
    discr["drive"] = re.findall(r"[(]\w*", soup.find("span", string = "Привод").find_next_sibling().text)[0][1:]
    discr["mileage"] = float(re.findall(r"[0-9 ]*", soup.find("span", string = "Пробег, км").find_next_sibling().text)[0].replace(" ", ""))
    discr["fuel_type"] = soup.find("span", string = "Тип топлива").find_next_sibling().text.lower()
    discr["transmission"] = re.findall(r"[(]\w*", soup.find("span", string = "Коробка передач").find_next_sibling().text)[0][1:].lower()
    discr["wheel"] = soup.find("span", string = "Руль").find_next_sibling().text.lower()
    return(discr)


req = requests.get(url = "https://aster.kz/catalog/236767")
if req.status_code == 200:
    res = pars_page(req.text)
    for i in res.keys():
        print(i + ": " + str(res[i]))

