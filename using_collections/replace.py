info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

print('+'.join(info.split(':')))
print(info.replace(':','+'))

#8
'''
3 is index in the slice, 4 is index in the original string
'''

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606
print(stuff)