# Soal 19
def sort(x):
    data = list(x.values())
    sum = 0
    index = 0
    for y in data:
        sum += y
        index += 1
    y = sum/index
    print('rerata harga buah tersebut adalah', y)
buah = {'apel':5000,"jeruk":8500,'mangga':7800,'duku':6500}
sort(buah)
