import logging
import repository.db as db
from flask import Flask
import logging

APP = Flask(__name__)

if __name__ == '__main__':
  logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
  db.connect()
  APP.run(host='0.0.0.0', port=9001)

@APP.route('/')
def index():
  return

@APP.route('/products', methods=['GET'])

@APP.route('/products', methods=['POST'])

@APP.route('/products', methods=['DELETE'])

@APP.route('/products', methods=['PUT'])

@APP.route('/products/<int:id>')

@APP.route('/operations', methods=['GET'])

@APP.route('/operations', methods=['DELETE'])

@APP.route('/operations', methods=['PUT'])

@APP.route('/operations/<int:id>')

@APP.route('/sales')

@APP.route('/sales', methods=['POST'])

@APP.route('/purchase')

@APP.route('/purchase', methods=['POST'])
