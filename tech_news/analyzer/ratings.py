from tech_news.database import db


# Requisito 10
def top_5_categories():
    search_result = list(
        db.news.aggregate(
            [
                {"$group": {"_id": "$category", "count": {"$sum": 1}}},
                {"$sort": {"count": -1, "_id": 1}},
            ]
        )
    )

    return [result["_id"] for result in search_result[:5]]
