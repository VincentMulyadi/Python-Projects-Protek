nama_mahasiswa = []
mau_lagi = 'y'
nama = []
while mau_lagi == 'y':
    nama = str(input('Masukkan nama mahasiswa : '))
    nama_mahasiswa.append(nama)
    mau_lagi = str(input('Mau masukkan nama lagi? (y/n) : '))

nama_mahasiswa.sort()
jumlah_karakter = [len(a) for a in nama_mahasiswa]
z = 0
for i in range(len(nama_mahasiswa)):
    print(nama_mahasiswa[i] + '('+ str(jumlah_karakter[z]) +' karakter)')
    z += 1
