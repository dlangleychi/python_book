my_list = [6, 3, 0, 11, 20, 4, 17]

i = 0 
while i < len(my_list):
    print(my_list[i])
    i += 1

print()

for number in my_list:
    print(number)

print()

i = 0 
while i < len(my_list):
    if my_list[i] % 2 == 0:
        print(my_list[i])
    i += 1

print()

for number in my_list:
    if number % 2 == 1:
        print(number)