import json

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from modelsol import create_tables, Publisher, Book, Shop, Stock, Sale
import configparser  # импортируем библиотеку

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

with open('tests_data.json', 'r', encoding="utf-8") as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()
session.close()


def search_publisher_name_id():
    publisher_name = input('Введите имя писателя или его id : ')
    if publisher_name.isnumeric():
        for c in session.query(Publisher).filter(
                Publisher.id == int(publisher_name)).all():
            print(c)
    else:
        for c in session.query(Publisher).filter(
                Publisher.name.like(f'%{publisher_name}%')).all():
            print(c)


if __name__ == '__main__':
    search_publisher_name_id()
