from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize SQLAlchemy instance (to be configured in __init__.py)
db = SQLAlchemy()

class Equipment(db.Model):
    __tablename__ = 'equipment'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # Name of the equipment
    description = db.Column(db.String(250))  # Brief description of the item
    status = db.Column(db.String(50), nullable=False, default='available')  # Status (available or borrowed)
    borrower = db.Column(db.String(100), nullable=True)  # Name of the borrower, if any
    borrowed_date = db.Column(db.DateTime, nullable=True)  # Date the item was borrowed
    return_date = db.Column(db.DateTime, nullable=True)  # Expected return date

    def __init__(self, name, description=None, status='available'):
        self.name = name
        self.description = description
        self.status = status

    def borrow(self, borrower_name, return_date=None):
        """Mark item as borrowed and set borrower and return date."""
        self.status = 'borrowed'
        self.borrower = borrower_name
        self.borrowed_date = datetime.utcnow()
        self.return_date = return_date

    def return_item(self):
        """Mark item as returned and clear borrower information."""
        self.status = 'available'
        self.borrower = None
        self.borrowed_date = None
        self.return_date = None

    def to_dict(self):
        """Convert item information to a dictionary for JSON responses."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'borrower': self.borrower,
            'borrowed_date': self.borrowed_date.isoformat() if self.borrowed_date else None,
            'return_date': self.return_date.isoformat() if self.return_date else None
        }