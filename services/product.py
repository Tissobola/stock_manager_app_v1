import model.product as prod
import repository.product as rp

class ProductService:
    def getProduct(id: int) -> tuple:    # (prod.Product, sqlite3.Error)
        return rp.getProduct(id)

    def getAllProducts() -> tuple:   # ([prod.Product], sqlite3.Error)
        return rp.getAllProducts()

    def createProduct(product: prod.Product) -> tuple:  # (bool, sqlite3.Error)
        return rp.createProduct(product)

    def deleteProduct(id: int) -> tuple:  # (bool, sqlite3.Error)
        return rp.deleteProduct(id)

    def updateProduct(product: prod.Product) -> tuple:  # (bool, sqlite3.Error)
        return rp.updateProduct(product)

_inst = ProductService
getProduct = _inst.getProduct
getAllProducts = _inst.getAllProducts
createProduct = _inst.createProduct
deleteProduct = _inst.deleteProduct
updateProduct = _inst.updateProduct