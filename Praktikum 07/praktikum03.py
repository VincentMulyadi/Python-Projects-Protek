file = open('d:/data3.txt', 'r')
sum = 0
for data in file:
    try:
       sum = sum + int(data)
    except ValueError:
        print('invalid input')
print(sum)
