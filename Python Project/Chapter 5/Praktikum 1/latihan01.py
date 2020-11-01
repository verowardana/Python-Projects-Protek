# input nilai
bind = int(input("Masukkan nilai Bhs Indonesia :"))
ipa = int(input("Masukkan nilai IPA            : "))
mtk = int(input("Masukkan nilai Matematika     : "))

# status kelulusan
if(bind<60):
    status = 'Tidak Lulus'
elif(ipa<60):
    status = 'Tidak Lulus'
elif(mtk<70):
    status = 'Tidak Lulus'
elif(bind>60 and ipa>60 and mtk>70):
    status = 'Lulus'

print("Status Kelulusan : ", status)

