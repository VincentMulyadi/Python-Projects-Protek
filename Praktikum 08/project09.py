buah = {
    'apel': 5000,
    'jeruk' : 8500,
    'mangga' : 7800,
    'duku' : 6500
}

nama_buah = str(input('Nama buah yang ingin dibeli  :  '))

if nama_buah in buah :
    for x,y in buah.items() :
        if(x == nama_buah):
            berat = float(input('Berat buah yang ingin dibeli : '))
            harga = berat * y
        print('---------------------------------------------------------')
        print('Total harga                  : Rp.'+ str(harga))
else:
    print('Maaf, buah yang diminta tidak tersedia')

            
