myFile = open('C:\\Users\\verow\\Documents\\File Text\\file teks 2.txt', 'r')
read = myFile.readlines()
dataMhs = {}
newdict = 1

for hasil in read:
    data = hasil.rstrip()
    baru = data.split('|')
    databaru = {}
    databaru['nim'] = baru[0]
    databaru['nama'] = baru[1]
    databaru['alamat'] = baru[2]
    dataMhs[newdict] = databaru
    newdict += 1
print(dataMhs)
myFile.close()
