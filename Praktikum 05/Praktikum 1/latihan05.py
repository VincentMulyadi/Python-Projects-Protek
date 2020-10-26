kodeK = int(input("Masukkan kode karyawan            : "))
namaK = input("Masukkan nama karyawan            : ")
goloK = input("Masukkan golongan                 : ")
statK = input("Masukkan status(1:menikah, 2:blm) : ")
if(statK == "1"):
    jumlahA = int(input("Masukkan jumlah anak              : "))
elif(statK == "2"):
    jumlahA = 0

#Potongan
A = 10000000 
perA = 2.5
potA = A * perA / 100
B = 8500000
perB = 2.0
potB = B * perB / 100
C = 7000000
perC = 1.5
potC = C * perC / 100
D = 5500000
perD = 1.0
potD = D* perD / 100

#Tunjangan
TunjanganA = jumlahA * 0.05 * A
TunjanganB = jumlahA * 0.05 * B
TunjanganC = jumlahA * 0.05 * C
TunjanganD = jumlahA * 0.05 * D
TunjanganIA = A * 0.1
TunjanganIB = B * 0.1
TunjanganIC = C * 0.1
TunjanganID = D * 0.1

#Gaji Kotor
gajiKA = A + TunjanganA + TunjanganIA
gajiKB = B + TunjanganB + TunjanganIB
gajiKC = C + TunjanganC + TunjanganIC
gajiKD = D + TunjanganD + TunjanganID

#Gaji Bersih
berA = gajiKA - potA
berB = gajiKB - potB
berC = gajiKC - potC
berD = gajiKD - potD

print(" ")
print("=========================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-----------------------------------------")
print("Nama Karyawan            :", namaK,"( Kode :", kodeK ,")")
print("Golongan                 :", goloK)
if(statK == "1"):
    print("Status Menikah           : Menikah")
elif(statK == "2"):
    print("Status Menikah           : Belum Menikah")

if(statK == "1"):
    print("Jumlah Anak              :", jumlahA)
elif(statK == "2"):
    print("Jumlah Anak              : 0")

print("-----------------------------------------")

if(goloK == "A"):
    print("Gaji Pokok               : Rp.", int(A))
    if(statK == "1") :
        print("Tunjangan Istri/Suami    : Rp.", int(TunjanganIA))
        print("Tunjangan Anak           : Rp.", int(TunjanganA))
    elif(statK == "2") :
        print("Tunjangan Istri/Suami    : Rp. 0")
        print("Tunjangan Anak           : Rp. 0")
    print("----------------------------------------- +")
    print("Gaji Kotor               : Rp.", int(gajiKA))
    print("Potongan(", float(perA) ,"%)         : Rp.", int(potA))
    print("----------------------------------------- -")
    print("Gaji Bersih              : Rp.", int(berA))

if(goloK == "B"):
    print("Gaji Pokok               : Rp.", int(B))
    if(statK == "1") :
        print("Tunjangan Istri/Suami    : Rp.", int(TunjanganIB))
        print("Tunjangan Anak           : Rp.", int(TunjanganB))
    elif(statK == "2") :
        print("Tunjangan Istri/Suami    : Rp. 0")
        print("Tunjangan Anak           : Rp. 0")
    print("----------------------------------------- +")
    print("Gaji Kotor               : Rp.", int(gajiKB))
    print("Potongan(", float(perB) ,"%)         : Rp.", int(potB))
    print("----------------------------------------- -")
    print("Gaji Bersih              : Rp.", int(berB))

if(goloK == "C"):
    print("Gaji Pokok               : Rp.", int(C))
    if(statK == "1") :
        print("Tunjangan Istri/Suami    : Rp.", int(TunjanganIC))
        print("Tunjangan Anak           : Rp.", int(TunjanganC))
    elif(statK == "2") :
        print("Tunjangan Istri/Suami    : Rp. 0")
        print("Tunjangan Anak           : Rp. 0")
    print("----------------------------------------- +")
    print("Gaji Kotor               : Rp.", int(gajiKC))
    print("Potongan(", float(perC) ,"%)         : Rp.", int(potC))
    print("----------------------------------------- -")
    print("Gaji Bersih              : Rp.", int(berC))

if(goloK == "D"):
    print("Gaji Pokok               : Rp.", int(D))
    if(statK == "1") :
        print("Tunjangan Istri/Suami    : Rp.", int(TunjanganID))
        print("Tunjangan Anak           : Rp.", int(TunjanganD))
    elif(statK == "2") :
        print("Tunjangan Istri/Suami    : Rp. 0")
        print("Tunjangan Anak           : Rp. 0")
    print("----------------------------------------- +")
    print("Gaji Kotor               : Rp.", int(gajiKD))
    print("Potongan(", float(perD) ,"%)         : Rp.", int(potD))
    print("----------------------------------------- -")
    print("Gaji Bersih              : Rp.", int(berD))