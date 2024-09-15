# დავალება 1.

# დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ 
# შეყვანილი რიცხვის ლუწობასა და კენტობას. თუ რიცხვი ლუწია გამოიტანეთ ტექსტი ‘even’ თუ კენტია ‘odd’


number = int(input('Enter the number... '))

if number % 2 == 0:
    print("even")
else:
    print("odd")

# დავალება 2.

# დაწერეთ პროგრამა რომელიც მომხმარებლის მიერ შეყვანილ ტექსტში მოძებნის სიტყვებს “small”, “tall”, “middle”
# a. თუ ტექსტში აღმოჩნდება რომელიმე მათგანი, დაბეჭდეთ სიტყვა
# b. თუ ტექსტში არცერთი სიტყვა მოიძებნა დაბეჭდეთ, რომ ტექსტში ეს სამი სიტყვა არ მოიძებნა

txt = input("enter something... ")

if "small" in txt :
    print('there is the word "small" ')
elif "tall" in txt: 
    print('there is the word "tall" ')
elif "middle" in txt: 
    print('there is the word "middle" ')
else:
    print('there is not such a word "small", "tall" or "middle" ')



# დავალება 3.
# დაწერეთ კალკულატორი, რომელიც შეგვეკითხება პირველ რიცხვს, შემდეგ მეორე რიცხვს,
# შემდეგ მათემატიკურ ოპერატორს და შესაბამისი მათემატიკური ოპერატორის გამოყენებით დაგვიბეჭდავს შედეგს.

num1 = int(input("enter first number... "))

num2= int(input("enter second number... "))

operation = input("enter operation... ")

if operation == "+" :
    print(f"{num1} + {num2} = ", num1 + num2)
elif operation == "-":
    print(f"{num1} - {num2} = ", num1 - num2)
elif operation == "/":
    print(f"{num1} / {num2} = ", num1 / num2)
elif operation == "*":
    print(f"{num1} * {num2} = ", num1 * num2)
elif operation == "**":
    print(f"{num1} ** {num2} = ", num1 ** num2)
elif operation == "//":
    print(f"{num1} // {num2} = ", num1 // num2)
elif operation == "%":
    print(f"{num1} % {num2} = ", num1 % num2)
