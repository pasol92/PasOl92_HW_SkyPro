import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнить форму данными: {first_name} {last_name}")
    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет персональные данные для доставки.
        :param first_name: Имя покупателя.
        :param last_name: Фамилия покупателя.
        :param postal_code: Почтовый индекс.
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получить итоговую сумму заказа")
    def get_total(self) -> str:
        """
        Ожидает появления элемента с ценой и возвращает его текст.
        :return: Строка вида 'Total: $58.29'.
        """
        total_element = self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text
