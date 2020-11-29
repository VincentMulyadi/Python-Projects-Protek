#input
bb = int(input('Masukkan berat badan (Kg)  : '))
tb = int(input('Masukkan tinggi badan (cm) : '))

#status BMI
def hasil(bb, tb):
    BMI = bb / ((tb / 100)**2)

    if(BMI < 18):
        print('Status berat badan         : KURUS')
    elif(BMI < 23):
        print('Status berat badan         : IDEAL')
    elif(BMI < 27):
        print('Status berat badan         : GEMUK')
    elif(BMI < 35):
        print('Status berat badan         : OBESITAS')
    else:
        print('Status berat badan         : OBESITAS MORBID')

hasil(bb, tb)