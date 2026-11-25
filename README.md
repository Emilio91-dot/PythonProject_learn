# PythonProject_learn

Учебный проект для практики Python, Pydantic, pytest, генерации тестовых данных и работы с SQLAlchemy.

## Требования

- Python 3.10 или новее
- pip

## Установка

Создайте и активируйте виртуальное окружение, затем установите зависимости:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS и Linux:

```bash
source .venv/bin/activate
```

Установка пакетов:

```bash
python -m pip install -r requirements.txt
```

## Запуск тестов

```bash
python -m pytest
```

Некоторые упражнения используют GoRest API и требуют подключения к интернету.

## База данных

По умолчанию приложение использует SQLite и создаёт файл `app.db` при подключении. Для PostgreSQL задайте строку подключения через переменную окружения `DATABASE_URL`. Не храните пароли и другие секреты в исходном коде.

PowerShell:

```powershell
$env:DATABASE_URL = "postgresql+psycopg2://user:password@localhost:5432/database"
```

Для подключения к PostgreSQL установите драйвер `psycopg2-binary`.

## Структура проекта

- `src/generators` — генераторы тестовых данных
- `src/schemas` — модели Pydantic
- `src/baseclasses` — общие классы и обработка ответов
- `tests` — тесты pytest
- `database` — настройка SQLAlchemy

# PythonProject_learn

A learning project for practicing Python, Pydantic, pytest, test data generation, and SQLAlchemy.

## Requirements

- Python 3.10 or newer
- pip

## Install

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

## Run tests

```bash
python -m pytest
```

Some exercises use the GoRest API and require an internet connection.

## Database

The project uses SQLite by default and creates `app.db` when it connects. To use PostgreSQL, set the `DATABASE_URL` environment variable. Keep passwords and other secrets out of source code.

Install `psycopg2-binary` to use PostgreSQL.
