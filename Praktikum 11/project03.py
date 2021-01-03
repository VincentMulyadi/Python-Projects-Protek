from datetime import *
from project01 import *

myfile = open('data_member.txt', 'r')
list_data = myfile.readlines()

new_list_data = []
i = 0
for data in list_data:
    split_data = list_data[i].split('|')
    new_list_data.append(split_data)
    i += 1

kode_member = input('Masukkan Kode Member   : ')

hasil = False
x = 0
for lists in new_list_data:
    if kode_member in new_list_data[x]:
        a = 0
        for lists in new_list_data:
            if kode_member == new_list_data[a][0]:
                date_now = datetime.date(datetime.now())
                days_late = diffDate(new_list_data[a][4])
                if days_late == None or days_late < 8:
                    days_late = 0
                else:
                    days_late = days_late
                print('\nData Peminjaman Buku')
                print('Kode Member              : '+ new_list_data[a][0])
                print('Nama Member              : '+ new_list_data[a][1])
                print('Judul Buku               : '+ new_list_data[a][2])
                print('Tanggal Mulai Peminjaman : '+ new_list_data[a][3])
                print('Tanggal Maks Peminjaman  : '+ str.rstrip(new_list_data[a][4]))
                print('Tanggal Pengembalian     : '+ str(date_now))
                print('Terlambat                : '+ str(days_late) +' hari')
                print('Denda                    : Rp '+ str(days_late * 2000))
                hasil = True
                break
            else:
                a += 1
    x += 1

if hasil == False :
    print('Data member tidak ditemukan')