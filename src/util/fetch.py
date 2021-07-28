from urllib.request import urlopen
from json import loads


def fetch_json(url):
    with urlopen(url) as fi:
        return loads(fi.read())


if __name__ == "__main__":
    print(fetch_json("https://caliber2-mock.revaturelabs.com:443/mock/evaluation/grades/assessment/2169"))
