namaFile = input('Masukkan nama file : ')
file = open(namaFile, 'a')
lagi = 'y'
while lagi == 'y' :
    dataTambahan = input('Data yang mau ditambahkan : ')
    file.write(dataTambahan + '\n')
    lagi = input('Mau lagi (y/n) : ')

file.close()
