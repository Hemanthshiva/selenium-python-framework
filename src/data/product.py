class Product:
    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price

    @classmethod
    def from_dict(cls, data):
        return cls(name=data['name'], code=data['code'], price=data['price'])


