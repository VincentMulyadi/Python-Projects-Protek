myfile = open('project01_10.txt', 'r')
ganjil = 0
genap = 0
i = 0
list_file = myfile.readlines()

for lists in list_file:
    if int(list_file[i]) % 2 == 0 :
        genap += 1
    else:
        ganjil += 1
    
    i += 1

print('Jumlah Angka Ganjil :', ganjil)
print('Jumlah Angka Genap  :', genap)