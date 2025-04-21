from flask import Flask

from ..routes.delivery_routes import delivery_routes_bp

app = Flask(__name__)
app.register_blueprint(delivery_routes_bp)
