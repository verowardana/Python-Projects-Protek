myFile = open('C:\\Users\\verow\\Documents\\File Text\\file teks 5.txt', 'r')

for baris in myFile:
    baris = baris.rstrip('\n')
    baris = baris.split('|')
    total = 0
    for angka in baris:
        try:
            angka = int(angka)
            total += angka
        except ValueError:
            print('\"',angka,'\"''Bukan bilangan')
            break
    print(total)
     
