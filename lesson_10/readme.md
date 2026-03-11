## Описание
В данном проекте реализованы тесты для калькулятора и онлайн-магазина с использованием паттерна Page Object и генерацией отчетов Allure.

## Инструкция по запуску
1. Установите зависимости:
   `pip install pytest selenium allure-pytest`
2. Запустите тесты для сбора данных Allure:
   `pytest --alluredir=allure-results lesson_10`

## Просмотр отчета
Для генерации визуального отчета выполните:
`allure serve allure-results`