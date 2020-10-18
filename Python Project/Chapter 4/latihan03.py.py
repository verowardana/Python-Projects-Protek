# input jarak
jarak = int(input("Berapa jarak tempuh mobil (dalam Km): "))
# liter bensin yang digunakan
total = jarak/12
print("Bensin yang digunakan untuk perjalanan tersebut: ", total, " liter")
# kapasitas tangki
kapasitas = int(input("Berapa kapasitas tangki mobil: "))
if(kapasitas<=50):
    print("Anda harus mengisi bensin minimal 2 kali.")
    print("pada awal keberangkatan dan saat bensin habis.")

