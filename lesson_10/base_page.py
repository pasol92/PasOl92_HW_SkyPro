from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    """Базовый класс для всех страниц."""

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы.

        Args:
            driver (WebDriver): Экземпляр драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator: tuple) -> WebElement:
        """
        Находит элемент на странице.

        Args:
            locator (tuple): Локатор элемента (By.XPATH, "xpath_value").

        Returns:
            WebElement: Найденный элемент.
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator: tuple) -> None:
        """
        Кликает по элементу.

        Args:
            locator (tuple): Локатор элемента.
        """
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator: tuple, text: str) -> None:
        """
        Вводит текст в поле.

        Args:
            locator (tuple): Локатор поля ввода.
            text (str): Текст для ввода.
        """
        field = self.find_element(locator)
        field.clear()
        field.send_keys(text)
