from flask import Flask
from flask_cors import CORS
from routes import routes

app = Flask(__name__)
CORS(app, support_credentials=True)

app.register_blueprint(routes, url_prefix='/api/v1')
if __name__ == '__main__':
   app.run()
