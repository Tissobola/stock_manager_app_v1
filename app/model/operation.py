class Operation:
    def __init__(self, product_id, units, price, operation_id = None, operation_date = None, is_sale = None):
        self.operation_id = operation_id
        self.product_id = product_id
        self.operation_date = operation_date
        self.units = units
        self.price = price
        self.is_sale = is_sale
    
    def __init__(self, operation_dict: dict):
        self.operation_id = operation_dict["operation_id"]
        self.product_id = operation_dict["product_id"]
        self.operation_date = operation_dict["operation_date"] # datetime
        self.units = operation_dict["units"]
        self.price = operation_dict["price"]
        self.is_sale = operation_dict["is_sale"]
        
    def to_tuple(self):
        return (self.operation_id, self.product_id, self.operation_date,
                self.units, self.price, self.is_sale)
    
    def to_list(self):
        result = []
        for item in self.to_tuple():
            result.append(item)
        return result
    
    def to_dict(self):
        return {
            "operation_id" : self.operation_id,
            "product_id" : self.product_id,
            "operation_date" : self.operation_date,
            "units" : self.units,
            "price" : self.price,
            "is_sale" : self.is_sale
        }