import app.service.operation as sr
import app.model.operation as op
import app.validator.operation as val
from flask import abort

class OperationHandler:
    def getOperation(id: int) -> dict:
        result, error = sr.getOperation(id)
        if error is not None:
            abort(500, str(error))
        return result

    def getAllOperations() -> list[dict]:
        result, error = sr.getAllOperations()
        if error is not None:
            abort(500, str(error))
        return result

    def createSale(operation: dict) -> str:
        validate, error = val.createSale(operation)
        if not validate:
            abort(404, str(error))
        try:
            operation["operation_id"] = None
            operation["operation_date"] = None
            operation["is_sale"] = None
            if operation["price"] == "":
                operation["price"] = None
            operation = op.Operation(operation, False)
        except Exception as e:
            abort(404, "Invalid Request: "+str(e))
        response, error = sr.createSale(operation)
        if error is not None:
            abort(500, str(error))
        return response

    def createPurchase(operation: dict) -> str:
        validate, error = val.createPurchase(operation)
        if not validate:
            abort(404, str(error))
        try:
            operation["operation_id"] = None
            operation["operation_date"] = None
            operation["is_sale"] = None
            operation = op.Operation(operation, False)
        except Exception as e:
            abort(404, "Invalid Request: "+str(e))
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
            operation = op.Operation(operation, False)
        except:
            abort(404, "Invalid Request")
        response, error = sr.updateOperation(operation)
        if error is not None:
            abort(500, str(error))
        return response

_inst = OperationHandler
getOperation = _inst.getOperation
getAllOperations = _inst.getAllOperations
createSale = _inst.createSale
createPurchase = _inst.createPurchase
deleteOperation = _inst.deleteOperation
updateOperation = _inst.updateOperation