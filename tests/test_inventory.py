
from pages.inventory_page import InventoryPage

INVENTORY_URL = "https://www.saucedemo.com/inventory.html"


def test_inventory_available_with_saved_session(auth_page):
    # auth_page уже «залогинен» — сразу открываем страницу товаров
    auth_page.goto(INVENTORY_URL)

    inventory = InventoryPage(auth_page)
    assert inventory.is_loaded()
    assert inventory.products_count() == 6


def test_inventory_url_when_authenticated(auth_page):
    """С сохранённой сессией открытие страницы товаров НЕ выкидывает на логин.
    Открой INVENTORY_URL и проверь, что текущий адрес страницы содержит 'inventory'.
    """
    auth_page.goto(INVENTORY_URL)
    assert "inventory" in auth_page.url
    inventory = InventoryPage(auth_page)
    assert inventory.is_loaded()
