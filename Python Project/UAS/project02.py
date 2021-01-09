#Project2
myFile = open('C:\\Users\\verow\\Documents\\dataKaryawan.dat','r')

newdict={}
for line in myFile.readlines():
    line = line.rstrip('\n').split('|')
    newdict[line[0]]=line[-5:]

def getGapok(gol):
    if gol=='A':
        return '4.000.000'
    if gol=='B':
        return '4.500.000'
    if gol=='C':
        return '5.000.000'
    else:
        return 'Terdapat salah input golongan'

kode = input('Masukkan Kode Karyawan: ')
print('')

try:
    print('Kode Karyawan    :',kode)
    print('Nama Karyawan    :',newdict[kode][0])
    print('Alamat           :',newdict[kode][1])
    print('Golongan         :',newdict[kode][2])
    print('Gaji Pokok       :',getGapok(newdict[kode][2]))
    print('Tanggal Lahir    :',newdict[kode][3], '(Usia:',newdict[kode][4],'Tahun)',end='')
except KeyError:
    print('Data tidak ditemukan',end='')
