import app.service.operation as sr
import app.model.operation as op
from datetime import datetime
import json
import sqlite3

class OperationHandler:
    def getOperation(id: int) -> tuple[op.Operation, Exception]:
        

    def getAllOperations() -> tuple[list[op.Operation], Exception]:
        

    def createSale(operation: op.Operation) -> tuple[bool, Exception]:
        

    def createPurchase(operation: op.Operation) -> tuple[bool, Exception]:
        

    def deleteOperation(id: int) -> tuple[bool, Exception]:
        

    def updateOperation(operation: op.Operation) -> tuple[bool, Exception]:
        

_inst = OperationHandler
getOperation = _inst.getOperation
getAllOperations = _inst.getAllOperations
createSale = _inst.createSale
createPurchase = _inst.createPurchase
deleteOperation = _inst.deleteOperation
updateOperation = _inst.updateOperation