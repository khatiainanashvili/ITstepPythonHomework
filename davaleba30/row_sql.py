from orm import session
from models import Product, CartItem, Order, OrderItem
from datetime import datetime

def view_cart():
    items = session.query(CartItem).all()
    if not items:
        print("Your cart is empty.")
    else:
        for item in items:
            product = item.product
            print(f"{product.name} - {item.quantity} units @ ${product.price} each")

def add_to_cart(product_id, quantity):
    product = session.query(Product).get(product_id)
    if not product or product.quantity_in_stock < quantity:
        print("Product unavailable or insufficient stock.")
        return

    cart_item = session.query(CartItem).filter_by(product_id=product_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(product_id=product_id, quantity=quantity)
        session.add(cart_item)

    product.quantity_in_stock -= quantity
    session.commit()
    print(f"Added {quantity} of {product.name} to cart.")

def remove_from_cart(product_id):
    cart_item = session.query(CartItem).filter_by(product_id=product_id).first()
    if not cart_item:
        print("Item not in cart.")
        return

    product = cart_item.product
    product.quantity_in_stock += cart_item.quantity
    session.delete(cart_item)
    session.commit()
    print(f"Removed {product.name} from cart.")

def place_order():
    cart_items = session.query(CartItem).all()
    if not cart_items:
        print("Cart is empty.")
        return

    total_amount = sum(item.quantity * item.product.price for item in cart_items)
    order = Order(order_date=datetime.now(), total_amount=total_amount)
    session.add(order)
    session.flush()

    for item in cart_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price_per_item=item.product.price
        )
        session.add(order_item)

    session.query(CartItem).delete()
    session.commit()
    print(f"Order placed successfully! Total amount: ${total_amount}")

def view_orders():
    orders = session.query(Order).all()
    if not orders:
        print("No orders found.")
    else:
        for order in orders:
            print(f"Order ID: {order.id}, Date: {order.order_date}, Total: ${order.total_amount}")

# User interface loop
def user_interface():
    while True:
        print("\nChoose an action:")
        print("1. View Cart")
        print("2. Add Product to Cart")
        print("3. Remove Product from Cart")
        print("4. Place Order")
        print("5. View Orders")
        print("6. Exit")

        choice = input("En1ter your choice: ")

        if choice == "1":
            view_cart()
        elif choice == "2":
            product_id = int(input("Enter Product ID: "))
            quantity = int(input("Enter Quantity: "))
            add_to_cart(product_id, quantity)
        elif choice == "3":
            product_id = int(input("Enter Product ID: "))
            remove_from_cart(product_id)
        elif choice == "4":
            place_order()
        elif choice == "5":
            view_orders()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    user_interface()
