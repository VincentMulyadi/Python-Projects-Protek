nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
 {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
 {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
 {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
 {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print('====================================================')
print('NIM'.ljust(10) + 'NAMA'.ljust(15) + 'N.MID'.ljust(10) + 'N.UAS'.ljust(10))
i = 0
for daftar in nilai :
    mhs = nilai[i]
    nim = mhs['nim']
    nama = mhs['nama']
    mid = str(mhs['mid'])
    uas = str(mhs['uas'])
    print(nim.ljust(10) + nama.ljust(15) + mid.rjust(5) + uas.rjust(10))
    i += 1
print('----------------------------------------------------')
print('----------------------------------------------------')