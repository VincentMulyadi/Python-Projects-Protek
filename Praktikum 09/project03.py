def bintang(n):
    x = -1
    y = round(n / 2)
    count = 0
    length = 1 + 2*(n-1)
    length += length
    space = ' '
    while count < y :
        x += 2
        count += 1
        star = '* '*x
        print(star.center(length, space))
    
    while count >- y :
        x -= 2
        count -= 1
        star = '* '*x
        print(star.center(length, space))
        if(count == 1):
            break

bintang(7)