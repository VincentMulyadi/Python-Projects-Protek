print('------------------------------')
print('PROGRAM HITUNG RATA-RATA')
print('------------------------------')

bil = 0
total = 0
sum = 0
answer = 'y'
mean = 0

while answer == 'y':
    try:
        bil = int(input('Masukkan bilangan bulat : '))
        sum = sum + bil
        total += 1
        mean = sum / total
    except ValueError:
        print('Bukan bilangan bulat')
    answer = input('Lagi (y/n)? : ')

print('Rata-ratanya adalah:', mean)
    
