def kuadrat(bil):
    for i in range(len(bil)):
        bil[i] **= 2
    return bil

print(kuadrat([2,5,7]))