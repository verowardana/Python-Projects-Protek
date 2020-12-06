# Soal 24
print('==================================')
def nilaiTertinggi(x):
    e = []
    nilai = 0
    for x in nilaiMhs:
        mid = x['mid']
        uas = x['uas']
        if mid + (uas * 2) > nilai:
            nilai = (mid + (uas * 2))
            max1 = mid
            max2 = uas
    for y in nilaiMhs:
        if y['mid'] == max1:
            if y['uas'] == max2:
                print('Nilai tertinggi diraih oleh')
                print('NIM :',y['nim'],'Nama :',y['nama'])
                nilai=(y['mid']+(2*y['uas']))/3
                print('Dengan nilai :', nilai)
nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80}, 	      {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50},
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
	      {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]
nilaiTertinggi(nilaiMhs)
