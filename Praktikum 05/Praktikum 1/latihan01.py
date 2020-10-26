nilaiBi = int(input("Masukkan nilai Bahasa Indonesia    : "))
nilaiIpa = int(input("Masukkan nilai IPA    : "))
nilaiMTK = int(input("Masukkan nilai Matematika     : "))

if(nilaiBi >= 60) or (nilaiIpa >= 60) :
    if(nilaiMTK>70):
        print("Status Kelulusan     : LULUS")
    else :
        print("Status Kelulusan     : TIDAK LULUS")
else:
    print("Status Kelulusan     : TIDAK LULUS")