"""ТВОИ ЗАДАНИЯ — напиши UI-тесты сама.

Где искать «инструменты»:
  - доступные методы страниц — в pages/login_page.py и pages/inventory_page.py
  - как в принципе устроен тест — в tests/test_login.py
  - фикстура login_page — уже открытая страница логина (см. tests/conftest.py)

Запуск:             pytest tests/test_your_turn.py -v
Посмотреть глазами:  pytest tests/test_your_turn.py --headed --slowmo 800
"""

from pages.inventory_page import InventoryPage


def test_locked_out_user_shows_error(login_page):
    """Заблокированный пользователь (login: locked_out_user) войти не может:
    после попытки входа появляется сообщение об ошибке о блокировке.
    Проверь и факт ошибки, и что она именно про блокировку.
    """
    login_page.login("locked_out_user", "secret_sauce")
    assert "Sorry, this user has been locked out." in login_page.error_text()


def test_empty_username_shows_error(login_page):
    """Попытка входа с пустым именем пользователя не проходит:
    появляется ошибка о том, что имя пользователя обязательно.
    """
    login_page.login("", "secret_sauce")
    assert "Username is required" in login_page.error_text()


def test_inventory_shows_six_products(login_page):
    """После успешного входа обычным пользователем страница товаров
    содержит ровно 6 позиций.
    """
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(login_page.page)
    assert inventory.is_loaded()
    assert inventory.products_count() == 6
