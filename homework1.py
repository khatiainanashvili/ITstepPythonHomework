# დავალება 1.

# დაწერეთ პროგრამა, რომელიც კითხულობს სამ მთელ რიცხვს 
# და ეკრანზე გამოაქვს მათი ჯამი


num1 = int(input('enter first number...'))
num2 = int(input('enter second number...'))

print("The sum is ", num1 + num2)

# დავალება 2.

# დაწერე პროგრამა, რომელიც კითხულობს კუბის გვერდის სიგრძეს(მთელ რიცხვს),
# გამოთვლის მოცულობას -V  და ზედაპიტის ფართობს S და ამ ორ მონაცემს დაბეჭდავს ეკრანზე.


cube_lenght = int(input('enter cube lenght..'))

v = cube_lenght ** 3
s = (cube_lenght ** 2) * 6

print("The volume of the cube is ", v)
print('The area of the cube is ', s)

# დავალება 3. 

# დაწერეთ პროგრამა, რომელიც ცალ-ცალკე კითხულობა კომპიუტერის 
# შემადგენელი ნაწილების ფასებს - მონიტორის, სისტემური ბლოკის, კლავიატურის 
# და ამუსის. ამ მონაცემების გამოყენებით გამოთვლის კომპიუტერის ფასს და დაბეჭდავს ეკრანზე.

monitor = float(input("enter monitor's price... "))
system_block = float(input("enter system block's price... "))
keyboard = float(input("enter keyBoard's price... "))
mouse = float(input("enter mouse's price... "))

computer_price = monitor + system_block + keyboard + mouse

print("The Computer Price is ", computer_price )