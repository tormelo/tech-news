import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)


# Requisitos 11 e 12
def option_0():
    print("Digite quantas notícias serão buscadas:")
    number = input()
    get_tech_news(int(number))


def option_1():
    print("Digite o título:")
    title = input()
    print(search_by_title(title))


def option_2():
    print("Digite a data no formato aaaa-mm-dd:")
    date = input()
    print(search_by_date(date))


def option_3():
    print("Digite a categoria:")
    category = input()
    print(search_by_category(category))


def option_4():
    print(top_5_categories())


def option_5():
    print("Encerrando script")


funcs = [option_0, option_1, option_2, option_3, option_4, option_5]


def analyzer_menu():
    print(
        "Selecione uma das opções a seguir:\n "
        "0 - Popular o banco com notícias;\n "
        "1 - Buscar notícias por título;\n "
        "2 - Buscar notícias por data;\n "
        "3 - Buscar notícias por categoria;\n "
        "4 - Listar top 5 categorias;\n "
        "5 - Sair.",
        end="",
    )
    option = input()

    try:
        funcs[int(option)]()
    except (IndexError, ValueError):
        print("Opção inválida", file=sys.stderr)
