import repository.operation as pr
import model.operation as op
from datetime import datetime

class OperationRepository:
    def getOperation(id: int) -> tuple:    # (op.Operation, sqlite3.Error)
        return pr.getOperation(id)

    def getAllOperations() -> tuple:   # ([op.Operation], sqlite3.Error)
        return pr.getAllOperations()

    def createSale(operation: op.Operation) -> tuple:  # (bool, sqlite3.Error)
        operation.is_sale = True
        operation.operation_date = datetime.now()
        return pr.createOperation(operation)

    def createPurchase(operation: op.Operation) -> tuple:  # (bool, sqlite3.Error)
        operation.is_sale = False
        operation.operation_date = datetime.now()
        return pr.createOperation(operation)

    def deleteOperation(id: int) -> tuple:  # (bool, sqlite3.Error)
        return pr.deleteOperation(id)

    def updateOperation(operation: op.Operation) -> tuple:  # (bool, sqlite3.Error)
        return pr.updateOperation(operation)

_inst = OperationRepository
getOperation = _inst.getOperation
getAllOperations = _inst.getAllOperations
createSale = _inst.createSale
createPurchase = _inst.createPurchase
deleteOperation = _inst.deleteOperation
updateOperation = _inst.updateOperation