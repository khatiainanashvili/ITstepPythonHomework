import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.account = BankAccount("Alice", 1000)

    def tearDown(self):
        print("tearDown")
        del self.account

    def test_initial_balance(self):
        print("test_initial_balance")
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit(self):
        print("test_deposit")
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

        with self.assertRaises(ValueError) as context:
            self.account.deposit(-100)
        self.assertEqual(str(context.exception), "Deposit amount must be positive")

    def test_withdraw(self):
        print("test_withdraw")
        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)

        with self.assertRaises(ValueError) as context:
            self.account.withdraw(1000)
        self.assertEqual(str(context.exception), "Insufficient funds")

    def test_balance_after_multiple_transactions(self):
        print("test_balance_after_multiple_transactions")
        self.account.deposit(500)
        self.account.withdraw(200)
        self.assertEqual(self.account.get_balance(), 1300)










from logics import add, divide, Employee 

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 15), 25)
        self.assertEqual(add(-10, 15), 5)
        self.assertEqual(add(10, -15), -5)
        self.assertEqual(add(-10, -15), -25)
        self.assertEqual(add(0, -15), -15)
        self.assertEqual(add(0, 15), 15)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.employee1 = Employee('John', 'Doe', 2000)

    def tearDown(self):
        print("tearDown")
        del self.employee1

    def test_email(self):
        print("test_email")
        self.assertEqual(self.employee1.email, 'John.Doe@gmail.com')

        self.employee1.first_name = 'Kate'
        self.assertEqual(self.employee1.email, 'Kate.Doe@gmail.com')

    def test_apply_raise(self):
        print("test_apply_raise")
        self.employee1.apply_raise()
        self.assertEqual(self.employee1.salary, 4000)

        self.employee1.apply_raise()
        self.assertEqual(self.employee1.salary, 8000)   


from shoppingCart import ShoppingCart 

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.cart = ShoppingCart()

    def tearDown(self):
        print("tearDown")
        del self.cart

    def test_add_item(self):
        print("test_add_item")
        self.cart.add_item("Apple", 1.0, 3)
        self.cart.add_item("Banana", 0.5, 2)

        self.assertEqual(len(self.cart.items), 2)
        self.assertEqual(self.cart.items[0]['name'], "Apple")
        self.assertEqual(self.cart.items[1]['name'], "Banana")

        with self.assertRaises(ValueError) as context:
            self.cart.add_item("Orange", 1.5, -1)
        self.assertEqual(str(context.exception), "Quantity must be greater than 0")

    def test_total_price(self):
        print("test_total_price")
        self.cart.add_item("Apple", 1.0, 3)
        self.cart.add_item("Banana", 0.5, 2)

        self.assertEqual(self.cart.total_price(), 4.0)

        self.cart.add_item("Orange", 1.5, 1)
        self.assertEqual(self.cart.total_price(), 5.5)

    def test_remove_item(self):
        print("test_remove_item")
        self.cart.add_item("Apple", 1.0, 3)
        self.cart.add_item("Banana", 0.5, 2)

        self.cart.remove_item("Apple")
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]['name'], "Banana")


        self.cart.remove_item("Orange") 
        self.assertEqual(len(self.cart.items), 1)

    def test_is_empty(self):
        print("test_is_empty")
        self.assertTrue(self.cart.is_empty())

        self.cart.add_item("Apple", 1.0, 3)
        self.assertFalse(self.cart.is_empty())





if __name__ == '__main__':
    unittest.main()
