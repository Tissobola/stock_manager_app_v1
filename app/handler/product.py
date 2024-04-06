import app.model.product as prod
import app.service.product as sr
import app.validator.product as val
from flask import abort

class ProductHandler:
    def getProduct(id: int) -> dict:
        result, error = sr.getProduct(id)
        if error is not None:
            abort(500, str(error))
        return result

    def getAllProducts() -> list[dict]:
        result, error = sr.getAllProducts()
        if error is not None:
            abort(500, str(error))
        return result

    def createProduct(product: dict) -> bool:
        validate, error = val.createProduct(product)
        if not validate:
            abort(404, str(error))
        try:
            product["product_id"] = None
            product = prod.Product(product)
        except:
            abort(404, "Invalid Request")
        response, error = sr.createProduct(product)
        if error is not None:
            abort(500, str(error))
        return response
        

    def deleteProduct(id: int) -> bool:
        validate, error = val.deleteProduct(id)
        if not validate:
            abort(404, str(error))
        result, error = sr.deleteProduct(id)
        if error is not None:
            abort(500, str(error))
        return result

    def updateProduct(product: dict) -> bool:
        validate, error = val.updateProduct(product)
        if not validate:
            abort(404, str(error))
        try:
            product = prod.Product(product)
        except:
            abort(404, "Invalid Request")
        response, error = sr.createProduct(product)
        if error is not None:
            abort(500, str(error))
        return response

_inst = ProductHandler
getProduct = _inst.getProduct
getAllProducts = _inst.getAllProducts
createProduct = _inst.createProduct
deleteProduct = _inst.deleteProduct
updateProduct = _inst.updateProduct