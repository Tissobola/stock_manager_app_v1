import app.model.product as prod
import app.repository.product as rp
import sqlite3

class ProductService:
    def getProduct(id: int) -> tuple[prod.Product, Exception]:
        return rp.getProduct(id)

    def getAllProducts() -> tuple[list[prod.Product], Exception]:
        return rp.getAllProducts()

    def createProduct(product: prod.Product) -> tuple[bool, Exception]:
        return rp.createProduct(product)

    def deleteProduct(id: int) -> tuple[bool, Exception]:
        return rp.deleteProduct(id)

    def updateProduct(product: prod.Product) -> tuple[bool, Exception]:
        return rp.updateProduct(product)

_inst = ProductService
getProduct = _inst.getProduct
getAllProducts = _inst.getAllProducts
createProduct = _inst.createProduct
deleteProduct = _inst.deleteProduct
updateProduct = _inst.updateProduct