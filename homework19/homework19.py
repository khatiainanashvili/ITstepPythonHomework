# ამოცანა 1.

# შექმენით კლასი Product ატრიბუტებით name, price, quantity,
# შექმენით კლასის რამდენიმე ობიექტი, დაამატეთ ლისტში, დაწერეთ სერიალიზაციის მეთოდი,
# რომ კლასი გადაითარგმნოს JSON ფორმატში და ჩაწერეთ ფაილში, შემდეგ წაიკითხეთ ეს ფაილი,
# დაწერეთ დესერიალიზაციის მეთოდი, 
# რომ ინფორმაცია გადაითარგმნოს Product კლასში და და ბეჭდეთ ყველა პროდუქტის ინფორმაცია



import json


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
    
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    @staticmethod
    def from_dict(data):
        
        return Product(data['name'], data['price'], data['quantity'])


product1 = Product("Product1", 100, 5)
product2 = Product("Product2", 200, 10)
product3 = Product("Product3", 300, 15)


products = [product1, product2, product3] 
json_string = json.dumps([product.to_dict() for product in products], indent=4)

print("Serialized JSON:")
print(json_string)


with open('products.json', 'w') as json_file:
    json_file.write(json_string)


with open('products.json', 'r') as json_file:
    data = json.load(json_file)

deserialized_products = [Product.from_dict(item) for item in data]


# ამოცანა 2.

# დავალების შესასრულებლად გამოიყენეთ movies.json
# წაიკითხეთ მოცემული ფაილი და ამავე ფაილში ჩაწერეთ ის ფილმები, რომელთა გამოშვების თარიღიც არის 2000-ზე მეტი და ჟანრი არის Crime,
# ხოლო Crime სიტყვა ჟანრში შეცვალეთ New_Crime-ით. ამავე ფაილში ჩაწერეთ ისეთი ფილმები, რომელთა გამოშვების თარიღიც არის 2000-ზე ნაკლები, 
# ჟანრი არის Drama და ჟანრის სახელი ჩაუწერეთ Old_Drama. 
# იმ ფილმებს, რომელიც 2000 წელს არის გამოშვებული ჟანრში ჩაუმატეთ New_Century და ეს ფილმებიც ამავე ფაილში ჩაწერეთ.


import json

with open('homework19/movies.json', 'r') as file:
    data = json.load(file)


new_crime_movies = []
old_drama_movies = []

for page in data:
    for movie in page["results"]:
        release_year = int(movie["release_date"].split("-")[0])
        genres = [genre.lower() for genre in movie["genres"]]

        if "crime" in genres and release_year > 2000:
            movie["category"] = "New_Crime"
            new_crime_movies.append(movie)
        
        if "drama" in genres and release_year <= 1999:
            movie["category"] = "Old_Drama"
            old_drama_movies.append(movie)

output_data = {
    "New_Crime": new_crime_movies,
    "Old_Drama": old_drama_movies
}


with open('movies.json', 'w') as file:
    json.dump(output_data, file, indent=4)

print("Movies have been categorized and written back to movies.json.")
