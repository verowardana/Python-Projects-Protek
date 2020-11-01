# input kode, nama, golongan
kode = input("Masukkan kode karyawan   : ")
nama = input("Masukkan nama Karyawan   : ")
gol = input("Masukkan golongan        : ")

#Struktur rincian gaji karyawan
print("__________________________")
print("--------------------------")

print("STRUKTUR RINCIAN GAJI KARYAWAN")
print("--------------------------")

print("Nama karyawan        : ", nama, "(kode:", kode,")")
print("Golongan             : ", gol)
print("--------------------------")

# perhitungan gaji dan potongan
while True:
    if(gol == 'A'):
        gaji = 10000000
        persen = print("Potongan = 2.5%")
        potongan = 10000000*2.5/100
    elif(gol == 'B'):
        gaji = 8500000
        persen = print("Potongan = 2.0%")
        potongan = 8500000*2/100
    elif(gol == 'C'):
        gaji = 7000000
        persen = print("Potongan = 1.5%")
        potongan = 7000000*1.5/100
    elif(gol == 'D'):
        gaji = 5500000
        persen = print("Potongan = 1.0%")
        potongan = 5500000*1/100
    else:
        print("Maaf input golongan tidak valid. Masukkan golongan A/B/C/D dengan huruf kapital.")
        break
    # perhitungan total
    gajiber = gaji - potongan
    #eksekusi perhitungan
    print("--------------------------")
    print("Gaji pokok           : Rp", gaji)
    print("Potongan             : Rp", potongan)
    print("Gaji Bersih          : Rp", gajiber)
    break
    






     

    
