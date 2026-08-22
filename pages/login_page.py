"""Page Object страницы логина saucedemo.com."""

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    # Локаторы (селекторы элементов) — в одном месте
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def load(self) -> None:
        """Открыть страницу логина."""
        self.open(self.URL)

    def login(self, username: str, password: str) -> None:
        """Заполнить логин/пароль и нажать кнопку входа."""
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def error_text(self) -> str | None:
        """Вернуть текст сообщения об ошибке (если есть)."""
        return self.page.text_content(self.ERROR_MESSAGE)
