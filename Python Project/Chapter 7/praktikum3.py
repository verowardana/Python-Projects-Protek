# membuka dan mau membaca file c:/Users/verow/Documents/data2
try:
    file = open("c:/Users/verow/Documents/data2.txt", "r")
except FileNotFoundError:
    print("File tidak ditemukan")

# Eksekusi program
try:
    sum = 0
    for data  in file:
        sum = sum + int(data)
    print(sum)
except ValueError:
    print("Tidak dapat menghasilkan data yang valid")

