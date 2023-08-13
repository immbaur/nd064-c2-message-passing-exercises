import json
from flask import Flask, jsonify, request

from .services import retrieve_orders, create_order

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})

@app.route('/api/orders/computers', methods=['POST'])
def create_computer_order():
    # Get request body
    data = request.json
    # Create order
    order = create_order(data)
    # Return response
    return jsonify(order)

@app.route('/api/orders/computers', methods=['GET'])
def get_computer_orders():
    # Retrieve orders
    orders = retrieve_orders()
    # Return response
    return jsonify(orders)

if __name__ == '__main__':
    app.run()
