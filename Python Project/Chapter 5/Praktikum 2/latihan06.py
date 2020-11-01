from random import randint

print("Hai..! Selamat datang di permainan tebak angka!")
print("Saya sudah memilih sebuah bilangan bulat secara acak antara 0 s/d 100.")
print("Coba tebak yaa!!!XD")

komputer = randint(0,100)

player = int(input("Masukkan angka: "))

jml = 98

while player >= 0:
    if player > komputer:
        print("Bilangan anda terlalu besar") 
        player = int(input("Masukkan angka: "))
        jml = jml - 2
    elif player < komputer:
        print("Bilangan anda terlalu kecil")
        player = int(input("Masukkan angka: "))
        jml = jml - 2
    elif player == komputer:
        print("Bilangan tebakkan anda BENAR")
        print("Skor anda adalah: " + str(jml))
        break
    else:
        int(input("Maaf input tidak valid. Silahkan masukkan angka: "))
