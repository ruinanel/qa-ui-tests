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
