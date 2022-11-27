from dataclasses import dataclass
import requests as req
from bs4 import BeautifulSoup


@dataclass
class ForexStruct:
    name: str = ''


def get_currencies_indicators(soup):
    list_of_quotes = [
        v for v in soup.find_all('a')
            if "data-test" in v.attrs
            and v["data-test"] == "quoteLink"
    ]

    return list_of_quotes

if __name__ == "__main__":
    url = 'https://finance.yahoo.com/currencies'
    response = req.get(url)
    if not response.status_code == 200:
        raise ValueError("Could not get currencies")

    soup = BeautifulSoup(response.content, features="html.parser")
    print(type(soup))
