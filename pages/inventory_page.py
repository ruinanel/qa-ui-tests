"""Page Object страницы товаров (после успешного логина)."""

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = ".title"  # заголовок "Products"
    INVENTORY_LIST = ".inventory_list"  # контейнер со списком товаров
    INVENTORY_ITEM = ".inventory_item"  # один товар

    def title(self) -> str | None:
        """Текст заголовка страницы."""
        return self.page.text_content(self.TITLE)

    def is_loaded(self) -> bool:
        """Загрузилась ли страница товаров (виден список)."""
        return self.page.locator(self.INVENTORY_LIST).is_visible()

    def products_count(self) -> int:
        """Сколько товаров на странице."""
        return self.page.locator(self.INVENTORY_ITEM).count()
