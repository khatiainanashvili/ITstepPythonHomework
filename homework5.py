# დავალება 1.
# მოცემულია სია my_list:
# mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9 , 12, 34, 49]
# დაწერეთ პროგრამა, რომელიც შეკრებს ამ სიის მე–3, მე–9 და მე–14 ელემენტებს
# და მიღებულ შედეგ დაბეჭდავს ტერმინალში.

mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9 , 12, 34, 49]

sum = mylist[2] + mylist[8] + mylist[13]
print(sum)

# დავალება 2.
# შექმენით 20 რენდომ რიცხვისგან შემდგარი ლისტი, შექმენით ახალი ლისტი, რომელშიც შეინახავთ პირველი ლისტიდან მხოლოდ კენტ 
# მნიშვნელობებს და დაბეჭდეთ ლისტში ყველაზე მცირე და ყველაზე დიდი ელემენტი. არ გამოიყენოთ ფუნქციები min() და max()


import random 
nums_lenght = 0
 
random_number_list = []
odd_nums_list = []

while nums_lenght < 20:
   random_number = random.randint(0, 5000)
   random_number_list.append(random_number)
   nums_lenght += 1
   

for i in random_number_list:
      if i % 2 != 0 :
         odd_nums_list.append(i)

odd_nums_list.sort()

print(random_number_list)
print(odd_nums_list)

max = odd_nums_list[-1]
min = odd_nums_list[0]

print(f' min number is: {min}, max number is {max}')



# დავალება 3.

# დაწერეთ პითონის პროგრამა, რომელიც შექმნის ლისტს my_llist = [43, '22', 12, 66, 210, ["hi"]], და შეასრულებს
# შემდეგ ნაბიჯებს:
# a. დაბეჭდავს 210-ის ინდექს, თუ მერამდენე ინდექსზეა
# b. დაამატებს ბოლო ელემენტში ტექსტს "hello"
# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს ლისტს
# d. შექმენით ახალი ლისტი my_llist_2 , რომელსაც ექნება my_llist მნიშვნელობა, გაასუფთავეთ my_llist_2
# მნიშნველობა და დაბეჭდეთ my_llist და my_llist_2 ლისტებ


my_llist = [43, '22', 12, 66, 210, ["hi"]]
item = 210

my_llist.index(item)

print(my_llist.index(item))

last_item = my_llist[-1]
last_item.append("hello")
print(my_llist)
my_llist.remove(my_llist[1])
print(my_llist)

my_llist2 = my_llist.copy()

my_llist2.clear()

print(my_llist, my_llist2)


# დავალება 4.

# დაწერეთ პროგრამა, რომელიც დაბეჭდავს ორი მატრიცის ჯამს, ჯამი გამოითვლება შემდეგი წესით,
# ერთი და იგივე ადგილზე მდგომი ელემენტები ემატება ერთმანეთს, მატრიცების განზომილებები უნდა იყოს ერთი და იგივე

matrix1= [
       [1,2,3],  
       [4,5,6],  
       [7,8,9]]  
  
matrix2 = [
       [9,8,7],  
       [6,5,4],  
       [3,2,2]
       ]  
  
result = [
    [0,0,0],  
    [0,0,0],  
    [0,0,0]
    ]  
for i in range(len(matrix1)):  
   for j in range(len(matrix1[0])):  
       result[i][j] = matrix1[i][j] + matrix2[i][j]  
for r in result:  
   print(r)  


# დავალება 5.

# დაწერეთ პროგრამა რომელიც გააკეთებს კვადრატული 3x3 მატრიცის ტრანსპონირებას, ტრანსპონირება ნიშნავს ინდექსების შებრუნებას, 
# მაგ. თუ გვაქვს ერთ-ერთი ჩანაწერი ინდექსით list[2][3], 
# ტრანსპონირების შემდეგ მისი ინდექსი უნდა გახდეს list[3][2], ასე ხდება ყველა ჩანაწერზე
# მაგ:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# ტრანსპონირებული: [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]

