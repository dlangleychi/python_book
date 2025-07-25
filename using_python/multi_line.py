def test():
    return ("I will try "
            "to return "
            "a multi-line "
            "string.")

def test2():
    return """
        This is 
        another example 
        of the same 
        situation.
    """

if __name__ == '__main__':
    print(test())
    print(test2())