def string_op(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string
    
print(string_op('hello world'))
print(string_op('goodbye'))