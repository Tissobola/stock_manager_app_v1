from flask import Flask, request, abort

APP = Flask(__name__)

@APP.route('/', methods=['GET'])
def index():
    return 200

@APP.route('/products', methods=['GET'])
def getAllProducts():
    print("test")
    return "200", 200

@APP.route('/products', methods=['POST'])
def createProduct():
    data = request.get_json()
    return

@APP.route('/products', methods=['PUT'])
def updateProduct():
    data = request.get_json()
    return

@APP.route('/products/<int:id>', methods=['GET'])
def getProduct(id):
    return

@APP.route('/products/<int:id>', methods=['DELETE'])
def deleteProduct(id):
    return

@APP.route('/operations', methods=['GET'])
def getAllOperations():
    return

@APP.route('/operations', methods=['PUT'])
def updateOperation():
    data = request.get_json()
    return

@APP.route('/operations/<int:id>', methods=['GET'])
def getOperation(id):
    return

@APP.route('/operations/<int:id>', methods=['DELETE'])
def deleteOperation(id):
    return

@APP.route('/sales', methods=['GET'])
def getAllSales():
    return

@APP.route('/sales', methods=['POST'])
def createSale():
    data = request.get_json()
    return

@APP.route('/purchases', methods=['GET'])
def getAllPurchases():
    return

@APP.route('/purchases', methods=['POST'])
def createPurchase():
    data = request.get_json()
    return