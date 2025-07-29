
def get_number(message):
    return float(input(message))

first_num = get_number('Enter the first number: ')
second_num = get_number('Enter the second number: ')

print(f'{first_num} * {second_num} = {first_num * second_num}')