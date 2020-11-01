banyak = 0
sum = 0
for i in range(100):
    bil = i + 1
    suku = i + 1
    if i % 2 == 0:
        print(bil)
        banyak = banyak + 1
        sum = sum + suku
print("Banyaknya bilangan ganjil: " + str(banyak))
print("Jumlah seluruh bilangan  : " + str(sum))
