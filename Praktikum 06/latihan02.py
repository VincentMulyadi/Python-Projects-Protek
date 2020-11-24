def starFormation1(n):
    kolom = 0
    baris = n
    
    i = 0
    while(i < baris):
        j = 0
        while(j <= kolom):
            print('*', end=' ')
            j += 1
        print(' ')
        i += 1
        kolom += 1

def starFormation2(n):
    kolom = n
    baris = n
    
    i = 0
    while(i < baris):
        j = 0
        while(j < kolom):
            print('*', end=' ')
            j += 1
        print(' ')
        i += 1
        kolom -= 1


starFormation2(4)
        


