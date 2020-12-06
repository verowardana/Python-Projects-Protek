# nomor 1
print('No. 1')
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print("====================")
# nomor 2
print('No. 2')
a.insert(3, 10)
b.insert(2, 15)
print(a)
print(b)
print("====================")
# nomor 3
print('No. 3')
a.append(4)
b.append(8)
print(a)
print(b)
print("====================")
# nomor 4
print('No. 4')
a.sort()
b.sort()
print(a)
print(b)
print("====================")
# nomor 5
print('No. 5')
c = a[:7]
d = b[1:9]
print(c)
print(d)
print("====================")
# nomor 6
print('No. 6')
e = []
for i in range (len(c)):
    e.insert(i,c[i]+d[i])
for x in range (len(c)):
    continue
for y in range (len(d)):
    continue
if x>y:
    e.insert(x,d[x])
if y>y:
    e.insert(y,d[y])
print(e)
print("====================")
# nomor 7
print('No. 7')
e = tuple(e)
print(e)
print("====================")
# nomor 8
print('No. 8')
print(min(e))
print(max(e))
print(sum(e))
print("====================")
# nomor 9
print('No. 9')
myString = 'python adalah bahasa pemrograman yang menyenangkan'
myString = set(myString)
print("====================")
# nomor 10
print('No. 10')
print(myString)
print("====================")
# nomor 11
print('No. 11')
myString = list(myString)
myString.sort()
print(myString)
