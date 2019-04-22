import logging
import connexion

#logging at debug level. Need to update to info once launched.
logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    #swagger setup to start rest server.
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml')
    application = app.app
    app.run(port=5000, debug=True)
