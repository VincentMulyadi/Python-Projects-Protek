def buahBesar(a):
    nama_buah = list(a.keys())
    harga = list(a.values())
    harga_max = max(harga)
    index_harga = harga.index(harga_max)
    print(nama_buah[index_harga])

buah = {
    'apel': 5000,
    'jeruk' : 8500,
    'mangga' : 7800,
    'duku' : 6500
}

buahBesar(buah)