from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 13", "+79123456789"))
catalog.append(Smartphone("Samsung", "Galaxy S21", "+79234567890"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 10", "+79345678901"))
catalog.append(Smartphone("Google", "Pixel 6", "+79456789012"))
catalog.append(Smartphone("Huawei", "P50 Pro", "+79567890123"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
