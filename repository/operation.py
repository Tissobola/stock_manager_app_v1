import model.operation as op
import repository.db as db
import sqlite3

class OperationRepository:
    def getOperation(id: int) -> tuple:    # (op.Operation, sqlite3.Error)
        try:
            stats = db.execute('''
                SELECT *
                FROM operation
                WHERE operation_id = ?
            ''', [id]).fetchone()   # dict
        except sqlite3.Error as error:
            return (None, error)
        operation = op.Operation(stats)
        return (operation, None)

    def getAllOperations() -> tuple:   # ([op.Operation], sqlite3.Error)
        try:
            operations = db.execute('''
                SELECT *
                FROM operation
                ORDER BY operation_date
            ''').fetchall()
        except sqlite3.Error as error:
            return (None, error)
        result = []
        for operation in operations:
            result.append(op.Operation(operation))
        return (result, None)

    def getAllSales() -> tuple:   # ([op.Operation], sqlite3.Error)
        try:
            operations = db.execute('''
                SELECT *
                FROM operation
                WHERE is_sale = ?
                ORDER BY operation_date
            ''', True).fetchall()
        except sqlite3.Error as error:
            return (None, error)
        result = []
        for operation in operations:
            result.append(op.Operation(operation))
        return (result, None)
    
    def getAllPurchases() -> tuple:   # ([op.Operation], sqlite3.Error)
        try:
            operations = db.execute('''
                SELECT *
                FROM operation
                WHERE is_sale = ?
                ORDER BY operation_date
            ''', False).fetchall()
        except sqlite3.Error as error:
            return (None, error)
        result = []
        for operation in operations:
            result.append(op.Operation(operation))
        return (result, None)

    def createOperation(operation: op.Operation) -> tuple:  # (bool, sqlite3.Error)
        query = '''INSERT INTO operation
             (operation_id, name, price, stock, unit)
             VALUES (?, ?, ?, ?, ?)'''
        try:
            db.execute(query, operation.to_list()).commit()
        except sqlite3.Error as error:
            return (False, error)
        return (True, None)

    def deleteOperation(id: int) -> tuple:  # (bool, sqlite3.Error)
        try:
            db.execute('''DELETE FROM operation
                WHERE operation_id = ?''', [id])
        except sqlite3.Error as error:
            return (False, error)
        return (True, None)

    def updateOperation(operation: op.Operation) -> tuple:  # (bool, sqlite3.Error)
        query = '''UPDATE operation
            SET (product_id, operation_date, unit)
            VALUES (?, ?, ?, ?)
            WHERE operation_id = ?'''
        try:
            db.execute(query, operation.to_list()[1:].append(operation.operation_id)).commit()
        except sqlite3.Error as error:
            return (False, error)
        return (True, None)

_inst = OperationRepository
getOperation = _inst.getOperation
getAllOperations = _inst.getAllOperations
createOperation = _inst.createOperation
deleteOperation = _inst.deleteOperation
updateOperation = _inst.updateOperation