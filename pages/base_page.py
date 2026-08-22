# -*- coding: utf-8 -*-
"""Базовый класс для всех страниц (Page Object).

Идея Page Object: каждая страница сайта — это класс. Локаторы и действия
живут внутри класса, а тесты вызывают понятные методы (login, add_to_cart)
и НЕ знают про селекторы. Если вёрстка поменяется — правим один Page Object,
а не десятки тестов. Это твои BasePage/LoginPage из Дня 4, только с реальным браузером.
"""


class BasePage:
    def __init__(self, page):
        # page — объект страницы Playwright (управляет браузером). Аналог self.driver.
        self.page = page

    def open(self, url):
        """Открыть URL в браузере."""
        self.page.goto(url)
