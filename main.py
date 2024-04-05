import logging
import app.repository.db as db
import logging
from app.server.server import APP

if __name__ == '__main__':
  logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
  db.connect()
  APP.run(host='0.0.0.0', port=9001)