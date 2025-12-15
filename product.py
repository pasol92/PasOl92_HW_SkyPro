class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getProductInfo(self):
        return f"Продукт {self.name} стоит {self.price}"
