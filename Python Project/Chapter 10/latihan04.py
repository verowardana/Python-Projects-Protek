cari = input('Masukkan NIM yang mau dicari: ')
myFile = open('C:\\Users\\verow\\Documents\\File Text\\file teks 2.txt', 'r')

read = myFile.readlines()
dataMhs=[]

for hasil in read:
    data = hasil.rstrip()
    baru = data.split('|')
    databaru = {}
    databaru['nim'] = baru[0]
    databaru['nama'] = baru[1]
    databaru['alamat'] = baru[2]
    dataMhs.append(databaru)

baris = 1
for key in dataMhs:
    if key['nim'] == cari:
        print('Nim : ', key['nim'])
        print('Nama : ', key['nama'])
        print('alamat : ', key['alamat'])
        break
    if baris == len(dataMhs):
        print('Data mahasiswa tidak ditemukan')
    baris += 1
    
