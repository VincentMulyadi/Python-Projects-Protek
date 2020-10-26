jP = 0
from random import randint
while True :
    bil = randint(0, 10)
    print(bil)
    jP += 1
    if bil == 5:
        break
print('Jumlah perulangan :', int(jP))