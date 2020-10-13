#1

#import library
import time
import datetime
import math

#date
jawabanPelanggan = input("Hallo... Dengan rental mobil Vincentio disini. Apa anda ingin melakukan peminjaman mobil?(ya/tidak) ") 
time.sleep(1)
if(jawabanPelanggan == "tidak") :
    print("Baiklah, Sampai Jumpa lagi, ditunggu untuk menyewa mobilnya")
    exit(0)
elif(jawabanPelanggan == "ya") :
    tanggal = int(input("Untuk bulan Oktober masih kosong jamnya, mau tanggal berapa ya? "))
    time.sleep(1)
    print("Okay, artinya tanggal", int(tanggal), "Oktober 2020 ya")

time.sleep(3)

#jam
jamAwal1 = float(input("Ingin melakukan peminjaman dari jam berapa ya? "))
time.sleep(1)
jamAkhir1 =  float(input("Oke, kira-kira sampai jam berapa peminjamannya ya? "))

jamAwal = math.floor(jamAwal1)
menitAwal = (jamAwal1 - jamAwal)*100 / 60
jamAwT = jamAwal + menitAwal

jamAkhir = math.floor(jamAkhir1)
menitAkhir = (jamAkhir1 - jamAkhir)*100 / 60
jamAkT = jamAkhir + menitAkhir

lamaPeminjaman = jamAkT - jamAwT
time.sleep(1)
print("Artinya dipinjam untuk", float(lamaPeminjaman), "jam ya")

time.sleep(3)

#pricing
sewa12Jam = 200000
setiapJam = 10000

harga1 = lamaPeminjaman - 12
harga2 = harga1 * setiapJam
hargaTotal = harga2 + sewa12Jam
print("Jadi total harganya untuk", float(lamaPeminjaman), "jam peminjaman sebanyak", int(hargaTotal), "rupiah")