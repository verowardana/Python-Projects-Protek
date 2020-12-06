# Soal 20
print("Terdapat buah apel, jeruk, mangga, dan duku. Silahkan dipilih.")
buah = {'apel':5000,"jeruk":8500,'mangga':7800,'duku':6500}
awal = 0
while True:
    beli = str(input('Nama buah yang dibeli   :'))
    total = int(input('Berapa Kg               :'))
    lagi = str(input('beli buah yang lain (y/n) :'))
    harga = buah[beli]*total
    awal+=harga
    if lagi == 'n':
        break
print('Total Harga             :',awal)
