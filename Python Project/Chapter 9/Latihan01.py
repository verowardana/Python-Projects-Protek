def ubahHuruf(teks, a, b):
    dataHuruf = list(set(teks))
    dataHuruf.sort()
    for huruf in dataHuruf:
        gabung = teks.replace(a, b)
    return gabung

