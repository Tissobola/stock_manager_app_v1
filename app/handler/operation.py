import app.service.operation as sr
import app.model.operation as op
from datetime import datetime
from flask import abort

class OperationHandler:
    def getOperation(id: int) -> op.Operation:
        

    def getAllOperations() -> list[op.Operation]:
        

    def createSale(operation: dict) -> bool:
        

    def createPurchase(operation: dict) -> bool:
        

    def deleteOperation(id: int) -> bool:
        

    def updateOperation(operation: dict) -> bool:
        

_inst = OperationHandler
getOperation = _inst.getOperation
getAllOperations = _inst.getAllOperations
createSale = _inst.createSale
createPurchase = _inst.createPurchase
deleteOperation = _inst.deleteOperation
updateOperation = _inst.updateOperation