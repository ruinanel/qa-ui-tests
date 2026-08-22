"""Тесты с УЖЕ авторизованным пользователем (сессия переиспользуется через storage_state).
Обрати внимание: в этих тестах НЕТ шага логина — он выполнен один раз в фикстуре auth_state.

Запуск:  pytest tests/test_inventory.py -v
"""

import pytest

from pages.inventory_page import InventoryPage

INVENTORY_URL = "https://www.saucedemo.com/inventory.html"


# --- ПРИМЕР (проходит) ---
def test_inventory_available_with_saved_session(auth_page):
    # auth_page уже «залогинен» — сразу открываем страницу товаров
    auth_page.goto(INVENTORY_URL)

    inventory = InventoryPage(auth_page)
    assert inventory.is_loaded()
    assert inventory.products_count() == 6


# --- ТВОЁ ЗАДАНИЕ ---
def test_inventory_url_when_authenticated(auth_page):
    """С сохранённой сессией открытие страницы товаров НЕ выкидывает на логин.
    Открой INVENTORY_URL и проверь, что текущий адрес страницы содержит 'inventory'.
    """
    auth_page.goto(INVENTORY_URL)

    inventory = InventoryPage(auth_page)
    assert inventory.is_loaded()
