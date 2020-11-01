# input kode, nama, golongan
kode = input("Masukkan kode karyawan   : ")
nama = input("Masukkan nama Karyawan   : ")
gol = input("Masukkan golongan        : ")
status = input("Masukkan status(1: menikah; 2:belum): ")
if(status == '1'):
    anak = float(input("Masukkan jumlah anak: "))

# struktur rincian gaji karyawan
print("______________________________________________")
print("----------------------------------------------")

print("STRUKTUR RINCIAN GAJI KARYAWAN")
print("----------------------------------------------")

print("Nama karyawan        : ", nama, "(kode:", kode,")")
print("Golongan             : ", gol)
if(status == '1'):
    print("Status menikah       : Menikah")
    print("Jumlah anak          : ", anak)
elif(status == '2'):
    print("Status menikah       : Belum menikah")


print("----------------------------------------------")
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
    # menikah
    if(status == '1'):
        tissu = gaji * 0.1
        tanak = gaji * 0.05 * anak
        gajitor = gaji+tissu+tanak
    # belum menikah
    elif(status == '2'):
        gajitor = gaji
        tissu = '0'
        tanak = '0'
    # Perhitungan total
    gajiber = gajitor-potongan
    #eksekusi perhitungan
    print("----------------------------------------------")
    print("Gaji pokok           : Rp", gaji)
    print("Tunjangan Istri/Suami: Rp", tissu)
    print("Tunjangan anak       : Rp", tanak)
    print("----------------------------------------------")
    print("Gaji kotor           : Rp", gajitor)
    print("Potongan             : Rp", potongan)
    print("----------------------------------------------")
    print("Gaji Bersih          : Rp", gajiber)
    break
