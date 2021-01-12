# Soal2
myFile = open('C:\\Users\\verow\\Documents\\File\\College\\NO LIFE\\Materi\\College\\Pemrograman Terstruktur\\Praktikum 11\\fileteks.txt', 'a')

import datetime
from datetime import *

import datetime
from datetime import*
today=datetime.date(datetime.today())
kembali=today+timedelta(days=7)
today=str(today)
kembali=str(kembali)
while True:
    datalist = []
    code=   input('Masukkan Kode Member     :')
    name=   input('Masukkan Nama Member     :')
    book=   input('Masukkan Judul Buku      :')
    repeat= input('Ulangi lagi     (y/n)    :')
    datalist.append(code)
    datalist.append(name)
    datalist.append(book)
    datalist.append(today)
    datalist.append(kembali)
    joint='|'.join(datalist)+'\n'
    myFile.write(joint)
    if repeat=='n':
        break
myFile.close()
myFile = open('C:\\Users\\verow\\Documents\\File\\College\\NO LIFE\\Materi\\College\\Pemrograman Terstruktur\\Praktikum 11\\fileteks.txt','r')
print(myFile.read())
