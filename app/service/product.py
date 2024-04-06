import app.model.product as prod
import app.repository.product as rp

class ProductService:
    def getProduct(id: int) -> tuple[prod.Product, Exception]:
        result, error = rp.getProduct(id)
        if error is not None:
            return None, error
        return result.to_dict(), None

    def getAllProducts() -> tuple[list[dict], Exception]:
        response, error = rp.getAllProducts()
        if error is not None:
            return None, error
        try:
            list = []
            for product in response:
                list.append(product.to_dict())
        except Exception as e:
            return None, e
        return list, None

    def createProduct(product: prod.Product) -> tuple[str, Exception]:
        result, error = rp.createProduct(product)
        if error is not None:
            return False, error
        return str(result), None

    def deleteProduct(id: int) -> tuple[str, Exception]:
        result, error = rp.deleteProduct(id)
        if error is not None:
            return False, error
        return str(result), None

    def updateProduct(product: prod.Product) -> tuple[str, Exception]:
        result, error = rp.updateProduct(product)
        if error is not None:
            return False, error
        return str(result), None

_inst = ProductService
getProduct = _inst.getProduct
getAllProducts = _inst.getAllProducts
createProduct = _inst.createProduct
deleteProduct = _inst.deleteProduct
updateProduct = _inst.updateProduct