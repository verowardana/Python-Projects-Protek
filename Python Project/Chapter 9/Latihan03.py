def bintang(n):
    cen = 2*x+5
    kol = 1
    loop = 0
    while loop < x:
        v = ('*'*kol)
        print(v.center(cen))
        loop += 1
        kol += 2
    kol -= 4
    loop -= 1
    while loop > 0:
        v = ('*' * kol)
        print(v.center(cen))
        loop -= 1
        kol -= 2
x=4
bintang(x);
