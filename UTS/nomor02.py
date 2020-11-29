#input
Vo = int(input('Masukkan kecepatan mula-mula (Vo) : '))
a = int(input('Masukkan percepatan (a)           : '))

#penghitung Jarak Tempuh dari 1 - 10 detik
def jarakTempuh(Vo, a):
    t = 1
    while(t <= 10):
        s = (Vo * t) + ((a * (t**2))/2)
        print('t = ',t,',  S(t) =', s,'meter')
        t += 1

jarakTempuh(Vo, a)

        