#Contoh sederhana pembuatan tuple pada bahasa pemrograman python

tup1 = ('fisika', 'kimia', 1993, 2017)
tup2 = (1, 2, 3, 4, 5 )
tup3 = ("a", "b", "c", "d")

#Cara mengakses nilai tuple

tup1 = ('fisika', 'kimia', 1993, 2017)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Aksi seperti dibawah ini tidak bisa dilakukan pada tuple python
# Karena memang nilai pada tuple python tidak bisa diubah
# tup1[0] = 100;

# Jadi, buatlah tuple baru sebagai berikut
tup3 = tup1 + tup2
print (tup3)

# tup = ('fisika', 'kimia', 1993, 2017)

# print (tup)
# del tup
# print ("Setelah menghapus tuple : ", tup)

a=[1,2,3]       #list
b=(4,5,6)       #tuple
print(tuple(a)) #mengubah list menjadi tuple
print(list(b))  #mengubah tuple menjadi list

c=(1)           #tipe int
print(type(c))  

c=(1,)          #tipe tuple
print(type(c))  

x=[(1,2,3),(4,5,6)]
print(x[1][1])

list(x[0])
print(x)