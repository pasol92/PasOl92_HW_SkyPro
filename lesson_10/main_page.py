from base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    """Класс для работы с главной страницей приложения."""

    # Локаторы элементов главной страницы
    SEARCH_FIELD = (By.ID, "search-input")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    HEADER_LOGO = (By.CLASS_NAME, "header-logo")
    NAVIGATION_LINKS = (By.CSS_SELECTOR, ".nav-link")

    def __init__(self, driver):
        """
        Инициализация главной страницы.

        Args:
            driver (WebDriver): Экземпляр драйвера Selenium.
        """
        super().__init__(driver)
        self.url = "https://example.com"

    def open(self) -> None:
        """
        Открывает главную страницу.

        Returns:
            None
        """
        self.driver.get(self.url)

    def is_logo_displayed(self) -> bool:
        """
        Проверяет, отображается ли логотип на странице.

        Returns:
            bool: True, если логотип виден, иначе False.
        """
        try:
            logo = self.find_element(self.HEADER_LOGO)
            return logo.is_displayed()
        except Exception:
            return False

    def get_navigation_links_count(self) -> int:
        """
        Получает количество навигационных ссылок на странице.

        Returns:
            int: Количество навигационных ссылок.
        """
        links = self.driver.find_elements(*self.NAVIGATION_LINKS)
        return len(links)

    def search(self, query: str) -> None:
        """
        Выполняет поиск по запросу.

        Args:
            query (str): Текст для поиска.

        Returns:
            None
        """
        with allure.step(f"Вводим поисковый запрос: '{query}'"):
            self.enter_text(self.SEARCH_FIELD, query)

        with allure.step("Нажимаем кнопку поиска"):
            self.click_element(self.SEARCH_BUTTON)

    def get_page_title(self) -> str:
        """
        Получает заголовок страницы.

        Returns:
            str: Текст заголовка страницы.
        """
        return self.driver.title
