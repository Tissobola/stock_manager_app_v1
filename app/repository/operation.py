import app.model.operation as op
import app.repository.db as db

class OperationRepository:
    def getOperation(id: int) -> tuple[op.Operation, Exception]:
        try:
            stats = db.execute('''
                SELECT operation_id, o.product_id, operation_date, units, o.price, is_sale, name, unit
                FROM operation o
                JOIN product p
                WHERE operation_id = ?
            ''', [id]).fetchone()   # dict
        except Exception as error:
            return (None, error)
        if stats is None:
            return (None, Exception('Could not find product with id: {}'.format(id)))
        operation = op.Operation(stats, True)
        return (operation, None)

    def getAllOperations() -> tuple[list[op.Operation], Exception]:
        try:
            operations = db.execute('''
                SELECT operation_id, o.product_id, operation_date, units, o.price, is_sale, name, unit
                FROM operation o
                JOIN product p
                WHERE o.product_id = p.product_id
                ORDER BY operation_date
            ''').fetchall() #dict list
        except Exception as error:
            return (None, error)
        if len(operations) == 0:
            return (None, Exception('There are no operations registered'))
        result = []
        for operation in operations:
            result.append(op.Operation(operation, True))
        return (result, None)

    def createOperation(operation: op.Operation) -> tuple[bool, Exception]:
        query = '''INSERT INTO operation
             (product_id, units, price, is_sale, operation_date)
             VALUES (?, ?, ?, ?, ?)'''
        try:
            db.execute(query, operation.to_list()[1:6])
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
        query = '''UPDATE operation SET
            product_id = ?,
            units = ?,
            price = ?,
            is_sale = ?
            WHERE operation_id = ?'''
        try:
            stats = operation.to_list()[1:5]
            stats.append(operation.operation_id)
            db.execute(query, stats)
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