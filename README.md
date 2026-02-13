# API Test Client

CLI-приложение для тестирования HTTP-запросов к различным публичным API.

## Возможности

- **GET по URL** — тестовый запрос к httpbin.org
- **Страна** — информация о любой стране через RestCountries API
- **Случайная собака** — ссылка на случайное фото собаки из Dog CEO API

## Требования

- Python 3.10+
- requests
- colorama

## Установка

```bash
# Клонирование репозитория (если применимо)
# git clone <repository-url>
# cd API

# Создание виртуального окружения
python -m venv venv

# Активация (Windows)
venv\Scripts\activate

# Активация (Linux/macOS)
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt
```

## Запуск

```bash
python main.py
```

Или напрямую:

```bash
python test_client.py
```

## Меню

| Пункт | Описание |
|-------|----------|
| 1 | GET-запрос к https://httpbin.org/get |
| 2 | Поиск страны по названию (RestCountries API) |
| 3 | Случайное изображение собаки (Dog CEO API) |
| 0 | Выход из приложения |

## Структура проекта

```
API/
├── main.py           # Точка входа
├── test_client.py    # Главное меню и логика пунктов
├── http_client.py    # Модуль HTTP GET-запросов
├── country_viewer.py # Просмотр информации о стране (цветной вывод)
├── requirements.txt
└── README.md
```

## Модули

### http_client

Универсальный модуль для GET-запросов:

```python
from http_client import get

data = get("https://api.example.com/data", params={"key": "value"})
```

### country_viewer

Модуль можно запустить отдельно для просмотра информации о странах:

```bash
python country_viewer.py
```

## Используемые API

- [httpbin.org](https://httpbin.org) — тестирование HTTP-запросов
- [RestCountries](https://restcountries.com) — данные о странах
- [Dog CEO API](https://dog.ceo/dog-api/) — случайные изображения собак
