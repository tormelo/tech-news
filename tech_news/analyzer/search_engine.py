from tech_news.database import db


# Requisito 7
def search_by_title(title):
    search_result = list(
        db.news.find(
            {"title": {"$regex": title, "$options": "i"}},
            {"title": 1, "url": 1, "_id": 0},
        )
    )

    return [(news["title"], news["url"]) for news in search_result]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
