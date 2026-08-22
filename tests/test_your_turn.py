from pages.inventory_page import InventoryPage


def test_locked_out_user_shows_error(login_page):
    login_page.login("locked_out_user", "secret_sauce")
    assert "Sorry, this user has been locked out." in login_page.error_text()


def test_empty_username_shows_error(login_page):
    login_page.login("", "secret_sauce")
    assert "Username is required" in login_page.error_text()


def test_inventory_shows_six_products(login_page):
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(login_page.page)
    assert inventory.is_loaded()
    assert inventory.products_count() == 6
