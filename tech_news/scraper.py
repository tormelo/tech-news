import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    HEADERS = {"user-agent": "Fake user-agent"}
    TIMEOUT = 3

    try:
        time.sleep(1)
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    return selector.css("h2.entry-title > a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    return selector.css("a.next::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)

    url = selector.css("div.pk-share-buttons-wrap::attr(data-share-url)").get()

    title = (
        selector.css("h1.entry-title::text").get().replace("\xa0", "").strip()
    )

    timestamp = selector.css("li.meta-date::text").get()

    writer = selector.css("span.author a::text").get()

    reading_time = int(
        selector.css("li.meta-reading-time::text").re_first(r"\d+")
    )

    first_paragraph = selector.css("div.entry-content p")[0]
    summary = (
        "".join(first_paragraph.css("* ::text").getall())
        .replace("\xa0", "")
        .strip()
    )

    category = selector.css("div.meta-category span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
