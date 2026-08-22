"""Фикстуры для UI-тестов.

Фикстуру `page` (готовая вкладка браузера) даёт плагин pytest-playwright —
её создавать не нужно, просто добавляй параметр `page` в тест.
Ниже — своя фикстура поверх неё: открытая страница логина.
"""

import pytest

from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    """Открытая страница логина saucedemo — готова к вводу."""
    lp = LoginPage(page)
    lp.load()
    return lp
