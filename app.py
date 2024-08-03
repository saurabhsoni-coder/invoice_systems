from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage
invoices = []

@app.route('/invoices', methods=['POST'])
def create_invoice():
    data = request.get_json()
    new_invoice = {
        'id': len(invoices) + 1,
        'date': data['date'],
        'items': data['items']
    }
    invoices.append(new_invoice)
    return jsonify({'message': 'Invoice created!'}), 201

@app.route('/invoices', methods=['GET'])
def get_invoices():
    return jsonify(invoices)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
