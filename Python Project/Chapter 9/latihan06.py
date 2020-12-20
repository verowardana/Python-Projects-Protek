def showdata(x):
    print("="*60)
    print("NIM       NAMA         N.MID     N.UAS    N.AKHIR     STATUS")
    print("-"*60)
    for data in x:
        print(data["nim"].ljust(10),end='')
        print(data['nama'].ljust(10),end='')
        angka = str(data['mid'])
        print(angka.center(10),end='')
        angka = str(data['uas'])
        print((angka).center(10),end='')
        tester = int((data['mid']+2*data['uas'])/3)
        test = str(tester)
        print(test.center(15),end="")
        if tester >= 60:
            print('LULUS')
        if tester < 60:
            print('TIDAK LULUS')
    print("-"*60)

nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
        {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
        {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

showdata(nilai)
