lagi = "y"
myFile = open('C:\\Users\\verow\\Documents\\File Text\\file teks 2.txt', 'w')
myFile.close()
myFile = open('C:\\Users\\verow\\Documents\\File Text\\file teks 2.txt', 'a+')

while lagi == "y":
    NIM    = input('Masukkan NIM     : ')
    nama   = input('Masukkan nama    : ')
    alamat = input('Masukkan alamat  : ')
    lagi   = input('Tambah input(y/n): ')
    hasil = NIM+'|'+nama+'|'+alamat+'\n'
    myFile.write(hasil)
myFile.seek(0,0)
read = myFile.read()
print(read)
myFile.close()
    
