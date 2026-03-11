import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        # 60 секунд достаточно, чтобы перекрыть задержку в 45 секунд
        self.wait = WebDriverWait(driver, 60)

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открывает страницу медленного калькулятора."""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    @allure.step("Установить задержку {delay} секунд")
    def set_delay(self, delay: int) -> None:
        """Устанавливает значение задержки выполнения."""
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    @allure.step("Нажать на кнопку '{value}'")
    def click_button(self, value: str) -> None:
        """Нажимает на кнопку калькулятора."""
        xpath = f"//span[text()='{value}']"
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("Ожидание и получение результата")
    def get_result(self) -> str:
        """
        Ждет появления текста '15' в элементе с классом 'screen'.
        """
        # МЕНЯЕМ By.ID "result" НА By.CLASS_NAME "screen"
        self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        return self.driver.find_element(By.CLASS_NAME, "screen").text
