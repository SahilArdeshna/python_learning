import pprint
import requests
from bs4 import BeautifulSoup


def sort_by_votes(list):
    return sorted(list, key=lambda k: k["votes"], reverse=True)


def create_custom_hn():
    hn = []

    for page in range(1, 3):
        res = requests.get(f"https://news.ycombinator.com/news?p={page}")
        soup = BeautifulSoup(res.text, "html.parser")
        links = soup.select(".titleline > a")
        subtext = soup.select(".subtext")

        for idx, item in enumerate(links):
            vote = subtext[idx].select(".score")
            if len(vote):
                point = int(vote[0].getText().replace(" points", ""))

                if point > 99:
                    title = item.getText()
                    href = item.get("href", None)
                    hn.append({"title": title, "href": href, "votes": point})

    return sort_by_votes(hn)


pprint.pprint(create_custom_hn())
