import app.service.operation as sr
import app.model.operation as op
import app.validator.operation as val
from flask import abort

class OperationHandler:
    def getOperation(id: int) -> dict:
        result, error = sr.getProduct(id)
        if error is not None:
            abort(500, str(error))
        return result

    def getAllOperations() -> list[dict]:
        result, error = sr.getAllOperations()
        if error is not None:
            abort(500, str(error))
        return result
        
    def getAllSales() -> list[dict]:
        result, error = sr.getAllSales()
        if error is not None:
            abort(500, str(error))
        return result
        
    def getAllPurchases() -> list[dict]:
        result, error = sr.getAllPurchases()
        if error is not None:
            abort(500, str(error))
        return result

    def createSale(operation: dict) -> str:
        validate, error = val.createOperation(operation)
        if not validate:
            abort(404, str(error))
        try:
            operation["operation_id"] = None
            operation["operation_date"] = None
            operation["is_sale"] = None
            try:
                aux = operation["price"]
            except:
                operation["price"] = None
            operation = op.Operation(operation)
        except:
            abort(404, "Invalid Request")
        response, error = sr.createSale(operation)
        if error is not None:
            abort(500, str(error))
        return response

    def createPurchase(operation: dict) -> str:
        validate, error = val.createOperation(operation)
        if not validate:
            abort(404, str(error))
        try:
            operation["operation_id"] = None
            operation["operation_date"] = None
            operation["is_sale"] = None
            operation = op.Operation(operation)
        except:
            abort(404, "Invalid Request")
        response, error = sr.createPurchase(operation)
        if error is not None:
            abort(500, str(error))
        return response

    def deleteOperation(id: int) -> str:
        validate, error = val.deleteOperation(id)
        if not validate:
            abort(404, str(error))
        result, error = sr.deleteOperation(id)
        if error is not None:
            abort(500, str(error))
        return result

    def updateOperation(operation: dict) -> str:
        validate, error = val.updateOperation(operation)
        if not validate:
            abort(404, str(error))
        try:
            operation["operation_date"] = None
            operation = op.Operation(operation)
        except:
            abort(404, "Invalid Request")
        response, error = sr.updateOperation(operation)
        if error is not None:
            abort(500, str(error))
        return response

_inst = OperationHandler
getOperation = _inst.getOperation
getAllOperations = _inst.getAllOperations
getAllSales = _inst.getAllSales
getAllPurchases = _inst.getAllPurchases
createSale = _inst.createSale
createPurchase = _inst.createPurchase
deleteOperation = _inst.deleteOperation
updateOperation = _inst.updateOperation