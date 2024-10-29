# დავალება 1.
# შეიმუშავეთ საბანკო ანგარიშის ძირითადი სისტემა. 
# შექმენით კლასი სახელწოდებით BankAccount, ისეთი ატრიბუტებით, როგორიცაა account_number, account_holder და balance.
# აღწერეთ ფულის ჩარიცხვის და გამოტანის მეთოდები. 
# შექმენით რამდენიმე ობიექტი და განახორციელეთ რამდენიმე ტრანზაქცია.



class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} to {self.account_holder}'s account.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount} from {self.account_holder}'s account.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
    
    def get_balance(self):
        return self.balance


account1 = BankAccount("001", "Ana", 1000)
account2 = BankAccount("002", "Nika", 500)
account3 = BankAccount("003", "Giorgi", 300)


account1.deposit(200)        
account2.withdraw(100)        
account3.withdraw(400)       
account1.withdraw(50)        


print(f"Ana's balance: ${account1.get_balance()}")
print(f"Nika's balance: ${account2.get_balance()}")
print(f"Giorgi's balance: ${account3.get_balance()}")



# დავალება 2.
# შექმენით კლასი სახელწოდებით Student ატრიბუტებით, როგორიცაა name, 
# student_id და courses(კურსების სია, რომელშიც სტუდენტი არის ჩარიცხული). 
# აღწერეთ სტუდენტის ინფორმაციის და კურსების ჩვენების მეთოდები. 
# შექმენით რამდენიმე ობიექტი და დაარეგისტრირეთ სხვადასხვა კურსებზე.


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def register_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} has been registered for the course: {course}")
        else:
            print(f"{self.name} is already registered for the course: {course}")
    
    def get_courses(self):
        return self.courses


student1 = Student("Ana", "S001")
student1.register_course("Math")
student1.register_course("Science")
student1.register_course("History")


student1.register_course("Math")

print(f"{student1.name} is registered in the following courses: {student1.get_courses()}")
