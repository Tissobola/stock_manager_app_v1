import model.product as prod
import repository.db as db
import sqlite3

class ProductRepository:
    def getProduct(id: int) -> tuple:    # (prod.Product, sqlite3.Error)
        try:
            stats = db.execute('''
                SELECT *
                FROM product
                WHERE product_id = ?
            ''', [id]).fetchone()   # dict
        except sqlite3.Error as error:
            return (None, error)
        product = prod.Product(stats)
        return (product, None)

    def getAllProducts() -> tuple:   # ([prod.Product], sqlite3.Error)
        try:
            products = db.execute('''
                SELECT *
                FROM product
                ORDER BY operation_date
            ''').fetchall()
        except sqlite3.Error as error:
            return (None, error)
        result = []
        for product in products:
            result.append(prod.Product(product))
        return (result, None)

    def createProduct(product: prod.Product) -> tuple:  # (bool, sqlite3.Error)
        query = '''INSERT INTO product
             (name, price, stock, unit)
             VALUES (?, ?, ?, ?)'''
        try:
            db.execute(query, product.to_list()[1:]).commit()
        except sqlite3.Error as error:
            return (False, error)
        return (True, None)

    def deleteProduct(id: int) -> tuple:  # (bool, sqlite3.Error)
        try:
            db.execute('''DELETE FROM product
                WHERE product_id = ?''', [id])
        except sqlite3.Error as error:
            return (False, error)
        return (True, None)

    def updateProduct(product: prod.Product) -> tuple:  # (bool, sqlite3.Error)
        query = '''UPDATE product
            SET (name, price, stock, unit)
            VALUES (?, ?, ?, ?)
            WHERE product_id = ?'''
        try:
            db.execute(query, product.to_list()[1:].append(product.product_id)).commit()
        except sqlite3.Error as error:
            return (False, error)
        return (True, None)

_inst = ProductRepository
getProduct = _inst.getProduct
getAllProducts = _inst.getAllProducts
createProduct = _inst.createProduct
deleteProduct = _inst.deleteProduct
updateProduct = _inst.updateProduct