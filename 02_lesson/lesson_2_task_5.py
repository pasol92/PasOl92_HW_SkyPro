def month_to_season(month):
    if not isinstance(month, int) or month < 1 or month > 12:
        raise ValueError("Номер месяца должен быть целым числом от 1 до 12")
    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    else:
        return "Осень"


print(f"Месяц 1 - время года: {month_to_season(1)}")
print(f"Месяц 3 - время года: {month_to_season(3)}")
print(f"Месяц 6 - время года: {month_to_season(6)}")
print(f"Месяц 9 - время года: {month_to_season(9)}")
print(f"Месяц 12 - время года: {month_to_season(12)}")
