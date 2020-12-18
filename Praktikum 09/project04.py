import random
def shuffleString(x, n):
    a = []
    x = list(x)
    count = 0
    while count < n :
        random.shuffle(x)
        result = ''.join(x)
        count += 1
        if result not in a:
            a.append(result)
        else :
            count -= 1
    print(a)

shuffleString('aku', 5)