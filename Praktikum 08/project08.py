def rerataBuah(x):
    harga_buah = list(x.values())
    i = len(harga_buah)
    a = 0
    sum = 0
    while a < i :
        sum += harga_buah[a]
        a += 1

    mean = sum / len(harga_buah)
    print(mean)

buah = {
    'apel': 5000,
    'jeruk' : 8500,
    'mangga' : 7800,
    'duku' : 6500
}

rerataBuah(buah)


    