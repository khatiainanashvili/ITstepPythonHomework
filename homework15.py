# აღწერეთ ორი კლასი შემდეგი მონაცემების მიხედვით:

# Person:
# name
# deposit (default value = 1000, მიუთითებს ამჟამად რამდენი აქვს დეპოზიტზე)
# loan (default value = 0, მიუთითებს ამჟამად რამდენი აქვს სესხი აღებული)

# House:
# ID – ბინის საკატასტრო კოდი
# price – ბინის ფასი
# owner – სახლის მეპატრონე (Person ტიპის ობიექტი)
# status – ახალი ბინის დამატებისას სტატუსი არის ყოველთვის “გასაყიდი”

# გაითვალისწინეთ owner-ის მნიშვნელობა არის Person კლასის ობიექტი
# Person კლასში დაამატეთ __str__ მეთოდი რომელიც დააბრუნებს პიროვნების სრულ ინფორმაციას

# შექმენით ორი Person კლასის ობიექტი(მაგალითად ერთი მეპატრონე, მეორე მყიდველი). 
# ასევე შექმენით House კლასის ობიექტი რომლის owner იქნება ერთ-ერთი Person ობიექტი
# House კლასში დაამატეთ ბინის გაყიდვის მეთოდი, რომლის დროსაც პარამეტრებად გადაეცემა მყიდველი, 
# თუ მეტი პარამეტრი არ გადაეცემა, ამ დროს უნდა შესრულდეს ბინის გაყიდვის ოპერაცია(გამყიდველის deposit უნდა გაიზარდოს ბინის ღირებულებით,

######  "თუ მეტი პარამეტრი არ გადაეცემა" ეს ვერ გავიგე რას ნიშნავს #####


# უნდა შეიცვალოს owner და status უნდა გახდეს “გაყიდული”, დაბეჭდეთ შესაბამისი ტექსტი). 
# თუ ამ მეთოდის გამოძახების დროს მყიდველის გარდა პარამეტრად გადაეცა კიდევ ერთი რიცხვი, 
# მაშინ შესრულდეს ბინის სესხით გაყიდვის ოპერაცია, სადაც პარამეტრად გადაცემული რიცხვი მიუთითებს მყიდველის მიერ აღებული სესხის რაოდენობას,
# მეთოდმა კი უნდა შეასრულოს შემდეგი ოპერაციები: გამყიდველის deposit უნდა გაიზარდოს ბინის ღირებულებით,
# owner უნდა შეიცვალოს, status გახდეს “გაყიდული სესხით”,
# მყიდველის სესხი (loan) უნდა გაიზარდოს შესაბამისი რაოდენობით და დაიბეჭდოს გაყიდვის შესაბამისი შეტყობინება.
# კლასის გარეთ მოახდინეთ აღწერილი ფუნქციების გამოძახება


class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Person(name={self.name}, deposit={self.deposit}, loan={self.loan})"


class House:
    def __init__(self, ID, price, owner, status='For Sale'):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status
        self.buyers = []

    def __str__(self):
        return f"House(id={self.ID}, price={self.price}, owner={self.owner.name}, status={self.status})"
    
    def sell(self, buyer):
        if buyer.deposit >= self.price:

            self.owner.deposit += self.price
            buyer.deposit -= self.price
            self.owner = buyer
            self.status = "Sold"
            self.buyers.append(buyer)
            return f"House sold to {buyer.name}"
        else:
            return "Buyer does not have enough funds to complete the purchase."


owner1 = Person('Ian', 50000, 0)
buyer1 = Person('Frank', 1500000, 0)

house1 = House(123, 100000, owner1)

print(house1) 
print(house1.sell(buyer1))
print(house1) 
print(owner1) 
print(buyer1) 