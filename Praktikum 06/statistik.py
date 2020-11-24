def sum(*x):
    SUM = 0
    for number in x :
        SUM += number
    return SUM

def average(*x):
    jumlah = 0
    for number in x :
        jumlah += 1
    print(sum(*x) / jumlah)

def maximum(*x):
    maks = x[0]
    for number in x :
        if(number > maks):
            maks = number
    
    print(maks)

def minimum(*x):
    mini = x[0]
    for number in x :
        if(number < mini):
            mini = number
    
    print(mini)

#5a
average(5,10,4,9,30,16,2,11)
maximum(5,10,4,9,30,16,2,11)
minimum(5,10,4,9,30,16,2,11)

#5b
average(81,98,12,83,45,77,69,30,56)
maximum(81,98,12,83,45,77,69,30,56)
minimum(81,98,12,83,45,77,69,30,56)