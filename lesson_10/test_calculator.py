import allure
from .calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.title("Проверка работы калькулятора с задержкой")
@allure.description("Проверяем сумму 7 + 8 с установленной задержкой 45 секунд.")
@allure.severity(allure.severity_level.NORMAL)
def test_calculator(driver):
    page = CalculatorPage(driver)

    with allure.step("Открытие сайта и настройка"):
        page.open()
        page.set_delay(45)

    with allure.step("Ввод математического выражения"):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Проверка итогового значения"):
        result = page.get_result()
        assert result == "15"
