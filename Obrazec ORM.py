import json

from pprint import pprint
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import configparser

from modelsol import create_tables, Publisher, Shop, Book, Stock, Sale

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings.ini")  # читаем конфиг

print('Перед запуском программы введите свой "login", "password" и имя БД в файл settings.ini')
login = (config["SQLs"]["login"])
password = (config["SQLs"]["password"])
name_db = config["SQLs"]["name_db"]

DSN = f"postgresql://{login}:{password}@localhost:5432/{name_db}"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('fixtures/tests_data.json', 'r') as fd:
    data = json.load(fd)
    # for record in data:
    #     pprint(record)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))


def search_publisher_name():
    pub_name = input('Введите имя писателя или его id : ')
    if pub_name.isnumeric():
        c = session.query(Book.title, Shop.name, Sale.price, Sale.count, Sale.date_sale). \
            join(Publisher).join(Stock).join(Sale).join(Shop).filter(Publisher.id == pub_name).order_by(Sale.date_sale)
        print(f'        Название книги           |  магазин   |стоимость| дата покупки')
        for book, shop, price, count, date in c:
            pprint(f'{book} | {shop:<10} | {price * count:<7} | {date}')

    else:
        c = session.query(Book.title, Shop.name, Sale.price, Sale.count, Sale.date_sale). \
            join(Publisher).join(Stock).join(Sale).join(Shop).filter(Publisher.name == pub_name).order_by(
            Sale.date_sale)
        print(f'        Название книги          |  магазин   |стоимость| дата покупки')
        for book, shop, price, count, date in c:
            pprint(f'{book} | {shop:<10} | {price * count:<7} | {date}')


if __name__ == '__main__':
    search_publisher_name()

