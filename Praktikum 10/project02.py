myfile = open('daftar_mhs.txt', 'w')
lagi = 'y'

while lagi == 'y':
    nim_mhs = input('Masukkan NIM            : ')
    nama_mhs = input('Masukkan Nama Mhs       : ')
    alamat_mhs = input('Masukkan Alamat         : ')
    myfile.write(nim_mhs+'|'+nama_mhs+'|'+alamat_mhs+'\n')
    lagi = input('Ulangi input lagi (y/n) :')
