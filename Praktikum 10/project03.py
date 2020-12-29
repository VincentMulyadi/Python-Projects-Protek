myfile = open('daftar_mhs.txt', 'r')
list_data = myfile.readlines()
i = 0
new_list = []
for data in list_data:
    data_mhs = str(list_data[i])
    data_mhs = data_mhs.split('|')
    new_list.append(data_mhs)
    i += 1

dataMhs = {}
x = 0
for datas in new_list:
    d = {}
    d['nim'] = new_list[x][0]
    d['nama'] = new_list[x][1]
    d['alamat'] = str.rstrip(new_list[x][2])
    dataMhs[str(x+1)] = d    
    x += 1

print(dataMhs)