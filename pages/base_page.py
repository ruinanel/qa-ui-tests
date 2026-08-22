"""Базовый класс для всех страниц (Page Object).

Идея Page Object: каждая страница сайта — это класс. Локаторы и действия
живут внутри класса, а тесты вызывают понятные методы (login, add_to_cart)
и НЕ знают про селекторы. Если вёрстка поменяется — правим один Page Object,
а не десятки тестов. Это твои BasePage/LoginPage из Дня 4, только с реальным браузером.
"""

import logging

from playwright.sync_api import Page

logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self, page: Page) -> None:
        # page — объект страницы Playwright (управляет браузером). Аналог self.driver.
        self.page = page

    def open(self, url: str) -> None:
        """Открыть URL в браузере."""
        self.page.goto(url)
