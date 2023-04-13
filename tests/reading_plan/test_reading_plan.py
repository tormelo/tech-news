from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
from unittest.mock import patch
import pytest


def mock_find_news():
    return [
        {
            "url": "https://blog.betrybe.com/novidades/noticia-1",
            "title": "Notícia 1",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 4,
            "summary": "Sumário da notícia",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-2",
            "title": "Notícia 2",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 2,
            "summary": "Sumário da notícia",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-3",
            "title": "Notícia 3",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 10,
            "summary": "Sumário da notícia",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-4",
            "title": "Notícia 4",
            "timestamp": "04/04/2021",
            "writer": "Eu",
            "reading_time": 3,
            "summary": "Sumário da notícia",
            "category": "Ferramentas",
        },
    ]


def test_reading_plan_group_news():
    with patch("tech_news.analyzer.reading_plan.find_news", mock_find_news):
        with pytest.raises(ValueError):
            ReadingPlanService.group_news_for_available_time(0)

        reading_plan = ReadingPlanService.group_news_for_available_time(10)
        assert reading_plan == {
            "readable": [
                {
                    "chosen_news": [
                        ("Notícia 1", 4),
                        ("Notícia 2", 2),
                        ("Notícia 4", 3),
                    ],
                    "unfilled_time": 1,
                },
                {"chosen_news": [("Notícia 3", 10)], "unfilled_time": 0},
            ],
            "unreadable": [],
        }

        reading_plan = ReadingPlanService.group_news_for_available_time(1)
        assert reading_plan == {
            "readable": [],
            "unreadable": [
                ("Notícia 1", 4),
                ("Notícia 2", 2),
                ("Notícia 3", 10),
                ("Notícia 4", 3),
            ],
        }
