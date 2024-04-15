import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
from flask import Flask, request, render_template
import app.handler.operation as op_handler
import app.handler.product as prod_handler

APP = Flask(__name__, template_folder='../../templates', static_folder='../../static')

@APP.route('/', methods=['GET'])
def index():
    return render_template('index.html'), 200

@APP.route('/products/', methods=['GET'])
def getAllProducts():
    return render_template('products.html', products = prod_handler.getAllProducts()), 200 

@APP.route('/register/', methods=['GET'])
def registerPage():
    return render_template('register.html'), 200

@APP.route('/register/', methods=['POST'])
def createProduct():
    data = request.get_json()
    return render_template('register.html', stats = prod_handler.createProduct(data)), 200

@APP.route('/products/', methods=['PUT'])
def updateProduct():
    data = request.get_json()
    return render_template('response.html', stats = prod_handler.updateProduct(data)), 200

@APP.route('/products/<int:id>/', methods=['GET'])
def getProduct(id):
    return render_template('product.html', product = prod_handler.getProduct(id)), 200

@APP.route('/products/<int:id>/', methods=['DELETE'])
def deleteProduct(id):
    return render_template('response.html', stats = prod_handler.deleteProduct(id)), 200

@APP.route('/operations/', methods=['GET'])
def getAllOperations():
    return render_template('operations.html', operations = op_handler.getAllOperations()), 200

@APP.route('/operations/', methods=['PUT'])
def updateOperation():
    data = request.get_json()
    return render_template('response.html', stats = op_handler.updateOperation(data)), 200

@APP.route('/operations/<int:id>/', methods=['GET'])
def getOperation(id):
    return render_template('operation.html', operation = op_handler.getOperation(id)), 200

@APP.route('/operations/<int:id>/', methods=['DELETE'])
def deleteOperation(id):
    return render_template('response.html', stats = op_handler.deleteOperation(id)), 200

@APP.route('/sell/', methods=['GET'])
def sellPage():
    return render_template('sell.html', stats = None), 200

@APP.route('/sell/', methods=['POST'])
def createSale():
    data = request.get_json()
    return render_template('sell.html', stats = op_handler.createSale(data)), 200

@APP.route('/buy/', methods=['GET'])
def buyPage():
    return render_template('buy.html', stats = None), 200

@APP.route('/buy/', methods=['POST'])
def createPurchase():
    data = request.get_json()
    return render_template('buy.html', stats = op_handler.createPurchase(data)), 200