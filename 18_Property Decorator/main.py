class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        del self._price

if __name__ == "__main__":
    p = Product(100)
    print(p.price)      
    p.price = 150
    print(p.price)      
    del p.price
