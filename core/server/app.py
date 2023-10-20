from flask import Flask
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
