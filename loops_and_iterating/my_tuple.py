
def find_integers(collection):
    return [obj for obj in collection if type(obj) is int]

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)     