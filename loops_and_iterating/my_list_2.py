my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

def odd_even(number):
    return 'odd' if number % 2 == 1 else 'even'

odd_even_list = [odd_even(number) for number in my_list]

print(odd_even_list)