myfile = open('project05.txt', 'r')
list_data = myfile.readlines()
i = 0
new_list = []
for data in list_data:
    data_angka = str(list_data[i])
    data_angka = data_angka.split('|')
    new_list.append(data_angka)
    i += 1

newfile = open('project05_jawaban.txt', 'w')
a = 0
for angka in new_list:
    angka1 = int(new_list[a][0])
    angka2 = int(new_list[a][1])
    newfile.write(str(angka1+angka2)+'\n')
    a += 1