jumlah = 0
sum = 0
for i in range(1, 100, 2):
    print(int(i))
    jumlah += 1
    sum = sum + i

print('Banyaknya bilangan ganjil :', int(jumlah))
print('Jumlah seluruh bilangan   :', int(sum))