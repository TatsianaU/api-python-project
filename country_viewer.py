"""Модуль просмотра информации о стране с цветным выводом."""
import sys

from colorama import Fore, Style, init

from http_client import get

init(autoreset=True)

# Обход проблем кодировки в консоли Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):
        pass

API_URL = "https://restcountries.com/v3.1/name/{country}"


def _label(text: str) -> str:
    return f"{Fore.CYAN}{text}{Style.RESET_ALL}"


def _value(text: str) -> str:
    return f"{Fore.WHITE}{text}{Style.RESET_ALL}"


def _highlight(text: str) -> str:
    return f"{Fore.YELLOW}{Style.BRIGHT}{text}{Style.RESET_ALL}"


def _section(text: str) -> str:
    return f"\n{Fore.GREEN}{Style.BRIGHT}{text}{Style.RESET_ALL}\n{'=' * 50}"


def fetch_country_data(country: str) -> dict | None:
    """Получает данные о стране из RestCountries API."""
    url = API_URL.format(country=country)
    try:
        data = get(url)
        return data[0] if isinstance(data, list) and data else data
    except Exception:
        return None


def format_currencies(currencies: dict) -> str:
    """Format currencies dict to string."""
    if not currencies:
        return "N/A"
    parts = []
    for code, info in currencies.items():
        symbol = info.get("symbol", "")
        name = info.get("name", "")
        parts.append(f"{code} ({symbol}) - {name}")
    return ", ".join(parts)


def format_languages(languages: dict) -> str:
    """Format languages dict to string."""
    if not languages:
        return "N/A"
    return ", ".join(languages.values())


def format_list(items: list) -> str:
    """Format list to string."""
    if not items:
        return "N/A"
    return ", ".join(str(x) for x in items)


def display_country(data: dict) -> None:
    """Display country data with colors."""
    name = data.get("name", {})
    common = name.get("common", "N/A")
    official = name.get("official", "N/A")

    flag = data.get("flag", "")
    code = data.get("cca2", "")
    header = f"  {flag} {common} [{code}]  " if flag else f"  {common} [{code}]  "
    print(_section(header))
    print(f"{_label('Официальное название:')} {_value(official)}")
    print(f"{_label('Столица:')}             {_value(format_list(data.get('capital', [])))}")
    print(f"{_label('Регион:')}              {_value(data.get('region', 'N/A'))}")
    print(f"{_label('Субрегион:')}           {_value(data.get('subregion', 'N/A'))}")
    print(f"{_label('Население:')}            {_highlight(f"{data.get('population', 0):,}")}")
    print(f"{_label('Площадь:')}             {_value(f"{data.get('area', 0):,.0f} км²")}")
    print(f"{_label('Валюты:')}              {_value(format_currencies(data.get('currencies', {})))}")
    print(f"{_label('Языки:')}               {_value(format_languages(data.get('languages', {})))}")
    print(f"{_label('Часовые пояса:')}       {_value(format_list(data.get('timezones', [])))}")
    print(f"{_label('Границы:')}             {_value(format_list(data.get('borders', [])))}")
    print(f"{_label('Коды:')}                {_value(f"cca2: {data.get('cca2', '')} | cca3: {data.get('cca3', '')} | ccn3: {data.get('ccn3', '')}")}")
    print(f"{_label('Независимость:')}       {_value('Да' if data.get('independent') else 'Нет')}")
    print(f"{_label('Член ООН:')}            {_value('Да' if data.get('unMember') else 'Нет')}")

    maps_data = data.get("maps", {})
    if maps_data:
        print(f"\n{_label('Карты:')}")
        print(f"  {_value('Google:')}    {maps_data.get('googleMaps', 'N/A')}")
        print(f"  {_value('OpenStreet:')} {maps_data.get('openStreetMaps', 'N/A')}")

    print()


def main() -> None:
    """Интерактивный просмотр информации о стране."""
    print(f"\n{Fore.MAGENTA}{Style.BRIGHT}Просмотр информации о стране{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}{'-' * 40}{Style.RESET_ALL}\n")

    while True:
        country = input(f"{_label('Введите название страны (пусто для выхода):')} ").strip()
        if not country:
            print(f"\n{_highlight('До свидания!')}\n")
            break

        data = fetch_country_data(country)
        if data is None:
            print(f"{Fore.RED}Страна не найдена. Попробуйте другое название.{Style.RESET_ALL}\n")
            continue

        display_country(data)


if __name__ == "__main__":
    main()
