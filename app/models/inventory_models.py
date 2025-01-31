from ..extensions import db
from datetime import datetime
from sqlalchemy import Enum

class Inventory(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    property_no = db.Column(db.String(255), unique=True, nullable=True)
    date_acquired = db.Column(db.Date, nullable=True)
    cost = db.Column(db.Numeric(10, 2), nullable=False)
    quantity = db.Column(db.Integer, default=0, nullable=False)
    unit = db.Column(db.String(120), nullable=False, default="pcs")  # Changed default to a string
    
    fund_source = db.Column(db.String(255), nullable=True)
    officer = db.Column(db.String(255), nullable=True)
    school = db.Column(db.String(255), nullable=True)
    status = db.Column(Enum("available", "borrowed", "reserved", "damaged", name="inventory_status"), 
                       default="available", nullable=False)
    
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))  # Changed from parent_id
    
    # Relationship to Category
    category = db.relationship('Category', backref=db.backref('inventory_items', lazy=True))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Inventory {self.id}: {self.title}, Quantity: {self.quantity} {self.unit}, Cost: {self.cost}, Status: {self.status}>"
