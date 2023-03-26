# Домашнее задание к лекции «Python и БД. ORM»

## Задание 1

Составить модели классов SQLAlchemy по схеме:
![](readme/book_publishers_scheme.png)   
Интуитивно необходимо выбрать подходящие типы и связи полей.  

## Задание 2

Используя SQLAlchemy, составить запрос выборки магазинов, продающих целевого издателя.

Напишите Python скрипт, который:

- Подключается к БД любого типа на ваш выбор.  
- Импортирует необходимые модели данных.
- Выводит издателя (publisher), имя или идентификатор которого принимается через `input`.  


## Задание 3.1 (необязательное)

- Заполнение тестовых данных через миграцию или внешний скрипт.  
- Тестовые данные берутся из папки `fixtures`. Пример содержания в JSON файле.  

Возможно несколько вариантов реализации:
1. Парсится json, создаются соотведствующие экземляры моделей и сохраняются в БД.

## Общие советы:
- Параметры подключения к БД выносятся в отдельные переменные.  
- Заполнять можно вручную или выполнить 3.2.
