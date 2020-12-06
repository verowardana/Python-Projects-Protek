# Soal 15
def kuadrat(bil):
    index = 0
    hasil =[]
    for nilai in bil:
        kuadrat = nilai**2
        hasil.insert(index,kuadrat)
        index += 1
    print(hasil)
x = [2,4,5,6]
kuadrat(x)
