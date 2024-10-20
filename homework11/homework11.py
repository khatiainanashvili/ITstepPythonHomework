# დავალება 1.

# დაწერეთ პითონის პროგრამა, რომელიც შექმნის ტექსტურ ფაილს და მასში ჩაწერს 1000 ხაზს(ტექსტს არ აქვს მნიშვნელობა)
# თავისი ნუმერაციით, 
# შემდეგ წაიკითხეთ ეს ფაილი და დაბეჭდეთ ხაზების რაოდენობა, თუ რამდენია შევსებულ

writable_file = open('homework11/writable_file.txt', 'w')

for i in range(1, 1001):
    writable_file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit")

with open('homework11/writable_file.txt', 'r') as readable_file:
    for line in readable_file:
         line_count = sum(1 for line in readable_file)
         print(line_count)
writable_file.close()

# დავალება 2.

# დაწერეთ პითონის პროგრამა, 
# რომელიც შექმნის ტექსტურ ფაილს და მეორე, მერვე, მეათე, 
# მეცამეტე და მეჩვიდმეტე ხაზებზე ჩაწერს ამ რიცხვებს შესაბამისი ტექსტური სახელით


with open('homework11/writable_file2.txt', 'w') as writable_file:
    for i in range(1, 101):
        writable_file.write(f"Line {i}: Lorem ipsum dolor sit amet, consectetur adipiscing elit\n")

with open('homework11/writable_file2.txt', 'r') as file:
    lines = file.readlines()

lines[1] = "Line 2: This is the 2nd line\n"
lines[7] = "Line 8: This is the  8th line\n"
lines[9] = "Line 10: This is the  10th line\n"
lines[12] = "Line 13: This is the  13th line\n"
lines[16] = "Line 17: This is the  17th line\n"


with open('homework11/writable_file2.txt', 'w') as file:
    file.writelines(lines) 

writable_file.close()


# დავალება 3.

# დაწერეთ პითონის პროგრამა, რომელიც წაიკითხავს ორ ფაილს და მათ გაერთიანებულს ჩაწერს ახალ ტექსტურ ფაილში. 
# გაერთიანებული ფაილი წაიკითხეთ და დაბეჭდეთ ტერმინალში



with open('homework11/file1.txt', 'w') as file1:
    file1.write("This is the content of the first file.\nLine 2 of the first file.\n")

with open('homework11/file2.txt', 'w') as file2:
    file2.write("This is the content of the second file.\nLine 2 of the second file.\n")

with open('homework11/file1.txt', 'r') as file1:
    content1 = file1.read()

with open('homework11/file2.txt', 'r') as file2:
    content2 = file2.read()

with open('homework11/merged_file.txt', 'w') as merged_file:
    merged_file.write(content1 + "\n" + content2)

print("Files merged successfully! Content of the merged file:")
with open('homework11/merged_file.txt', 'r') as merged_file:
    print(merged_file.read())



# დავალება 4.

# დაწერეთ ფუნქცია, რომელიც წაიკითხავს ფაილს, დაბეჭდეთ ის ხაზები, რომელიც არის ერთმანეთის პალინდრომი

with open('homework11/writable_file3.txt', 'w') as writable_file:
    writable_file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit\n")
    writable_file.write("ana\n")

with open('homework11/writable_file3.txt', 'r') as file:
    lines = file.readlines()

    for line in lines:
        cleaned_line = line.strip()
        

        if cleaned_line == cleaned_line[::-1]:
            print(f"Palindrome line: {cleaned_line}")

writable_file.close()

# დავალება 5.

# დაწერეთ პითონის ფუნქცია, რომელიც ატრიბუტად მიიღებს ფაილის სახელს, 
# წაიკითხეთ ფაილი, დაყავით ხაზები რაოდენობის მიხედვით და ჩაწერეთ ახალ ფაილებში, თითოში მაქსიმუმ 10 ხაზი.

# დავალება 6.

# დაწერეთ პითონის ფუნქცია, რომელიც ატრიბუტებად მიიღებს ფაილის სახელებს,
# წაიკითხეთ ერთი ფაილი, ამოშალეთ ცარიელი ხაზები და სრული ინფორმაცია ჩაწერეთ მეორე ფაილში
