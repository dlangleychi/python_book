def remainders_3(numbers):
    return [number % 3 for number in numbers]

def remainders_5(numbers):
    return [number % 5 for number in numbers]

def any_non_multiples(numbers):
    return any(remainders_3(numbers))

def all_non_5_multiples(numbers):
    return all(remainders_5(numbers))

if __name__ == '__main__':
    numbers_1 = [0, 1, 2, 3, 4, 5, 6]
    numbers_2 = [1, 2, 4, 5]
    numbers_3 = [0, 3, 6]
    numbers_4 = []

    print (numbers_1, any_non_multiples(numbers_1))
    print (numbers_2, any_non_multiples(numbers_2))
    print (numbers_3, any_non_multiples(numbers_3))
    print (numbers_4, any_non_multiples(numbers_4))

    numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
    numbers_3 = [0, 5, 10]
    numbers_4 = []

    print(numbers_1, all_non_5_multiples(numbers_1))
    print(numbers_2, all_non_5_multiples(numbers_2))
    print(numbers_3, all_non_5_multiples(numbers_3))
    print(numbers_4, all_non_5_multiples(numbers_4))