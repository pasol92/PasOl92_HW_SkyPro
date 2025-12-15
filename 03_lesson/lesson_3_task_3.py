from address import Address
from mailing import Mailing

to_addr = Address("123456", "Москва", "ул. Ленина", "10", "5")
from_addr = Address("654321", "Санкт-Петербург", "Невский пр-т", "20", "12")

package = Mailing(to_addr, from_addr, 350, "TRACK-889900")

print(f"Отправление {package.track} из {package.from_address.index}, "
      f"{package.from_address.city}, {package.from_address.street}, "
      f"{package.from_address.house} - {package.from_address.apartment} "
      f"в {package.to_address.index}, {package.to_address.city}, "
      f"{package.to_address.street}, {package.to_address.house} - "
      f"{package.to_address.apartment}. Cтоимость {package.cost} рублей.")
