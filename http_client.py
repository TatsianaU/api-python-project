"""Модуль для выполнения HTTP GET-запросов."""
import requests


def get(url: str, params: dict | None = None, timeout: int = 10) -> dict | list:
    """
    Выполняет GET-запрос к указанному URL.

    Args:
        url: URL для запроса.
        params: Опциональные параметры запроса (query string).
        timeout: Таймаут запроса в секундах.

    Returns:
        JSON-данные ответа (dict или list).

    Raises:
        requests.RequestException: При ошибках сети или таймауте.
        requests.HTTPError: При кодах ответа 4xx/5xx.
    """
    response = requests.get(url, params=params, timeout=timeout)
    response.raise_for_status()
    return response.json()
