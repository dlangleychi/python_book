'''
#1
counter is never incremented, so it stays at zero ad infinitum
'''

age = int(input("How old are you? "))

print(f'You are {age} years old.')
throw_away = [
    print(f'In {increment} years, you will be {increment + age} years old')
    for increment in range(10,50,10)
]

