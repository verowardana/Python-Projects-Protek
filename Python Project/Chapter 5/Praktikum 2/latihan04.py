string = ""
baris = 5
while baris >= 0:
    kolom = baris
    while kolom > 0:
        string = string + "*"
        kolom = kolom - 1

    string = string + "\n"
    baris = baris - 1
print(string)
