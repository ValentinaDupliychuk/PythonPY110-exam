import random
import json
from faker import *
from conf import MODEL


def main():
    """Данная функция является основной и запускает выполнение функции-генератора"""

    for i in range(100):
        print(next(dictionary()))


def pk_(pk=1):
    """
    Это счетчик.

    Он используется для подсчета количества книг. Тип данных int
    """

    while pk < 1000:
        return pk
        pk += 1


def title_():
    """Функция title_ считывает построчно названия книг из файла books.txt. Тип данных str"""

    with open("books.txt", "r", encoding="utf-8") as file:
        while True:
            title = file.readline()
            yield title.strip()


def year_():
    """Эта функция выводит год из случайной выборки. Тип данных int"""

    year = random.randint(1900, 2021)
    yield year


def pages_():
    """Данная функция выводит количество страниц из случайной выборки. Тип данных int"""

    pages = random.randint(10, 300)
    yield pages


def isbn13_():
    """Данная функция выводит isbn13 с помощью подключенного модуля faker. Тип данных str"""

    fake = Faker()
    for _ in range(101):
        isbn13 = fake.isbn13()
    yield isbn13


def rating_():
    """Данная функция выводит рейтинг книги из случайной выборки. Тип данных float"""

    rating = round(random.uniform(0, 5), 2)
    yield rating


def price_():
    """Данная функция выводит цену книги из случайной выборки. Тип данных float"""

    price = round(random.uniform(100, 500), 2)
    yield price    # выводим результат


def author_():
    """Данная функция выводит автора книги, сгенерированного при помощи модуля faker. Тип данных str"""

    x = random.randint(1, 3)
    fake = Faker()
    for author in range(x):
        author = fake.name()
    yield author


def dictionary():
    """Данная функция собирает все данные в единое целое. Тип данных dict"""

    yield{
        "model": MODEL,
        "pk": pk_(),
        "fields": {
            "title": next(title_()),
            "year": next(year_()),
            "pages": next(pages_()),
            "isbn13": next(isbn13_()),
            "rating": next(rating_()),
            "price": next(price_()),
            "author": next(author_())
        }
    }


filename = "books.json"

if __name__ == "__main__":
    print(next(main()))
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(main(), f, indent=4)
