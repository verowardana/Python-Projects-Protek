# Soal 17
def sort(x):
    data = list(x.values())
    data.sort()
    for y in data:
        continue
    for name, harga in x.items():
        if harga == y:
            print('Harga paling mahal adalah', name,':', harga)
buah = {'apel':5000, 'jeruk':8500, 'mangga':7800, 'duku':6500}
sort(buah)
