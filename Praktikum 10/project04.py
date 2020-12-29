myfile = open('daftar_mhs.txt', 'r')
list_data = myfile.readlines()
i = 0
new_list = []
for data in list_data:
    data_mhs = str(list_data[i])
    data_mhs = data_mhs.split('|')
    new_list.append(data_mhs)
    i += 1

cari = input('Masukkan NIM yang mau dicari : ')

if cari in new_list[1]:
    a = 1
    for lists in new_list:
        if cari == new_list[a][0]:
            print('Data Mahasiswa')
            print('NIM    : '+ new_list[a][0])
            print('Nama   : '+ new_list[a][1])
            print('Alamat : '+ new_list[a][2])
            break
        else:
            a += 1
else:
    print('Data mahasiswa tidak ditemukan')