"""Фикстуры для UI-тестов.

Фикстуру `page` (готовая вкладка браузера) даёт плагин pytest-playwright —
её создавать не нужно, просто добавляй параметр `page` в тест.

Здесь две группы фикстур:
  1) login_page — открытая страница логина (для тестов самого логина);
  2) auth_state / auth_page — «залогинься один раз, переиспользуй сессию»
     (для тестов, которым логин не важен, а нужен уже авторизованный пользователь).
"""

from collections.abc import Iterator

import pytest
from playwright.sync_api import Browser, Page

from pages.login_page import LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Открытая страница логина saucedemo — готова к вводу."""
    lp = LoginPage(page)
    lp.load()
    return lp


@pytest.fixture(scope="session")
def auth_state(browser: Browser, tmp_path_factory) -> str:
    """Залогиниться ОДИН РАЗ за весь прогон и сохранить состояние (cookies/localStorage)
    в файл. Дальше тесты стартуют уже авторизованными — не тратят время на логин.
    scope="session" — выполняется единожды.
    """
    state_path = tmp_path_factory.mktemp("auth") / "state.json"
    context = browser.new_context()
    page = context.new_page()

    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")
    page.wait_for_url("**/inventory.html")  # дождались успешного входа

    context.storage_state(path=str(state_path))
    context.close()
    return str(state_path)


@pytest.fixture
def auth_page(browser: Browser, browser_context_args, auth_state: str) -> Iterator[Page]:
    """Страница в контексте с УЖЕ загруженной сессией (пользователь залогинен)."""
    context = browser.new_context(**browser_context_args, storage_state=auth_state)
    page = context.new_page()
    yield page
    context.close()
