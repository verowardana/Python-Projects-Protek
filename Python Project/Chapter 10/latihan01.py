myFile = open('C:\\Users\\verow\\Documents\\File Text\\file teks 1.txt', 'r')

read = myFile.readlines()

ganjil = 0
genap = 0

for i in read:
    i = int(i)
    if i % 2 == 0:
        genap += 1
    elif i % 2 == 1:
        ganjil += 1
    else:
        continue
print('Banyaknya bilangan genap  : ', genap)
print('Banyaknya bilangan ganjil : ', ganjil)
