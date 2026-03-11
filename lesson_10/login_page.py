import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Открыть главную страницу магазина")
    def open(self) -> None:
        """Открывает URL сайта SauceDemo."""
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизоваться пользователем {username}")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему.
        :param username: Логин пользователя.
        :param password: Пароль пользователя.
        """
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
