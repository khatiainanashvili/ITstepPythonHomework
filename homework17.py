class Node:                            #Node კლასის იმპლემენტაცია
    def __init__(self, data=None):
        self.data = data              
        self.next = None               #აუცილებლად უნდა ჰქონდეს None მნიშვნელობა      
           


class LinkedList:
    def __init__(self):
        self.head = None     #ლისტის პირველი კვანძი არ შეიცავს datas და რადგან ის ჯერ-ჯერპბით ბოლო ელემენტცი არის,
                             #default მნიშვნელობად მიენიჭენა None

                             
    def append(self, data):   #append ფუნქციით ლისტში ემატება ახალი კვანძები
        
        new_node = Node(data) 
        if self.head is None:    #მოწმდება არის თუ არა ჰედი ბოლო ელემენტი
            self.head = new_node  
            return

        last_node = self.head     #ბოლო კვანძი ინიციალიზდება, როგორც ჰედი
        while last_node.next:     #სანამ ბოლო ნოუდი არ უდრის None-ს ლისტს ემატება ელემენტი,
            last_node = last_node.next  # ანუ ლისტში ემატება ელემენტი ბოლო ელემენტამდე

        last_node.next = new_node

    def remove_at(self, index):
        if index < 0 and self.head is None:  #აქ ვერ გავიგე რატო წერია ეს ხაზი, ინდექსი 0-ზე ნაკლები როგორ იქნება,
            return                           # აა, მივხვდი, რომ არ გახდეს 0 ზე ნაკლები ეგ შემოწმება წერია
                                             #ან ვერ მივხვდი
                                            

        if index == 0:                   #მოწმდება თუ ინდექსი 0 -ს უდრის აბრუნებს მხოლოდ ერთ კვანძს, რომელიც არის ჰედი
            self.head = self.head.next   
            return

        current_node = self.head      
        current_position = 0             #და რომლის პოზიციაც არის 0

        while current_node.next and current_position < index - 1:  #სანამ მოცემული ნოუდის შემდეგი ნოუდი არსებობს და წასაშლელი კვანძის  
                                                                   #ინდექსი ამ ნოუდის ინდექსზე ერთით ნაკლებია
            
            current_node = current_node.next                       #წაშლილი კვანძი ჩანაცვლდება მომდევნო კვანძით i guess                
            current_position += 1                                  #ერთით წინ წაიწევს ელემენტის პოზიცია 

        if current_node.next:                                      #ამოწმებს მიმდინარე კვანძი None ჰო არ არის, ანუ ბოლო ჰო არაა
            current_node.next = current_node.next.next             # და თუ არ არის ანაცვლებს მომდევნო კვანძით I guess

    def display(self):
        current_node = self.head                                  #მიმდინარე კვანძი ინიციალიზდება, როგორც ჰედი
        while current_node is not None:                           #სანამ კვანძი ლისტის ბოლო ელემენტი არ არის     
            print(current_node.data, end=' -> ')                  #თითოეული მონაცემი default ნიუ ლაინის ნაცვლად სრულდება '->' ამით
            current_node = current_node.next

# დავალება 2.
# დაწერეთ value გადაწოდების შედეგად ამოშლის ლოგიკა დაკავშირებულ სიებში და 
# ინდექსით ჩამატების ლოგიკა

    def delete_node(self, data):
        current_node = self.head

        if current_node is None:
            return "nothing to delete."

        if current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        
        previous_node = None
        while current_node is not None and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next


        if current_node is None:
            return "Node with value not found."
        previous_node.next = current_node.next
        current_node = None


linked_list = LinkedList()

linked_list.append(10)
linked_list.append(5)
linked_list.append(25)
linked_list.append(12)
linked_list.append(11)

linked_list.display()
print()

linked_list.delete_node(5)

print()
linked_list.remove_at(2)
linked_list.display()
print()
linked_list.remove_at(2)
linked_list.display()