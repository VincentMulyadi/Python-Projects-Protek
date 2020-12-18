def ubahHuruf(teks, a, b):
    teks = list(teks)
    result = []
    for huruf in teks:
        if huruf == a :
            huruf = b
        result.append(huruf)
    print(''.join(result))
    

def ubahHuruf2(teks, a, b):
    print(teks.replace(a, b))


ubahHuruf('MATEMATIKA', 'T', 'S')
ubahHuruf2('MATEMATIKA', 'T', 'S')