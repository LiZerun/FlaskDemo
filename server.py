from flask import Flask, request, jsonify
import random

app = Flask(__name__)

users = {}

@app.route("/user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    name = data.get("name")
    age = data.get("age")
    
    if name is None or age is None:
        return jsonify({"error": "Invalid input"}), 400
    
    users[user_id] = {"name": name, "age": age}
    return jsonify({"message": "User updated successfully"})

@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    else:
        return jsonify(user)

@app.route("/random_number", methods=["POST"])
def random_number():
    data = request.json
    min_value = data.get("min", 0)
    max_value = data.get("max", 100)
    
    random_num = random.randint(min_value, max_value)
    return jsonify({"random_number": random_num})

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    operation = data.get("operation")
    num1 = data.get("num1")
    num2 = data.get("num2")
    
    if num1 is None or num2 is None or operation is None:
        return jsonify({"error": "Invalid input"}), 400
    
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        else:
            result = num1 / num2
    
    return jsonify({"result": result})
            
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)