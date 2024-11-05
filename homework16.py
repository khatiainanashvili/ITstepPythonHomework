# დავალება 1.

# დაწერეთ ფუნქცია, რომელიც უბრალოდ აბრუნებს არგუმენტად გადაწოდებულ რიცხვს,
# დაუწერეთ დეკორატორი, რომელიც შეამოწმებს, რომ რიცხვი უნდა იყოს დადებითი, 
# თუ არის უარყოფითი ამ შემთხვევაში დააბრუნეთ ValueError შესაბამისი ტექსტით, სხვა შემთხვევაში აამოქმედეთ ფუნქცია, 
# შედეგი კი დაბეჭდეთ დეკორატორიდან.

def check_positive(func):

    def wrapper(number):
        if number < 0:
            print("Error: The number is negative.")
            raise ValueError("The number must be positive.")
        return func(number)
    return wrapper

@check_positive
def return_number(number):
    return number

try:
    print(return_number(-10))  
except ValueError as err:
    print(f"Caught an error: {err}")


# დავალება 2.

# დაწერეთ პირველი დავალება ფუნქტორის გამოყენებით

class PositiveNumber:
    def __call__(self, number):
        if number < 0:
            print("Error: The number is negative.")
            raise ValueError("The number must be positive.")
        return number

try:
    positive_number = PositiveNumber()
    print(positive_number(-10))
except ValueError as err:
    print(f"Caught an error: {err}")


# დავალება 3.

# დაწერეთ დეკორატორი, რომელიც გამოთვლის ფუნქციის მოქმედების დროს და დაბეჭდავს ტერმინალში. 
# დროის აღსაქმელად გამოიყენეთ time.time()




# დავალება 4.
# შექმენით მეტაკლასი LoggingMeta,
# რომელიც ყოველი კლასის შექმნის დროს დაბეჭდავს თუ რა სახელის მქონე კლასი იქმნება და რა მეთოდები გააჩნია მას.

