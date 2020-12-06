# Soal 19
print("Terdapat buah apel, jeruk, mangga, duku silahkan dipilih.")
buah={'apel':5000,"jeruk":8500,'mangga':7800,'duku':6500}
beli = str(input('Nama buah yang dibeli   :'))
total = int(input('Berapa Kg               :'))
print("___________________________________")
harga = buah[beli]*total
print('Total Harga             :',harga)
