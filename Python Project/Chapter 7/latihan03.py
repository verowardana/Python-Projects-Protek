print("------------------------------")
print("PROGRAM HITUNG RATA-RATA")
print("------------------------------")

i = 0
awal = 0
def masukkan():
    try:
        global lagi
        global awal
        global i
        bil = float(input('Masukkan bilangan bulat :    '))
        again = input(str('Lagi     (y/n) ? : '))
        awal += bil
        i += 1
    except ValueError:
        print("Bukan bilangan bulat")
while True:
    masukkan()
    if lagi == 'n':
        break
print ('_____________________________')
mean = start/a
print('Rata - ratanya adalah : ', mean)

