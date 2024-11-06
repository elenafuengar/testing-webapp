from flask import Blueprint, request, jsonify
from .inventory_model import db, Equipment

bp = Blueprint('main', __name__)

@bp.route('/api/equipment', methods=['GET'])
def list_equipment():
    items = Equipment.query.all()
    return jsonify([item.to_dict() for item in items])

@bp.route('/api/equipment/<int:id>/borrow', methods=['POST'])
def borrow_equipment(id):
    item = Equipment.query.get(id)
    if item and item.status == 'available':
        item.status = 'borrowed'
        item.borrower = request.json.get('borrower')
        db.session.commit()
        return jsonify(item.to_dict())
    return {"error": "Item not available"}, 400