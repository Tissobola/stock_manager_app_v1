class Operation:
    def __init__(self, operation_dict: dict, complete: bool):
        self.operation_id = operation_dict["operation_id"]
        self.product_id = operation_dict["product_id"]
        self.operation_date = operation_dict["operation_date"] # datetime
        self.units = operation_dict["units"]
        self.price = float(operation_dict["price"])
        self.is_sale = bool(operation_dict["is_sale"])
        if complete:
            self.name = operation_dict["name"]
            self.unit = operation_dict["unit"]
        else:
            self.name = None
            self.unit = None

    def to_list(self):
        return [self.operation_id, self.product_id, self.units, self.price, self.is_sale, self.operation_date, self.name, self.unit]

    def to_dict(self):
        return {
            "operation_id" : self.operation_id,
            "product_id" : self.product_id,
            "operation_date" : self.operation_date,
            "units" : self.units,
            "price" : self.price,
            "is_sale" : self.is_sale,
            "name" : self.name,
            "unit" : self.unit
        }