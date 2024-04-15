class Product:
    def __init__(self, product_dict: dict):
        self.product_id = product_dict["product_id"]
        self.name = str(product_dict["name"])
        self.price = float(product_dict["price"])
        self.stock = int(product_dict["stock"])
        self.unit = str(product_dict["unit"])
    
    def to_list(self):
        return [self.product_id, self.name, self.price, self.stock, self.unit]
    
    def to_dict(self):
        return {
            "product_id" : self.product_id,
            "name" : self.name,
            "price" : self.price,
            "stock" : self.stock,
            "unit" : self.unit
        }
    