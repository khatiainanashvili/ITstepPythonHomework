from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Base, Product, CartItem, Order, OrderItem

engine = create_engine('sqlite:///ecommerce.db')
Session = sessionmaker(bind=engine)
session = Session()

def add_sample_products():
    sample_products = [
        Product(name='Laptop', price=1500.0, quantity_in_stock=10),
        Product(name='Phone', price=800.0, quantity_in_stock=20),
        Product(name='Headphones', price=200.0, quantity_in_stock=30)
    ]

    session.add_all(sample_products)
    session.commit()

if not inspect(engine).has_table('products'):
    Base.metadata.create_all(engine)
    add_sample_products()
