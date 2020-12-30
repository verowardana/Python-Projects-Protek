file = open('C:\\Users\\verow\\Documents\\File Text\\file teks 6.txt', 'r')
tulis = open('C:\\Users\\verow\\Documents\\File Text\\file teks 6 encoded.txt', 'w')

for line in file:
    line = line.rstrip('\n')
    line = line.split(' ')
    for value in line:
        try:
            angka=(int(value))
            save=str(angka)
        except ValueError:
            continue
        del line[line.index(save)]
    word = line
    newword = []
    for letter in word:
        character=letter.split()
        fixit = []
        for kata in character:
            for huruf in kata:
                geser = angka
                if ord(huruf)+geser>90:
                    geser=ord(huruf)+geser-90+64
                    new=chr(geser)
                if ord(huruf)+geser<=90:
                    geser=ord(huruf)+geser
                    new=chr(geser)
                fixit.append(new)
                done=''.join(fixit)
            newword.append(done)
            hasil=' '.join(newword)
    hasil = ' '.join(newword) + ' ' + save + '\n'
    print('hasil: \n', hasil)
    tulis.write(hasil)
file.close()
tulis.close()
