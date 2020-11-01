def factorial(n):
    if (n == 0):
        return 1
    else :
        return n * factorial(n-1)

def C(a, b):
    hasil = factorial(a) / (factorial(a-b)*factorial(b))
    print(hasil)

def P(a, b):
    hasil = factorial(a)/factorial(a-b)
    print(hasil)

#3A
C(5,3)

#3B
P(10,7)