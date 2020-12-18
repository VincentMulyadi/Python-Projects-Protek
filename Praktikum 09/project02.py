def bintang(n):
    x = -1
    y = n
    count = 0
    length = 1 + 2*(n-1)
    length += length
    space = ' '
    while count < y :
        x += 2
        count += 1
        star = '* '*x
        print(star.center(length, space))

bintang(4)