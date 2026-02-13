"""Тестовый модуль для ручных запросов к API."""
import json
import sys

import requests

from country_viewer import display_country
from http_client import get

# Обход проблем кодировки в консоли Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

URL_HTTPBIN = "https://httpbin.org/get"
URL_REST_COUNTRIES = "https://restcountries.com/v3.1/name/{country}"
URL_RANDOM_DOG = "https://dog.ceo/api/breeds/image/random"


def _print_json(data: dict | list) -> None:
    """Печатает JSON-данные в читаемом виде."""
    print(json.dumps(data, indent=2, ensure_ascii=False))


def run_get_by_url() -> None:
    """Выполняет GET-запрос к httpbin.org."""
    try:
        data = get(URL_HTTPBIN)
        print("\n--- Результат GET-запроса ---\n")
        _print_json(data)
        print()
    except requests.RequestException as e:
        print(f"\nОшибка запроса: {e}\n")


def run_country() -> None:
    """Запрашивает и отображает данные о стране."""
    country = input("\nВведите название страны: ").strip()
    if not country:
        print("Страна не указана.\n")
        return

    url = URL_REST_COUNTRIES.format(country=country)
    try:
        data = get(url)
        country_data = data[0] if isinstance(data, list) and data else data
        display_country(country_data)
    except requests.HTTPError as e:
        if e.response and e.response.status_code == 404:
            print("\nСтрана не найдена. Попробуйте другое название.\n")
        else:
            print(f"\nОшибка HTTP: {e}\n")
    except requests.RequestException as e:
        print(f"\nОшибка запроса: {e}\n")


def run_random_dog() -> None:
    """Выводит ссылку на случайное изображение собаки."""
    try:
        data = get(URL_RANDOM_DOG)
        image_url = data.get("message", "")
        print(f"\n--- Случайная собака ---\n\n{image_url}\n")
    except requests.RequestException as e:
        print(f"\nОшибка запроса: {e}\n")


def main() -> None:
    """Главное меню приложения."""
    while True:
        print("\n" + "=" * 40)
        print("  Меню")
        print("=" * 40)
        print("  1 — GET по URL")
        print("  2 — Страна")
        print("  3 — Случайная собака")
        print("  0 — Выход")
        print("=" * 40)
        choice = input("\nВыберите пункт меню: ").strip()

        if choice == "0":
            print("\nДо свидания!\n")
            break
        elif choice == "1":
            run_get_by_url()
        elif choice == "2":
            run_country()
        elif choice == "3":
            run_random_dog()
        else:
            print("\nНеверный выбор. Введите 0, 1, 2 или 3.\n")


if __name__ == "__main__":
    main()
