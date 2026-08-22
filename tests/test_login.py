from pages.inventory_page import InventoryPage


def test_successful_login(login_page):
    # login_page — фикстура: уже открытая страница логина
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(login_page.page)
    assert inventory.is_loaded()
    assert inventory.title() == "Products"


def test_invalid_password_shows_error(login_page):
    login_page.login("standard_user", "wrong_password")

    assert "do not match" in login_page.error_text()
