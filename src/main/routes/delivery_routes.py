from flask import Blueprint, jsonify, request
from ..http_types.http_request import HttpRequest


delivery_routes_bp = Blueprint("delivery_routes", __name__)


@delivery_routes_bp.route("/delivery/order", methods=["POST"])
def registry_order():
    print(request.json)
    http_request = HttpRequest(body=request.json)

    # enviar o http_request para a logica
    # logica ira retornar http_response

    return jsonify({"ola": "mundo"}), 200
