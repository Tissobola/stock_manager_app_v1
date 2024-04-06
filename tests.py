from validator import validate
import sqlite3
import app.repository.db as db
import app.validator.error_reader as error_reader

x = {1: 3}
print(x[3])

# data = {
#     "id" : 1
# }
# rules = {
#     "id" : "min:2|required"
# }
# result, data, error = validate(data, rules, return_info=True)
# print(result)
# print(data)
# print(error_reader.read(error))
# print()
# print(' '.join(sqlite3.DatabaseError.args))
# try:
#     query = '''INSERT INTO operation
#              (operation_id, name, price, stock, unit)
#              VALUES (?, ?, ?, ?, ?)'''
#     db.execute(query, ()).commit()
# except Exception as e:
#     print(e)
# Exception.