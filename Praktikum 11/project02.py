from datetime import*

myfile = open('data_member.txt', 'a')
list_data = []
lagi = 'y'
while lagi == 'y':
    kode_member = input('Masukkan Kode Member : ')
    nama_member = input('Masukkan Nama Member : ')
    judul_buku = input('Masukkan Judul Buku  : ')
    date_now = datetime.date(datetime.now())
    date_due = date_now + timedelta(days=7)
    gabungan_data = kode_member+'|'+nama_member+'|'+judul_buku+'|'+str(date_now)+'|'+str(date_due)
    list_data.append(gabungan_data)
    lagi = input('Ulangi lagi (y/n)    : ')

i = 0
for data in list_data:
    datas = str(list_data[i])
    myfile.write(datas+'\n')
    i += 1

myfile.close()