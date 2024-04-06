from validator import validate
import app.model.product as prod
from app.validator.error_reader import read

class Validator:
    def getProduct(id: int) -> tuple[bool, Exception]:
        data = {"id" : id}
        rules = {"id" : "required|integer"}
        result, _, error = validate(data, rules, return_info=True)
        return (result, read(error))

    def createProduct(product: prod.Product) -> tuple[bool, Exception]:
        data = product
        rules = {"product_id"   : "",
                 "name"         : "required|alpha|min:1",
                 "price"        : "required|min:0",
                 "stock"        : "integer",
                 "unit"         : "required|alpha|min:1"
                }
        result, _, error = validate(data, rules, return_info=True)
        return (result, read(error))

    def deleteProduct(id: int) -> tuple[bool, Exception]:
        data = {"id" : id}
        rules = {"id" : "required"}
        result, _, error = validate(data, rules, return_info=True)
        return (result, read(error))

    def updateProduct(product: prod.Product) -> tuple[bool, Exception]:
        data = product
        rules = {"product_id"   : "required|integer",
                 "name"         : "required",
                 "price"        : "required|min:0",
                 "stock"        : "",
                 "unit"         : "required"
                }
        result, _, error = validate(data, rules, return_info=True)
        return (result, read(error))

_inst = Validator
getProduct = _inst.getProduct
createProduct = _inst.createProduct
deleteProduct = _inst.deleteProduct
updateProduct = _inst.updateProduct