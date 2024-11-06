from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///inventory.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database instance
db = SQLAlchemy(app)

# Import the Equipment model (assuming it's in a separate file)
from inventory_model import db, Equipment  # Import db and model from inventory_model.py

db.init_app(app)


# Route to render the inventory HTML page
@app.route('/')
def show_inventory():
    return render_template('inventory.html')


# API endpoint to get all equipment items
@app.route('/api/equipment', methods=['GET'])
def get_inventory():
    items = Equipment.query.all()
    return jsonify([item.to_dict() for item in items])


# API endpoint to borrow an item
@app.route('/api/equipment/<int:item_id>/borrow', methods=['POST'])
def borrow_item(item_id):
    item = Equipment.query.get(item_id)
    if item and item.status == 'available':
        borrower_name = request.json.get('borrower')
        return_date = request.json.get('return_date')
        item.borrow(borrower_name, return_date)
        db.session.commit()
        return jsonify(item.to_dict()), 200
    return jsonify({"error": "Item not available or does not exist"}), 400


# API endpoint to return an item
@app.route('/api/equipment/<int:item_id>/return', methods=['POST'])
def return_item(item_id):
    item = Equipment.query.get(item_id)
    if item and item.status == 'borrowed':
        item.return_item()
        db.session.commit()
        return jsonify(item.to_dict()), 200
    return jsonify({"error": "Item not currently borrowed"}), 400


# Initialize database and create tables
@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
