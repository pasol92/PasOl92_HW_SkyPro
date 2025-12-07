import math


def square(side):
    area = side * side
    if not isinstance(side, int) and side != int(side):
        area = math.ceil(area)
    return area


print(f"Сторона 4, площадь: {square(4)}")
print(f"Сторона 2.7, площадь: {square(2.7)}")
print(f"Сторона 6.6, площадь: {square(6.6)}")
print(f"Сторона 7.0, площадь: {square(7.0)}")
