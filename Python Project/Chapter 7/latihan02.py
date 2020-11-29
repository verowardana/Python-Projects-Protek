try:
    # input
    nama_file = input("Masukkan nama file: ")
    tambahan = input("Data yang mau ditambahkan: ")
    lagi = input("Mau lagi (y/n): ")
    while lagi == 'y':
        input("Data yang mau ditambahkan: ")
        jawab = input("Mau lagi (y/n): ")
        if jawab == 'n':
            print("Terimakasih")
            break
        else:
            print("Maaf input tidak valid")
            break

    # format teks
    teks = tambahan.format()
    # buka file
    file = open(nama_file, 'a')
    # tulis teks
    file.write(teks)
    #tutup file
    file.close()
    
except FileNotFoundError:
    print("Maaf, file tidak ditemukan")
except:
    print("Maaf input tidak valid")
    
    

