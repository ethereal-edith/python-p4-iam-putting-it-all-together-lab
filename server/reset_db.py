from app import app
from config import db

with app.app_context():
    db.drop_all()
    db.create_all()
    print("✅ Database reset and tables created!")
