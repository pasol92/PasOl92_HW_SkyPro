from base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """Класс для работы со страницей входа в систему."""

    # Локаторы элементов страницы входа
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-btn")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Forgot password?")

    def __init__(self, driver):
        """
        Инициализация страницы входа.

        Args:
            driver (WebDriver): Экземпляр драйвера Selenium.
        """
        super().__init__(driver)
        self.url = "https://example.com/login"

    def open(self) -> None:
        """
        Открывает страницу входа.

        Returns:
            None
        """
        self.driver.get(self.url)

    @allure.step("Вводим email: {email}")
    def enter_email(self, email: str) -> None:
        """
        Вводит email в поле ввода.

        Args:
            email (str): Email для ввода.

        Returns:
            None
        """
        self.enter_text(self.EMAIL_FIELD, email)

    @allure.step("Вводим пароль: {password}")
    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в поле ввода.

        Args:
            password (str): Пароль для ввода.

        Returns:
            None
        """
        self.enter_text(self.PASSWORD_FIELD, password)

    @allure.step("Выполняем вход в систему")
    def click_login(self) -> None:
        """
        Кликает по кнопке входа.

        Returns:
            None
        """
        self.click_element(self.LOGIN_BUTTON)

    def login(self, email: str, password: str) -> None:
        """
        Выполняет полный процесс входа в систему.

        Args:
            email (str): Email пользователя.
            password (str): Пароль пользователя.

        Returns:
            None
        """
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self) -> str:
        """
        Получает текст сообщения об ошибке.

        Returns:
            str: Текст сообщения об ошибке или пустая строка, если ошибки нет.
        """
        try:
            error_element = self.find_element(self.ERROR_MESSAGE)
            return error_element.text
        except Exception:
            return ""

    def is_forgot_password_link_displayed(self) -> bool:
        """
        Проверяет, отображается ли ссылка «Забыли пароль?».

        Returns:
            bool: True, если ссылка видна, иначе False.
        """
        try:
            link = self.find_element(self.FORGOT_PASSWORD_LINK)
            return link.is_displayed()
        except Exception:
            return False
