import app.repository.operation as op_rp
import app.service.product as prod_sr
import app.model.operation as op
import app.model.product as prod
from datetime import datetime

class OperationService:
    def getOperation(id: int) -> tuple[dict, Exception]:
        result, error = op_rp.getOperation(id)
        if error is not None:
            return None, error
        return result.to_dict(), None

    def getAllOperations() -> tuple[list[dict], Exception]:
        response, error = op_rp.getAllOperations()
        if error is not None:
            return None, error
        try:
            list = []
            for operation in response:
                list.append(operation.to_dict())
        except Exception as e:
            return None, e
        return list, None

    def createSale(sale: op.Operation) -> tuple[str, Exception]:
        product, _ = prod_sr.getProduct(sale.product_id)
        if product is None:
            return str(False), Exception("Product not found")
        
        product = prod.Product(product)

        if product.stock - sale.units < 0:
            return str(False), Exception("Insuficient stock")

        if sale.price is None:
            sale.price = product.price * sale.units
        sale.is_sale = True
        sale.operation_date = datetime.now()
        product.stock -= sale.units
        
        result, error = op_rp.createOperation(sale)
        if error is not None:
            return str(False), error
        
        _, error = prod_sr.updateProduct(product)
        if error is not None:
            return str(False), error
        return str(result), None

    def createPurchase(purchase: op.Operation) -> tuple[str, Exception]:
        product, _ = prod_sr.getProduct(purchase.product_id)
        if product is None:
            return str(False), Exception("Product not found")
        
        product = prod.Product(product)

        if purchase.price is None:
            purchase.price = product.price * purchase.units
        purchase.is_sale = False
        purchase.operation_date = datetime.now()
        product.stock += purchase.units
        
        
        result, error = op_rp.createOperation(purchase)
        if error is not None:
            return str(False), error
        
        _, error = prod_sr.updateProduct(product)
        if error is not None:
            return str(False), error
        return str(result), None

    def deleteOperation(id: int) -> tuple[str, Exception]:
        operation, error = getOperation(id)
        operation = op.Operation(operation, False)
        if operation is None:
            return str(True), None
        if error is not None:
            return str(False), error
        product, _ = prod_sr.getProduct(operation.product_id)
        if product is None:
            return str(False), Exception("Product not found")
        product = prod.Product(product)
        if operation.is_sale:
            product.stock += operation.units
        else:
            product.stock -= operation.units
        _, error = prod_sr.updateProduct(product)
        if error is not None:
            return str(False), error
        result, error = op_rp.deleteOperation(id)
        if error is not None:
            return str(False), error
        return str(result), None

    def updateOperation(operation: op.Operation) -> tuple[str, Exception]:
        old_operation, error = getOperation(operation.operation_id)
        old_operation = op.Operation(old_operation, False)
        if old_operation is None:
            return str(True), None
        if error is not None:
            return str(False), error
        
        old_product, _ = prod_sr.getProduct(old_operation.product_id)
        if old_product is None:
            return str(False), Exception("Product not found")
        
        old_product = prod.Product(old_product)
        if old_operation.is_sale:
            old_product.stock += old_operation.units
        else:
            old_product.stock -= old_operation.units
        _, error = prod_sr.updateProduct(old_product)
        if error is not None:
            return str(False), error
        
        new_product, _ = prod_sr.getProduct(operation.product_id)
        if new_product is None:
            return str(False), Exception("Product not found")
        
        new_product = prod.Product(new_product)
        if operation.is_sale:
            new_product.stock -= operation.units
        else:
            new_product.stock += operation.units
        _, error = prod_sr.updateProduct(new_product)
        if error is not None:
            return str(False), error
        
        result, error = op_rp.updateOperation(operation)
        if error is not None:
            return str(False), error
        return str(result), None

_inst = OperationService
getOperation = _inst.getOperation
getAllOperations = _inst.getAllOperations
createSale = _inst.createSale
createPurchase = _inst.createPurchase
deleteOperation = _inst.deleteOperation
updateOperation = _inst.updateOperation