from flask import Flask, request, abort
# import app.handler.operation as op_hand
import app.handler.product as prod_handler

APP = Flask(__name__)

@APP.route('/', methods=['GET'])
def index():
    return 200

@APP.route('/products/', methods=['GET'])
def getAllProducts():
    return prod_handler.getAllProducts(), 200 

@APP.route('/products/', methods=['POST'])
def createProduct():
    data = request.get_json()
    return prod_handler.createProduct(data), 200

@APP.route('/products/', methods=['PUT'])
def updateProduct():
    data = request.get_json()
    return prod_handler.updateProduct(data), 200

@APP.route('/products/<int:id>/', methods=['GET'])
def getProduct(id):
    return prod_handler.getProduct(id), 200

@APP.route('/products/<int:id>/', methods=['DELETE'])
def deleteProduct(id):
    return prod_handler.deleteProduct(id), 200

@APP.route('/operations/', methods=['GET'])
def getAllOperations():
    return

@APP.route('/operations/', methods=['PUT'])
def updateOperation():
    data = request.get_json()
    return

@APP.route('/operations/<int:id>/', methods=['GET'])
def getOperation(id):
    return

@APP.route('/operations/<int:id>/', methods=['DELETE'])
def deleteOperation(id):
    return

@APP.route('/sales/', methods=['GET'])
def getAllSales():
    return

@APP.route('/sales/', methods=['POST'])
def createSale():
    data = request.get_json()
    return

@APP.route('/purchases/', methods=['GET'])
def getAllPurchases():
    return

@APP.route('/purchases/', methods=['POST'])
def createPurchase():
    data = request.get_json()
    return