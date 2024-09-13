from flask import Flask, jsonify, request

app = Flask(__name__)

items = {}

@app.route('/items', methods=['GET'])
def list_items():
    return jsonify(items), 200

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    item_id = len(items) + 1
    item_name = data.get("name", "Unnamed Item")

    items[item_id] = {"id": item_id, "name": item_name}
    return jsonify({"message": f"Item '{item_name}' created successfully!", "item": items[item_id]}), 201

if __name__ == '__main__':
    app.run(port=8000)