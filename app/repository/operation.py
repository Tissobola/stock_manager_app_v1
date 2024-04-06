import app.model.operation as op
import app.repository.db as db

class OperationRepository:
    def getOperation(id: int) -> tuple[op.Operation, Exception]:
        try:
            stats = db.execute('''
                SELECT *
                FROM operation
                WHERE operation_id = ?
            ''', [id]).fetchone()   # dict
        except Exception as error:
            return (None, error)
        operation = op.Operation(stats)
        return (operation, None)

    def getAllOperations() -> tuple[list[op.Operation], Exception]:
        try:
            operations = db.execute('''
                SELECT *
                FROM operation
                ORDER BY operation_date
            ''').fetchall()
        except Exception as error:
            return (None, error)
        result = []
        for operation in operations:
            result.append(op.Operation(operation))
        return (result, None)

    def getAllSales() -> tuple[list[op.Operation], Exception]:
        try:
            operations = db.execute('''
                SELECT *
                FROM operation
                WHERE is_sale = ?
                ORDER BY operation_date
            ''', True).fetchall()
        except Exception as error:
            return (None, error)
        result = []
        for operation in operations:
            result.append(op.Operation(operation))
        return (result, None)
    
    def getAllPurchases() -> tuple[list[op.Operation], Exception]:
        try:
            operations = db.execute('''
                SELECT *
                FROM operation
                WHERE is_sale = ?
                ORDER BY operation_date
            ''', False).fetchall()
        except Exception as error:
            return (None, error)
        result = []
        for operation in operations:
            result.append(op.Operation(operation))
        return (result, None)

    def createOperation(operation: op.Operation) -> tuple[bool, Exception]:
        query = '''INSERT INTO operation
             (operation_id, name, price, stock, unit)
             VALUES (?, ?, ?, ?, ?)'''
        try:
            db.execute(query, operation.to_list()).commit()
        except Exception as error:
            db.rollback()
            return (False, error)
        db.commit()
        return (True, None)

    def deleteOperation(id: int) -> tuple[bool, Exception]:
        try:
            db.execute('''DELETE FROM operation
                WHERE operation_id = ?''', [id])
        except Exception as error:
            db.rollback()
            return (False, error)
        db.commit()
        return (True, None)

    def updateOperation(operation: op.Operation) -> tuple[bool, Exception]:
        query = '''UPDATE operation
            SET (product_id, operation_date, unit)
            VALUES (?, ?, ?, ?)
            WHERE operation_id = ?'''
        try:
            db.execute(query, operation.to_list()[1:].append(operation.operation_id)).commit()
        except Exception as error:
            db.rollback()
            return (False, error)
        db.commit()
        return (True, None)

_inst = OperationRepository
getOperation = _inst.getOperation
getAllOperations = _inst.getAllOperations
createOperation = _inst.createOperation
deleteOperation = _inst.deleteOperation
updateOperation = _inst.updateOperation