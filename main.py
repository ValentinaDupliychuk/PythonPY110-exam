import random
import re
import json
from Faker import *
from conf import MODEL


def main():
    model()
    pk()
    fields()


def model_():
    filename = "conf.py"
    with open(filename, "r", encoding = "utf-8") as f:
        model = dict{model:f}
    print(model)

def pk_():
    pk = 1
    for i in range(101):
       pk +=1
       yield pk


def title_():
    with open("books.txt", "r", encoding = "utf-8") as file:
        title = re.compile(r"\b\w+\n?")
    yield title


def year_():
    year = random.randint(1970,2021)
    yield year


def pages_():
    pages = random.randint(10,200)
    yield pages


def isbn13_():
    Faker.seed(0)
    for _ in range(100):
        isbn13 = fake.isbn13()
    yield isbn13


def rating_():
    rating = random.random()
    yield rating


def price_():
    price = random.randint(100,500)
    yield price


def author_():
    Faker.seed(0)
    for _ in range(100):
        author = fake.name()
    yield author


def fields(**kwargs):
    title_()
    year_()
    pages_()
    isbn13_()
    rating_()
    price_()
    author_()
    for key, kwarg in enumerate(kwargs):
        print({key}:{kwarg})


if __name__ == "__main__":
    json.dump(main(100), indent = 4, encoding = "utf-8")
