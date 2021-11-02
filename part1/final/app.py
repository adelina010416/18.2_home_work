# В этом финальном задании Вам предстоит написать приложение на Flask
# которое работает с двумя моделями Book и Review.
# 
#
# Для сущности Book должны быть созданы эндпоинты:
# /books        - работает с методами GET, POST
# /books/{id}   - работает с методами GET, PUT, DELETE
#
# Для сущности Review должны быть созданы эндпоинты:
# /reviews      - работает с методами GET, POST
# /reviews/{id} - работает с методами GET, PUT, DELETE
#
# Сведения для заполнения базы данных:
#
# Таблица books:
# +----+-------------------------------+---------------+------+-------+
# | id |              name             |     author    | year | pages |
# +----+-------------------------------+---------------+------+-------+
# | 1  | Гарри Поттер и Тайная Комната | Джоан Роулинг | 1990 |  400  |
# | 2  |       Граф Монте-Кристо       |      Дюма     | 1510 |  1344 |
# | 3  |  Гарри Поттер и Орден Феникса | Джоан Роулинг | 1993 |  500  |
# | 4  |   Гарри Поттер и Кубок Огня   | Джоан Роулинг | 1994 |  600  |
# +----+-------------------------------+---------------+------+-------+
#
# Таблица reviews:
# +----+-------+--------+---------+
# | id |  user | rating | book_id*|
# +----+-------+--------+---------+
# | 1  |  Oleg |   5    |    1    |
# | 2  |  Ivan |   6    |    2    |
# | 3  |  John |   4    |    3    |
# | 4  | Diana |   3    |    4    |
# +----+-------+--------+---------+
# *При создании таблицы reviews присваивать полю book_id свойство Foreign_key
#  необязательно.
#
# Структура вашего приложения должна выглядеть следующим образом:
#
# final
# ├── ./app.py         - Это главный файл, который запускает приложение
# ├── ./config.py      - Здесь мы сохраняем настройки приложения
# ├── ./constants.py   - Здесь мы сохраняем константы
# ├── ./models.py      - Здесь мы сохраняем модели
# ├── ./setup_db.py    - Здесь мы инициализируем базу данных
# ├── ./test.py        - Здесь наши тесты, запустите их, как проверите работу приложения
# └── ./views          
#     ├── ./views/books.py    - view-классы по модели Book
#     └── ./views/reviews.py  - view-классы по модели Review
#
# Пожалуйста, не меняйте название переменной 'app', которая должна 
# содержать экземпляр класса Flask, а также название переменной db,
# в которой вы инициализируете базу данных.
# это необходимо для корректной работы тестов
#
#

# app = Flask(__name__)