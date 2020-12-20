def daftar(x):
    print("=" * 70)
    print("NIM       NAMA                TGL LAHIR           TEMPAT LAHIR")
    print("-" * 70)
    for data in x:
        newdata = data.split(':')
        tgl = newdata[2].split('-')
        NIM = newdata[0]
        name = newdata[1]
        place = newdata[3]
        print(NIM.ljust(10),end='')
        print(name.ljust(20),end='')
        print((tgl[2]+'/'+tgl[1]+'/'+tgl[0]).ljust(20),end='')
        newlist = []
        #for tanggal in tgl:
            #tanggal=str(tanggal)
            #newlist=newlist.append(tanggal)
            #print(tanggal)
        print(place.ljust(20))
    print("-" * 70)
mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
daftar(mhs)
