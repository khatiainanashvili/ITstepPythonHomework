# დავალება 1.

# დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრინგს და შეამოწმებს არის თუ არა სტრიქონი ანაგრამი. 
# ( ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების
# ასოების გადაადგილებით)


def is_anagram(word1, word2):

    return sorted(word1) == sorted(word2)

arg1 =  input("enter first word... ")
arg2 = input("enter second word... ")

result = is_anagram(arg1, arg2)

print(result)



# დავალება 2.

# დაწერეთ პითონის ფუნქცია რომელიც მიიღებს ორ პარამეტრს, 
# პირველს სტრიქონს და მეორეს სიმბოლოს. 
# ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს მისი რაოდენობა


def count_i_in_string(string, symbol):
    return string.count(symbol)

str = input("enter the string... ")
symb = input("Enter The symbol... ")

result2 = count_i_in_string(str, symb)
print(result2) 


# დავალება 3.

# დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, 
# და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.(ფიბონაჩის მიმდევრობის თანახმად, ყოველი მომდევნო რიცხვი წინა ორი რიცხვის ჯამია)
# 0, 1, 1, 2, 3, 5, 8, 13 ...


def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

num = int(input("Enter the number"))
result = fibonacci_sequence(num)
print(result)