kodeK = int(input("Masukkan kode karyawan   : "))
namaK = input("Masukkan nama karyawan   : ")
goloK = input("Masukkan golongan        : ")

A = 10000000 
perA = 2.5
potA = A * perA / 100
berA = A - potA
B = 8500000
perB = 2.0
potB = B * perB / 100
berB = B - potB
C = 7000000
perC = 1.5
potC = C * perC / 100
berC = C - potC
D = 5500000
perD = 1.0
potD = D* perD / 100
berD = D - potD

print(" ")
print("=========================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-----------------------------------------")
print("Nama Karyawan            : ", namaK,"( Kode :", kodeK,")")
print("Golongan                 : ", goloK)
print("-----------------------------------------")
if(goloK == "A"):
    print("Gaji Pokok               : Rp.", int(A))
    print("Potongan(", float(perA) ,"%)         : Rp.", int(potA))
    print("----------------------------------------- -")
    print("Gaji Bersih              : Rp.", int(berA))
elif(goloK == "B"):
    print("Gaji Pokok               : Rp.", int(B))
    print("Potongan(", float(perB) ,"%)         : Rp.", int(potB))
    print("----------------------------------------- -")
    print("Gaji Bersih              : Rp.", int(berB))
elif(goloK == "C"):
    print("Gaji Pokok               : Rp.", int(C))
    print("Potongan(", float(perC) ,"%)         : Rp.", int(potC))
    print("----------------------------------------- -")
    print("Gaji Bersih              : Rp.", int(berC))
elif(goloK == "D"):
    print("Gaji Pokok               : Rp.", int(D))
    print("Potongan(", float(perD) ,"%)         : Rp.", int(potD))
    print("----------------------------------------- -")
    print("Gaji Bersih              : Rp.", int(berD))
