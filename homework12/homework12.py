# დავალება 1.

# გამოიყენეთ titanic.csv
# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი “survived.csv”
# და ჩაწერეთ მხოლოდ გადარჩენილების ინფორმაცია.


import csv
headers = [
    'PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'
]

new_list = []

with open("homework12/titanic.csv", 'r') as csvfile:
    csv_dict_reader = csv.DictReader(csvfile, delimiter = ',')
    
    for row in csv_dict_reader:
        info = {
            'PassengerId': row['PassengerId'],
            'Survived': row['Survived'],
            'Pclass': row['Pclass'],
            'Name': row['Name'], 
            'Sex': row['Sex'], 
            'Age': row['Age'], 
            'SibSp': row['SibSp'], 
            'Parch': row['Parch'], 
            'Ticket': row['Ticket'], 
            'Fare': row['Fare'], 
            'Cabin': row['Cabin'], 
            'Embarked': row['Embarked']
            }
        if row['Survived'] == '1':
            new_list.append(info)

    with open('homework12/survived.csv', 'w') as newFile:
        writer = csv.DictWriter(newFile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(new_list) 

# დავალება 2.

# გამოიყენეთ organizations-100.csv
# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი “sorted_csv.csv” 
# და ჩაწერეთ დასორტირებული ინფორმაცია, დაასორტირეთ თანამშრომელთა რაოდენობის მიხედვით

import csv

headers2 = [
    "Index",
    "Organization Id",
    "Name",
    "Website",
    "Country",
    "Description",
    "Founded",
    "Industry",
    "Number of employees"
]

new_list2 = []

with open('homework12/organizations-100.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')

    for row in csv_reader:

        new_list2.append({
            'Index': row['Index'],
            'Organization Id': row['Organization Id'],
            'Name': row['Name'],
            'Website': row['Website'],
            'Country': row['Country'],
            'Description': row['Description'],
            'Founded': row['Founded'],
            'Industry': row['Industry'],
            'Number of employees': int(row['Number of employees']) if row['Number of employees'].isdigit() else 0 
        })

sorted_list2 = sorted(new_list2, key=lambda x: x['Number of employees'])

with open('homework12/sorted_csv.csv', 'w', newline='') as newFile:
    writer = csv.DictWriter(newFile, fieldnames=headers2)
    writer.writeheader()
    writer.writerows(sorted_list2)

# დავალება 3.

# გამოიყენეთ organizations-100.csv
# წაიკითხეთ მოცემული csv ფაილი, შექმენით ახალი csv ფაილი “ssl_companies.csv” და ჩაწერეთ მხოლოდ აიდი, კომპანიის სახელი, ვებ საიტი,
# ინდუსტრია და დასაქმებულების რაოდენობა ისეთი კომპანიების რომელთაც აქვთ ssl-ით დაცული ვებსაიტი(HTTPS)



new_list3 = []

with open('homework12/organizations-100.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')

    for row in csv_reader:
        nfo = ({
                'Index': row['Index'],
                'Organization Id': row['Organization Id'],
                'Name': row['Name'],
                'Website': row['Website'],
                'Country': row['Country'],
                'Description': row['Description'],
                'Founded': row['Founded'],
                'Industry': row['Industry'],
                'Number of employees': int(row['Number of employees']) if row['Number of employees'].isdigit() else 0 
        })
        if 'https' in row['Website']:
            new_list3.append(nfo)

with open('homework12/ssl_companies.csv', 'w', newline='') as newFile:
    writer = csv.DictWriter(newFile, fieldnames=headers2)
    writer.writeheader()
    writer.writerows(new_list3)
