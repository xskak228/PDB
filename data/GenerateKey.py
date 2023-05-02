import random

a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = '1234567890'


def GenerateKeys():
    key = ''
    for i in range(12):
        numb = random.randint(1, 2)
        if numb == 1:
            key += random.choice(list(a))
        elif numb == 2:
            key += random.choice(list(b))

    return key