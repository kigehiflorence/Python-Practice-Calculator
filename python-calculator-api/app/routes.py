from flask import Blueprint, jsonify, request
from .calculator import Calculator

routes = Blueprint('routes', __name__)

@routes.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    operation = data.get("operation")
    a = data.get("a")
    b = data.get("b", None)

    try:
        calc = Calculator()
        if operation == "add":
            result = calc.add(a, b)
        elif operation == "subtract":
            result = calc.subtract(a, b)
        elif operation == "multiply":
            result = calc.multiply(a, b)
        elif operation == "divide":
            result = calc.divide(a, b)
        elif operation == "power":
            result = calc.power(a, b)
        elif operation == "sqrt":
            result = calc.sqrt(a)
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400
