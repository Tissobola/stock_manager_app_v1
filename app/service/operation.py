import app.repository.operation as rp
import app.model.operation as op
from datetime import datetime
import sqlite3

class OperationService:
    def getOperation(id: int) -> tuple[op.Operation, Exception]:     
        return rp.getOperation(id)

    def getAllOperations() -> tuple[list[op.Operation], Exception]:    
        return rp.getAllOperations()

    def createSale(operation: op.Operation) -> tuple[bool, Exception]:   
        operation.is_sale = True
        operation.operation_date = datetime.now()
        return rp.createOperation(operation)

    def createPurchase(operation: op.Operation) -> tuple[bool, Exception]:   
        operation.is_sale = False
        operation.operation_date = datetime.now()
        return rp.createOperation(operation)

    def deleteOperation(id: int) -> tuple[bool, Exception]:   
        return rp.deleteOperation(id)

    def updateOperation(operation: op.Operation) -> tuple[bool, Exception]:   
        return rp.updateOperation(operation)

_inst = OperationService
getOperation = _inst.getOperation
getAllOperations = _inst.getAllOperations
createSale = _inst.createSale
createPurchase = _inst.createPurchase
deleteOperation = _inst.deleteOperation
updateOperation = _inst.updateOperation