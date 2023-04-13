from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    search_result = list(
        db.news.find(
            {"title": {"$regex": title, "$options": "i"}},
            # {"title": 1, "url": 1, "_id": 0},
        )
    )

    return [(news["title"], news["url"]) for news in search_result]


# Requisito 8
def search_by_date(date):
    try:
        q_datetime = datetime.strptime(date, "%Y-%m-%d")
        q_date = q_datetime.strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")

    search_result = list(
        db.news.find(
            {"timestamp": q_date},
            # {"title": 1, "url": 1, "_id": 0},
        )
    )

    return [(news["title"], news["url"]) for news in search_result]


# Requisito 9
def search_by_category(category):
    search_result = list(
        db.news.find(
            {"category": {"$regex": category, "$options": "i"}},
            # {"title": 1, "url": 1, "_id": 0},
        )
    )

    return [(news["title"], news["url"]) for news in search_result]
