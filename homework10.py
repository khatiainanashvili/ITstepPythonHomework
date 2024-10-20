# დავალება 1.

# დაწერეთ პითნის ფუნქცია, რომელიც იღებს პარამეტრად ერთი და იგივე ზომის სიას(list) 
# და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები ერთმანეთთან.
# params: [1, 2, 3], ['a', 'b', 'c']
# outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]

def func(par1, par2):
    zipped = list(zip(par1, par2))
    return zipped

print(func([1, 2, 3], ['a', 'b', 'c']))


# დავალება 2.

# დაწერეთ lambda ფუნქცია რომელიც იღებს სიას(list) და აბრუნებს მხოლოდ სიის ლუწ ელემენტებს
# params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [2, 4, 6]

numbers = [1, 2, 3, 4, 5, 6, 7]

even_nums = filter(lambda x: x % 2 == 0, numbers)

print(list(even_nums))


# დავალება 3.

# დაწერეთ lambda ფუნქცია, რომელიც დააბრუნებს მხოლოდ რიცხვის დადებით მნიშვნელობებს, 
# შესამოწმებელი რიცხვები აღწერილი უნდა იყოს ლისტში. გამოიყენეთ filter ფუნქცია functools მოდულიდან

nums2 = [1, 2, -3, 4, 5, -6, 7]

positive_number = filter(lambda x: x >= 0, nums2)

print(list(positive_number))


# დავალება 4.

# დაწერეთ lambda ფუნქცია, რომელიც პასუხად დააბრუნებს სტრინგი არის თუ არა პალინდრომი,
# სტრინგები უნდა იყოს შენახული ლისტში. დაწერეთ filter ფუნქციის გამოყენებით


str = ["gig","akp", "ana", "pov", "aka"]


is_palindrome = filter(lambda x:  x == (x[::-1]), str)

print(list(is_palindrome))

#####ეს ფუნქცია აბრუნებს მარტო იმ სტრინგებს, რომელიც პალინდრომია...######## 
##### და არის თუ არა პალინდრომი ეგ როგორ უნდა დავაბრუნო ვერ გავაკეთე######


# დავალება 5.


# დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს,
# ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError). 
# ფუქნციის დასაწერად გამოიყენეთ lambda და functools-ის reduce მეთოდი.
# params:[1, 2, 3, 4, 5]
# output: 120
from functools import  reduce


arr = [1, 2, 3, 4, 5]
result = lambda a, b: a * b

try:
  multiplay = reduce(result, arr)
 
except Exception as e:
    print(e)
else:
    print(multiplay)




# დავალება 6.

# დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს(ending).
# დააბრუნეთ მხოლოდ ის სიის ელემენტები, რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით.
# გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError)
# params: ['hello', 'world', 'coding', 'nod'], 'ing'
# outputs: ['coding']

par1 = ['hello', 'world', 'coding', 'nod']
par2 = 'ing'

try:
    fact_lambda =  filter(lambda a: a.endswith(par2), par1)

except TypeError as e:
    print(e)
else:
    print(list(fact_lambda))
