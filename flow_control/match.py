value = 2

match value:
    case 1 | 2 | 3| 4:
        print('value is < 5')
    case 6:
        print('value is 6')
    case 5:
        print('5 again')
    case _: # default case
        print('value is neither 5 nor 6')