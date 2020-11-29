try:
    # input
    nama_file = input("Masukkan nama file: ")
    # open file
    file = open(nama_file, "r", encoding='cp1252')
    #print file
    print("Isi file", nama_file, "adalah: ")
    isi = file.readlines()
    for teks in isi:
        print(teks)
except FileNotFoundError:
    print("Maaf, File tidak ditemukan")

except NameError:
    print("Maaf, Nama file tidak ditemukan")

except OSError:
    print("Maaf, input tidak diketahui")

except ValueError:
    print("binary mode doesn't take an encoding argument")

# C:\Users\verow\Documents\data3.txt
          
