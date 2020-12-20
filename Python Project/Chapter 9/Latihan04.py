import random
def shufflestring(x,n):
    result=[]
    if n > 2*len(x):
        n=(len(x)*2)
        print('jumlah pengacakan sebanyak: ', n)
    while n > 0:
        acak = random.sample(x, len(x))
        hasil = ''.join(acak)
        if (hasil in result)==True:
            n+=1
        if (hasil in result)==False:
            result.append(hasil)
        n -= 1
    print(result)

shufflestring('aku',100);
