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

@APP.route('/products/<int:id>/', methods=['GET'])
def getProduct(id):
    return render_template('product.html', product = prod_handler.getProduct(id)), 200

@APP.route('/products/<int:id>/delete/', methods=['GET'])
def deleteProductPage(id):
    return render_template('delete.html', product = prod_handler.getProduct(id)), 200

@APP.route('/products/<int:id>/delete/', methods=['POST'])
def deleteProduct(id):
    return render_template('delete.html', response = prod_handler.deleteProduct(id)), 200    #TODO

@APP.route('/products/<int:id>/edit/', methods=['GET'])
def editProductPage(id):
    return render_template('product_edit.html', product = prod_handler.getProduct(id)), 200

@APP.route('/products/<int:id>/edit/', methods=['POST'])
def updateProduct(id):
    if request.is_json:
        data = request.get_json()
    elif request:
        data = request.form.to_dict()
    data["operation_id"] = id
    response = prod_handler.updateProduct(data)
    return render_template('response.html', response = response), 200   #TODO

@APP.route('/operations/', methods=['GET'])
def getAllOperations():
    return render_template('operations.html', operations = op_handler.getAllOperations()), 200

@APP.route('/operations/<int:id>/', methods=['GET'])
def getOperation(id):
    return render_template('operation.html', operation = op_handler.getOperation(id)), 200

@APP.route('/operations/<int:id>/delete/', methods=['GET'])
def deleteOperationPage(id):
    return render_template('delete.html', operation = op_handler.getOperation(id)), 200    #TODO

@APP.route('/operations/<int:id>/delete/', methods=['POST'])
def deleteOperation(id):
    return render_template('delete.html', response = op_handler.deleteOperation(id)), 200    #TODO

@APP.route('/operations/<int:id>/edit/', methods=['GET'])
def editOperationPage(id):
    return render_template('operation_edit.html', operations = op_handler.getOperation(id)), 200

@APP.route('/operations/<int:id>/edit/', methods=['POST'])
def updateOperation(id):
    if request.is_json:
        data = request.get_json()
    elif request:
        data = request.form.to_dict()
    data["operation_id"] = id
    response = op_handler.updateOperation(data)
    return render_template('response.html', response = response), 200   #TODO

@APP.route('/register/', methods=['GET'])
def registerPage():
    return render_template('register.html', clean = True), 200

@APP.route('/register/', methods=['POST'])
def createProduct():
    if request.is_json:
        data = request.get_json()
    elif request:
        data = request.form.to_dict()
    response = prod_handler.createProduct(data)
    return render_template('register.html', response = response), 200

@APP.route('/sell/', methods=['GET'])
def sellPage():
    return render_template('sell.html', clean = True), 200

@APP.route('/sell/', methods=['POST'])
def createSale():
    if request.is_json:
        data = request.get_json()
    elif request:
        data = request.form.to_dict()
    response = op_handler.createSale(data)
    return render_template('sell.html', response = response), 200

@APP.route('/buy/', methods=['GET'])
def buyPage():
    return render_template('buy.html', clean = True), 200

@APP.route('/buy/', methods=['POST'])
def createPurchase():
    if request.is_json:
        data = request.get_json()
    elif request:
        data = request.form.to_dict()
    response = op_handler.createPurchase(data)
    return render_template('buy.html', response = response), 200