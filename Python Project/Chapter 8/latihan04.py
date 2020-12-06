# Soal 13
print("Jumlah Huruf")
total = int(input("Tentukan banyak nama mahasiswa yang ingin dimasukkan: "))
index = 0
n = 1

e = []
while True:
    print("Masukkan bilangan ke-", n,":", end ='')
    bil = str(input())
    e.insert(index, bil)
    index += 1
    total -= 1
    if total == 0:
        break
e.sort()
e = tuple(e)
print("Hasil: ")
for bil in e:
    urut = len(bil)
    print(bil, urut, 'karakter')
