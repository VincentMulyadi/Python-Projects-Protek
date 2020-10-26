from random import randint
print('"Hai.. nama saya Mr.Lappie, saya telah memilih sebuah bilanga bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!" ')
while True :
    bil = randint(0, 100)
    ans = int(input('Tebakan Anda = '))
    if(ans > bil):
        print('Hehehe... Bilangan tebakan anda terlalu besar')
    elif(ans < bil):
        print('Hehehe... Bilangan tebakan anda terlalu kecil')
    elif (ans == bil):
        print('Yeeee... Bilangan tebakan anda BENAR :-)')
        break