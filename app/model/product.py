class Product:
    def __init__(self, name, price, stock, unit, product_id = None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.unit = unit

    def __init__(self, product_dict: dict):
        self.product_id = int(product_dict.product_id)
        self.name = str(product_dict.name)
        self.price = float(product_dict.price)
        self.stock = int(product_dict.stock)
        self.unit = str(product_dict.unit)
        
    def to_tuple(self):
        return (self.id, self.name, self.price, self.stock, self.unit)
    
    def to_list(self):
        result = []
        for item in self.to_tuple():
            result.append(item)
        return result
    
    def to_dict(self):
        return {
            "product_id" : self.product_id,
            "name" : self.name,
            "price" : self.price,
            "stock" : self.stock,
            "unit" : self.unit
        }
    