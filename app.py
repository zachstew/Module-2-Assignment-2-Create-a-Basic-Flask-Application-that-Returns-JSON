"""
Small Flask REST API demonstrating Python fundamentals:
  - Functions & control flow (if/else inside route handlers)
  - Data types & structures (JSON -> dicts/lists -> JSON)
  - Error handling (400 for bad input, JSON error responses)
"""

from flask import Flask, jsonify, request

# Create the Flask application object.
app = Flask(__name__)


# ---------------------------------------------------------------
# Route 1: GET /hello?name=Alex
# ---------------------------------------------------------------
@app.route("/hello", methods=["GET"])
def hello():
    # request.args is a dictionary-like object holding query parameters.
    # .get() returns None if "name" wasn't provided (no crash).
    name = request.args.get("name")

    # Control flow: use the name if given, otherwise a default.
    if name:
        message = f"Hello, {name}!"
    else:
        message = "Hello, World!"

    # jsonify turns a Python dictionary into a JSON response.
    return jsonify({"message": message}), 200


# ---------------------------------------------------------------
# Route 2: POST /sum  with body {"numbers": [1, 2, 3]}
# ---------------------------------------------------------------
@app.route("/sum", methods=["POST"])
def sum_numbers():
    # silent=True means: return None on bad/missing JSON instead of crashing.
    data = request.get_json(silent=True)

    # --- Validation (error handling) ---
    # 1. Body must be a JSON object (a dictionary).
    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object."}), 400

    # 2. The "numbers" key must exist.
    if "numbers" not in data:
        return jsonify({"error": "Missing required field: 'numbers'."}), 400

    numbers = data["numbers"]

    # 3. "numbers" must be a non-empty list.
    if not isinstance(numbers, list) or len(numbers) == 0:
        return jsonify({"error": "'numbers' must be a non-empty list."}), 400

    # 4. Every item must be a number. (bool is technically an int in
    #    Python, so we exclude it explicitly.)
    for item in numbers:
        if isinstance(item, bool) or not isinstance(item, (int, float)):
            return jsonify({"error": "All items in 'numbers' must be numbers."}), 400

    # --- Happy path: sum() adds up every value in the list. ---
    total = sum(numbers)
    return jsonify({"sum": total}), 200


# ---------------------------------------------------------------
# Error handlers: make Flask return JSON instead of HTML error pages.
# ---------------------------------------------------------------
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Route not found."}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed for this route."}), 405


# ---------------------------------------------------------------
# Start the server only when this file is run directly
# (python app.py), not when it's imported by the tests.
# ---------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)