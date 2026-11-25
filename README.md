# PythonProject_learn

Учебный проект для практики Python, Pydantic, pytest, генерации тестовых данных и SQLAlchemy.

## Установка

Нужен Python 3.10 или новее. Создайте виртуальное окружение и установите зависимости:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

## Тесты

```bash
python -m pytest
```

Тесты базы данных используют отдельную временную SQLite-базу и не обращаются к пользовательской базе.

## База данных

Строка подключения задаётся переменной окружения `DATABASE_URL`. По умолчанию используется SQLite-файл `app.db`. Для PostgreSQL установите `psycopg2-binary` и задайте URL подключения через эту переменную. Не добавляйте пароли в исходный код.

В проекте описаны таблицы пользователей и заказов в `database/tables.py`; генератор тестовых пользователей находится в `src/generators/user_type_generator.py`.
