#Soal21
buah = {'apel':5000,"jeruk":8500,'mangga':7800,'duku':6500}
awal = 0
while True:
    print('Menu:')
    print('A. Tambah data buah')
    print('B. Beli Buah')
    pilih = str(input('Pilihan menu '))
    
    if pilih == 'A':
        nama = str(input('Masukkan nama buah      :'))
        harga = int(input('Masukkan harga satuan   :'))
        print('==================================')
        print('Data buah:')
        test = nama in buah.keys()
        if test == False:
            buah[nama] = harga
            for x,y in buah.items():
                print(x,'(Harga Rp ',y,')')
        if test == True:
            print('Nama buah sudah ada di dalam dictionary')
        next = str(input('Masukkan lagi? (y/n)'))
        if next == 'n':
            break
    if pilih == 'B':
        while True:
            beli= str(input('Nama buah yang dibeli   :'))
            total = int(input('Berapa Kg               :'))
            lagi = str(input('beli buah yang lain (y/n) :'))
            harga = buah[beli]*total
            awal += harga
            if lagi == 'n':
                break
        print("___________________________________")
        print('Total Harga             :',awal)
        next = str(input('Masukkan lagi? (y/n)'))
        if next == 'n':
            break
