import app.model.operation as op
from validator import validate 
from app.validator.error_reader import read

class Validator:
    def getOperation(id: int) -> tuple[bool, Exception]:
        data = {"id" : id}
        rules = {"id" : "required"}
        result, _, error = validate(data, rules, return_info=True)
        return (result, read(error))

    def createOperation(operation: op.Operation) -> tuple[bool, Exception]:
        data = operation.to_dict()
        rules = {"operation_id"     : "",
                 "product_id"       : "required",
                 "operation_date"   : "",
                 "units"            : "required|min:1",
                 "price"            : "required|min:0",
                 "is_sale"          : ""
                }
        result, _, error = validate(data, rules, return_info=True)
        return (result, read(error))

    def deleteOperation(id: int) -> tuple[bool, Exception]:
        data = {"id" : id}
        rules = {"id" : "required"}
        result, _, error = validate(data, rules, return_info=True)
        return (result, read(error))

    def updateOperation(operation: op.Operation) -> tuple[bool, Exception]:
        data = operation.to_dict()
        rules = {"operation_id"     : "required",
                 "product_id"       : "required",
                 "operation_date"   : "",
                 "units"            : "required|min:1",
                 "price"            : "required|min:0",
                 "is_sale"          : ""
                }
        result, _, error = validate(data, rules, return_info=True)
        return (result, read(error))

_inst = Validator
getOperation = _inst.getOperation
createOperation = _inst.createOperation
deleteOperation = _inst.deleteOperation
updateOperation = _inst.updateOperation