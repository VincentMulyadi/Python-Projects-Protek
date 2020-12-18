mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
 'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
 'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
print(60*'=')
print('NIM'.ljust(10) + 'NAMA MAHASISWA'.ljust(22) + 'TGL LAHIR'.ljust(15) + 'TEMPAT LAHIR')
print(60*'-')
i = 0
for daftar in mhs:
    data = mhs[i].split(':')
    nim = data[0]
    nama = data[1]
    tanggal = data[2].split('-')
    tanggal = tanggal[2] +'/'+ tanggal[1] +'/'+ tanggal[0]
    tempat = data[3]
    i += 1
    print(nim.ljust(10)+nama.ljust(22)+tanggal.ljust(15) +tempat)
print(60*'-')
