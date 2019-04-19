import connexion
import datetime
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml')
    application = app.app
    app.run(port=5000, debug=True)
