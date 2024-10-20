# დავალება 1.

# დაწერეთ პითონის პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს წინადადება, 
# პროგრამას დააბეჭდინეთ დიქტის სახით რამდენჯერ არის თითოეული სიტყვა გამოყენებული წინადადებაში
# input: The wind howled and howled all night long
# output: {“the”: 1, “wind”:1, “howled”:2, “and”:1, “all”:1, ”night”:1, “long”:1


sentence = input("Enter your sentence... ")
arr = sentence.split()
arr2 = []


for i in arr:  
    count = arr.count(i)  
    arr2.append(count)

key = set(arr)
value = set(arr2)
word_count_dict = dict(zip(key, value))  

print(word_count_dict) 



# დავალება 2.
# დაწერეთ პითონის პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს ორი რიცხვი და ერთი მათემატიკური ოპერატორი, ააწყვეთ კალკულატორი,
# რომელიც გამოთვლის შესაბამის მოქმედებას, გამოიყენეთ დიქტები, სადაც key მნიშვნელობებად იქნება მათემატიკური ოპერატორები

num1 = int(input("enter first number... "))
num2= int(input("enter second number... "))
operation = input("enter operation... ")

operation_dict = {
 "plus": "+",
 "minus": "-",
 "division": "/",
 "multiply": "*",
 "square": "**"
}

########     აქ ვერაფერი ვერ გავიგე რაში მჭირდება და როგორ გამოვიყენო dictionary     #######

# დავალება 3.
# comperhension-ის გამოყენებით დააგენერირეთ დიქტი, 
# რომლის key მნიშვნელობები იქნება 1-დან 10-ის ჩათვლით რიცხვები, ხოლო value მათი კვადრატი

squares_dict = {num: num ** 2 for num in range(1, 11)}

print(squares_dict)

# დავალება 4.
# შექმენით დიქტი, რომელიც ინახავს ინფორმაციას დეპარტამენტების და თანამშრომლების შესახებ, 
# თითოეულ თანამშრომელს უნდა ჰქონდეს ატრიბუტები: სახელი, გვარი, ასაკი, ხელფასი. 
# გამოთვალეთ საშუალო ხელფასი დეპარტამენტების მიხედვით.



company = {
    "it_department": {
        "employe1": {
            "name": "natia",
            "surmane": "gavasheli",
            "age": 25,
            "salary": 3000
        },
        'employe2': {
            "name": "gela",
            "surmane": "gavasheli",
            "age": 28,
            "salary": 5000
        },
    },
    "marketing_department": {
        "employe1": {
            "name": "valeri",
            "surmane": "natsvlishvili",
            "age": 25,
            "salary": 2000
        },
        'employe2': {
            "name": "iremi",
            "surmane": "natsvlishvili",
            "age": 28,
            "salary": 5000
        },
    }
}

full_salary = 0

for key, value in company.items():
    for key2, value2 in value.items():
        full_salary += value2["salary"]

print(f"Total salary sum: {full_salary}")
