import app.model.operation as op
from validator import validate 
from app.validator.error_reader import read

class Validator:
    def getOperation(id: int) -> tuple[bool, Exception]:
        data = {"id" : id}
        rules = {"id" : "required|integer"}
        result, _, error = validate(data, rules, return_info=True)
        return (result, read(error))

    def createOperation(operation: op.Operation) -> tuple[bool, Exception]:
        data = operation
        rules = {"operation_id"     : "",
                 "product_id"       : "required|integer",
                 "operation_date"   : "",
                 "units"            : "required|min:1|integer",
                 "price"            : "",
                 "is_sale"          : ""
                }
        result, _, error = validate(data, rules, return_info=True)
        return (result, read(error))

    def deleteOperation(id: int) -> tuple[bool, Exception]:
        data = {"id" : id}
        rules = {"id" : "required|integer"}
        result, _, error = validate(data, rules, return_info=True)
        return (result, read(error))

    def updateOperation(operation: op.Operation) -> tuple[bool, Exception]:
        data = operation
        rules = {"operation_id"     : "required|integer",
                 "product_id"       : "required|integer",
                 "operation_date"   : "",
                 "units"            : "required|min:1|integer",
                 "price"            : "required|min:0",
                 "is_sale"          : "required|min:0|max:1"
                }
        result, _, error = validate(data, rules, return_info=True)
        return (result, read(error))

_inst = Validator
getOperation = _inst.getOperation
createOperation = _inst.createOperation
deleteOperation = _inst.deleteOperation
updateOperation = _inst.updateOperation