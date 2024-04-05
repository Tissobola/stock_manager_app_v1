import app.model.product as prod
import app.service.product as sr
import json
import sqlite3

class ProductHandler:
    def getProduct(id: int) -> tuple[prod.Product, Exception]:
        

    def getAllProducts() -> tuple[list[prod.Product], Exception]:
        

    def createProduct(product: prod.Product) -> tuple[bool, Exception]:
        

    def deleteProduct(id: int) -> tuple[bool, Exception]:
        

    def updateProduct(product: prod.Product) -> tuple[bool, Exception]:
        

_inst = ProductHandler
getProduct = _inst.getProduct
getAllProducts = _inst.getAllProducts
createProduct = _inst.createProduct
deleteProduct = _inst.deleteProduct
updateProduct = _inst.updateProduct