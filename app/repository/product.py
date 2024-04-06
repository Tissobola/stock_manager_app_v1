import app.model.product as prod
import app.repository.db as db

class ProductRepository:
    def getProduct(id: int) -> tuple[prod.Product, Exception]:
        try:
            stats = db.execute('''
                SELECT *
                FROM product
                WHERE product_id = ?
            ''', [id]).fetchone()   # dict
        except Exception as error:
            return (None, error)
        if stats is None:
            return (None, Exception('Could not find product with id: {}'.format(id)))
        product = prod.Product(stats)
        return (product, None)

    def getAllProducts() -> tuple[list[prod.Product], Exception]:
        try:
            products = db.execute('''
                SELECT *
                FROM product
                ORDER BY product_id
            ''').fetchall()
        except Exception as error:
            return (None, error)
        if len(products) == 0:
            return (None, Exception('There are no products registered'))
        result = []
        for product in products:
            result.append(prod.Product(product))
        return (result, None)

    def createProduct(product: prod.Product) -> tuple[bool, Exception]:
        query = '''INSERT INTO product
            (name, price, stock, unit)
            VALUES (?, ?, ?, ?)'''
        try:
            db.execute(query, product.to_list()[1:])
        except Exception as error:
            db.rollback()
            return (False, error)
        db.commit()
        return (True, None)

    def deleteProduct(id: int) -> tuple[bool, Exception]:
        try:
            db.execute('''DELETE FROM product
                WHERE product_id = ?''', [id])
        except Exception as error:
            db.rollback()
            return (False, error)
        db.commit()
        return (True, None)

    def updateProduct(product: prod.Product) -> tuple[bool, Exception]:
        query = '''UPDATE product
            SET (name, price, stock, unit)
            VALUES (?, ?, ?, ?)
            WHERE product_id = ?'''
        try:
            db.execute(query, product.to_list()[1:].append(product.product_id))
        except Exception as error:
            db.rollback()
            return (False, error)
        db.commit()
        return (True, None)

_inst = ProductRepository
getProduct = _inst.getProduct
getAllProducts = _inst.getAllProducts
createProduct = _inst.createProduct
deleteProduct = _inst.deleteProduct
updateProduct = _inst.updateProduct