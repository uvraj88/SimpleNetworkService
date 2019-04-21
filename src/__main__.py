import logging
import connexion

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml')
    application = app.app
    app.run(port=5003, debug=True)
