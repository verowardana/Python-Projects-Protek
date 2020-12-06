# Soal 14
sayur = ['bayam', 'kangkung', 'selada']
print('MENU')
print('A. Tambah data sayur')
print('B. Hapus data sayur')
print('C. Tampilkan data sayur')
print("------------------")
while True:
    hasil = str(input('Pilihan anda: '))
    if hasil == 'A':
        new = str(input('Masukkan nama sayur yang ingin ditambahkan: '))
        sayur.append(new)
    if hasil == 'B':
        hapus = str(input('Masukkan nama sayur yang akan dihapus: '))
        try:
            nomor = sayur.index(hapus)
            del sayur[nomor]
        except ValueError:
            print('Data tidak ditemukan')
    if hasil == 'C':
        for nama in sayur:
            print(nama)
    lagi = str(input('ingin mengulang? (y/n)'))
    if lagi == 'y':
        continue
    if lagi == 'n':
        break
                    
    

                
