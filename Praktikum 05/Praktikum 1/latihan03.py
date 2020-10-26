nilaiBi = int(input("Masukkan nilai Bahasa Indonesia    : "))
nilaiIpa = int(input("Masukkan nilai IPA                 : "))
nilaiMTK = int(input("Masukkan nilai Matematika          : "))

if(100 > nilaiBi > 0) and (100 > nilaiIpa > 0 and (100 > nilaiMTK > 0)):
    if(nilaiBi>=60) or (nilaiIpa>=60) :
        if(nilaiMTK>70):
            print("Status Kelulusan     : LULUS")
        else :
            print("Status Kelulusan     : TIDAK LULUS")
            print("Sebab :")
    else:
        print("Status Kelulusan     : TIDAK LULUS")
        print("Sebab :")
else :
    print("Maaf input ada yang tidak valid")

if(100 > nilaiBi > 0) and (100 > nilaiIpa > 0 and (100 > nilaiMTK > 0)):    
    if(0 <= nilaiBi < 60):
        print("-    Nilai bahasa indonesia kurang dari 60")
    if(0 <= nilaiIpa < 60):
        print("-    Nilai IPA kurang dari 60")
    if(0 <= nilaiMTK < 70):
        print("-    Nilai MTK kurang dari 70")