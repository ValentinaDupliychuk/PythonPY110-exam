import random
import re
import json
from faker import *
from conf import MODEL


def main(): # Создаем основную функцию
    for _ in range(100):
        print(next(dictionary()))


def pk_(pk=1): # создаем функцию для pk  и задаем начальный аргумент для него
    while pk < 1000: # все равно pk жесткий, страшно уйти в бесконечный цикл и подвесить комп, который и так тормоз рода человеческого
        yield pk # выводим одно значение
        pk += 1 # меняем значение pk на следующее


def title_(): # создаем функцию для заголовков
    with open("books.txt", "r", encoding = "utf-8") as file: # открываем файл, где хранятся названия книг
        title = re.compile(r"\b\w+\w+\n?") # создаем регулярку для считывания низвания книги
    yield title # получаем заголовко книги. Правда куда приткнуть random я не знаю. Может, в регулярку можно?


def year_(): # создаем функцию для года
    year = random.randint(1900,2021) # случайный выбор фиксированного года, можно, конечно, с Гутенберга начать, но, думаю, этих книг нет в свободном доступе
    yield year # выводим год


def pages_(): # создаем функцию для вывода страниц
    pages = random.randint(10,300) # тоже фиксированный диапазон
    yield pages # выводим страницы


def isbn13_(): # создаем функцию для isbn13
    fake = Faker() # вводим модуль Faker
    for _ in range(100): # как уйти от жестких границ?!!
        isbn13 = fake.isbn13() # подлог isbn13
    yield isbn13 # выводим результат


def rating_(): # дошли до рейтинга. Создаем функцию
    rating = random.random() # вот и функция, используем модуль random
    yield rating # выводим значение рейтинга


def price_(): # создаем функцию для цены
    price = random.randint(100,500) # больше 500 все равно дорого покупать, проще скачать
    yield price # выводим результат


def author_(): # авторы!
    x = random.randint(1,3) # задаем произвольное количество авторов
    s = [] # создаем пустой список
    fake = Faker() # задаем модуль Faker
    for _ in range(x): # если авторов больше одного
        author = s.append(fake.name()) # формируем список авторов
    yield author # выводим результат


def dictionary(): # создаем фанкцию, которая все объединяет
    yield{
        "model":MODEL, # выводим через генератор все значения
        "pk": pk_(),
        "fields":{
            "title": next(title_()),
            "pages": next(pages_()),
            "isbn13": next(isbn13_()),
            "rating": next(rating_()),
            "price": next(price_()),
            "author": next(author_())
        }
    }


filename = "books.json" # создаем файл для json

if __name__ == "__main__":
    main()
    with open(filename, "w", encoding="utf-8") as f: # открываем файл для записи
        json.dump(main, f, indent=4) # а записывать он не хочет. Говорит, что он такое не записывает:(

