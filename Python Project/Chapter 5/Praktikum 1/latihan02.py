# input nilai
bind = int(input("Masukkan nilai Bhs Indonesia : "))
ipa = int(input("Masukkan nilai IPA            : "))
mtk = int(input("Masukkan nilai Matematika     : "))

# status kelulusan
if(bind >= 0 and bind <= 100 and ipa >=0 and ipa <= 100 and mtk >= 0 and mtk <=100):
    if(bind >= 0 and bind < 60):
        status = 'Tidak Lulus'
    elif(ipa >= 0 and ipa < 60):
        status = 'Tidak Lulus'
    elif(mtk >= 0 and mtk < 70):
        status = 'Tidak Lulus'
    elif(bind > 60 and ipa > 60 and mtk > 70 and bind <= 100 and ipa <= 100 and mtk <= 100):
        status = 'Lulus'
    print("Status Kelulusan : ", status)
else:
    print("Maaf input tidak valid")



