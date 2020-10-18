# import library
import time
import datetime

# input nama user
Nama = input("Nama: ")

# input mulai sewa
print("Mulai sewa: ")
skrg = datetime.datetime.now()
tgl = skrg.day, skrg.month, skrg.year
print("Tanggal: ", tgl)
jam0 = int(input("Jam: "))
menit0 = int(input("Menit: "))

# input selesai sewa
print("Selesai sewa: ")
print("Tanggal: ", tgl)
jam1 = int(input("Jam: "))
menit1 = int(input("Menit: "))

# tarif
jamtotal = jam1 - jam0
menittotal= menit1 - menit0
print("Total waktu sewa: ", jamtotal, "jam", menittotal, "menit")

if(jamtotal>=12):
    tarif1 = 200000
    sisa = jamtotal - 12
    tarif2 = sisa*10000
if(menittotal<=60):
    tarif3 = 166*menittotal
print("Total biaya: ", tarif1+tarif2+tarif3)

