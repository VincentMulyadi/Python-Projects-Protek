buah = {
    'apel': 5000,
    'jeruk' : 8500,
    'mangga' : 7800,
    'duku' : 6500
}

answer = 'y'

while answer == 'y':
    print('Menu : \nA. Tambah data buah \nB. Beli buah \nC. Menghapus data buah')
    menu = str(input('Pilihan menu : '))
    if menu == 'A' :
        nama_buah = str(input('Masukkan nama buah    : '))
        harga_satuan = str(input('Masukkan harga satuan : '))
        if nama_buah in buah :
            print('Nama buah sudah ada dalam dictionary.')
        else:
            buah[nama_buah] = harga_satuan
            print(buah)
    elif menu == 'B':
        sum = 0
        lagi = 'y'
        while lagi == 'y':
            nama_buah = str(input('Nama buah yang ingin dibeli  :  '))
            if nama_buah in buah :
                for x,y in buah.items() :
                    if(x == nama_buah):
                        berat = float(input('Berat buah yang ingin dibeli : '))
                        harga = berat * y
            else:
                print('Maaf, buah yang diminta tidak tersedia')
            sum += harga
            lagi = str(input('Beli buah yang lain (y/n)? '))
            
        print('---------------------------------------------------------')
        print('Total harga                  : Rp.'+ str(sum))
    elif menu == 'C':
        hapus = str(input('Nama buah yang ingin dihapus : '))
        if hapus in buah:
            del buah[hapus]
            print(buah)
        else :
            print('Nama buah tidak ditemukan')
    
    answer = str(input('Ingin melakukan penambahan/pembelian lagi(y/n) ?'))

print('Terima Kasih telah menggunakan layanan buah kami. \nSampai Jumpa Lagi! :)')
        


    