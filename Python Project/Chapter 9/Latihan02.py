def bintang(n):
    for star in range(n):
        cen = 2*x
        kol = 1
        loop = 0
        while loop < x:
            v = ('*'*kol)
            print(v.center(cen))
            loop += 1
            kol += 2
x = 4
bintang(x);
