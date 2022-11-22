import requests as req
from bs4 import BeautifulSoup
from dataclasses import dataclass
import os
import multiprocessing as mp


@dataclass
class ForexStruct:
    name: str = ''


def get_currencies_indicators():
    url = 'https://finance.yahoo.com/currencies'
    response = req.get(url)
    if not response.status_code == 200:
        raise ValueError("Could not get currencies")

    soup = BeautifulSoup(response.content, features="html.parser")

    list_of_quotes = [
        v for v in soup.find_all('a')
            if "data-test" in v.attrs
            and v["data-test"] == "quoteLink"
    ]

    return list_of_quotes


def main():
    pass


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == "__main__":
    p = mp.Process(target=f, args=('bob',))
    p.start()

    b = mp.Process(target=f, args=('alice',))
    b.start()

    p.join()
    b.join()
