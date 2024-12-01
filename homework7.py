# დავალება 1.

# შექმენით ცვლადი squared_numbers რომელიც შეიცავს 1-დან 10-ის ჩათვლით კვადრატში აყვანილ რიცხვებს
# (არ შეავსოთ ხელით, გამოიყენეთ სეტის ტიპის მონაცემი)


squared_numbers = {x**2 for x in range(1, 11)}
print(squared_numbers)

# დავალება 2.
# მომხმარებელს მოთხოვეთ შეიყვანოს სტრინგის ტიპის მონაცემი, 
# დააბრუნეთ სეტი, რომლის ელემენტებიც არის სტრინგში არსებული თითოეული სიმბოლო


user_input = input("Enter a string: ")
unique_characters = set(user_input)
print("Set of unique characters:", unique_characters)

# დავალება 3.


# აღწერეთ ორი tuple ტიპის მონაცემი, გააერთიანეთ ეს ორი tuple და დაბეჭდეთ ერთი მთლიანი დუბლიკატების გარეშე, 
# შექმენით ლისტი duplicated_values და მასში დაამატეთ ის ინფორმაცია მხოლოდ ერთხელ, რომელიც დუბლირებული სახით გვხვდება tuple-ში, 
# დაბეჭდეთ მოცემული სია


# example:
# tuple1 = (1,2,3,4,5,6)
# tuple2 = (4,5,5,6,6,7)

# output:
# combined_tuple: (1,2,3,4,5,6,7)
# duplicated_values: [4,5,6]



tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 5, 6, 6, 7)

combined_tuple = tuple(sorted(set(tuple1).union(tuple2)))

duplicated_values = sorted(set(tuple1).intersection(tuple2))

print("Combined Tuple:", combined_tuple)
print("Duplicated Values:", duplicated_values)


# დავალება 4.


# აღწერეთ ორი ტაპლის ტიპის მონაცემი, დაბეჭდეთ ტაპლი სადაც პირველ და ბოლო ელემენტს შეცვლილი ექნება ადგილები: input: (1, 2, 3, 4)

# output: (4, 2, 3, 1)


input_tuple = (1, 2, 3, 4)
output_tuple = (input_tuple[-1],) + input_tuple[1:-1] + (input_tuple[0],)
print("Output Tuple:", output_tuple)


# დავალება 5.
# აღწერეთ ერთმანეთში ჩადგმული ტაპლის მონაცემები, დაბეჭდეთ ერთი სრული ტაპლი, სადაც მოცემული იქნება ყველა ელემენტი.


# Input: (1, (2, 3), (4, (5, 6)))
# output: (1, 2, 3, 4, 5, 6)

def flatten_tuple(nested_tuple):
    result = []
    for item in nested_tuple:
        if isinstance(item, tuple):
            result.extend(flatten_tuple(item))  # Recursively flatten nested tuples
        else:
            result.append(item)
    return tuple(result)

nested_tuple = (1, (2, 3), (4, (5, 6)))

flattened_tuple = flatten_tuple(nested_tuple)
print("Flattened Tuple:", flattened_tuple)


# დავალება 6.
# აღწერეთ ორი სეტი, დაბეჭდეთ სეტი, რომელიც შედგება ტაპლებისგან და ისინი შეიცავენ ორი სეტის ყველა შესატყვისს:


# input: {1, 2}{‘a’, ‘b’}

# output: {(1, ‘a’), (1, ‘b’), (2, ‘a’), (2, ‘b’)}

set1 = {1, 2}
set2 = {'a', 'b'}

combination  = {(x, y) for x in set1 for y in set2}

print(combination)