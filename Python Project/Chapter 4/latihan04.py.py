# import library
import datetime

# input jarak kota A-B
Jab = int(input("Berapa jarak antara kota A ke B (dalam Km): "))
# input kecepatan A-B
Kab = int(input("Berapa kecepatan rata-rata dari kota A ke B (dalam Km/jam): "))

# input jarak kota B-C
Jbc= int(input("Berapa jarak antara kota B ke C (dalam Km): "))
# input kecepatan B-C
Kbc= int(input("Berapa kecepatan rata-rata dari kota B ke C (dalam Km/jam): "))

# jarak keseluruhan
Jabc = Jab+Jbc
print("Jarak yang ditempuh dari kota A ke kota C adalah ", Jabc)

# waktu keberangkatan
print("Pukul berapa anda berangkat: ")
jam0 = int(input("Jam: "))
menit0 = int(input("Menit: "))

# lama istirahat
ist = int(input("Berapa lama anda beristirahat (dalam menit): "))

# waktu dari kota A ke B
waktu1 = int(Jab/Kab)
print("Waktu yang dibutuhkan dari kota A ke B adalah ", waktu1)

# waktu dari kota B ke C
waktu2 = int(Jbc/Kbc)
print("Waktu yang dibutuhkan dari kota B ke C adalah ", waktu2)

# total waktu
waktutotjam = waktu1+waktu2
print("Waktu yang dibutuhkan adalah ", waktutotjam, " jam")
jamtiba = jam0+waktutotjam
menittiba = menit0+ist
print("Jadi, anda sampai ke tujuan pukul: ", jamtiba, " jam", menittiba, "menit")



