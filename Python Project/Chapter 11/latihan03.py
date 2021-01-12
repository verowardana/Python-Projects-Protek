# Soal3
myFile = open('C:\\Users\\verow\\Documents\\File\\College\\NO LIFE\\Materi\\College\\Pemrograman Terstruktur\\Praktikum 11\\fileteks.txt','r')
readline = myFile.readlines()
testline=[]
for line in readline:
    line=line.rstrip('\n')
    line=line.split('|')
    testline+=line
    
import datetime
from datetime import *

today=datetime.date(datetime.now())

while True:
    membercode = input('Masukkan Kode Member    :')
    if (membercode in testline)==False:
        print('Kode member tidak ditemukan, silahkan coba lagi')
    if (membercode in testline)==True:
        break

def diffDate(today,exp):
    expired=datetime.date(datetime.strptime(exp,'%Y-%m-%d'))
    selisih=(today-expired).days
    if selisih>0:
        return selisih
    if selisih<0:
        return 0
    else:
        return 0
    
for data in readline:
    data = data.rstrip('\n')
    data= data.split('|')
    code=data[0]
    name=data[1]
    book=data[2]
    tanggalpinjam=data[3]
    tanggalexp=data[4]
    if data[0]==membercode:
        print('Kode Member              :',membercode)
        print('Nama Member              :',name)
        print('Judul Buku               :',book)
        print('Tanggal Mulai Peminjaman :',tanggalpinjam)
        print('Tanggal Maks Pengembalian:',tanggalexp)
        print('Tanggal Pengembalian     :',today)
        print('Terlambat                :',diffDate(today,tanggalexp),'hari')
        print('Denda                    : Rp',diffDate(today,tanggalexp)*2000)
    else:
        continue
