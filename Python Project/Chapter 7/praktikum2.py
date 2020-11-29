# membuka dan mau membaca file c:/Documents/data.txt
try:
    file = open("c:/data.txt", "r")

    
# baca baris pertama dari file
# simpan ke dalam variabel bil1 sbg integer
    bil1 = int(file.readline())

# baca baris pertama dari file
# simpan ke dalam variabel bil2 sbg integer
    bil2 = int(file.readline())
except FileNotFoundError:
    print("File tidak ditemukan")

# hitung dan tampiilkan hasil bagi
try:
    hasil = bil1/bil2
    print(bil1, ' dibagi ', bil2, ' sama dengan ', hasil)
except ZeroDivisionError:
    print("Tidak boleh pembagian nol")
except NameError:
    print("File tidak ditemukan maka hasil tidak bisa dieksekusi")
