#Contoh sederhana pembuatan list pada bahasa pemrograman python
list1 = ['kimia', 'fisika', 1993, 2017]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

#Cara mengakses nilai di dalam list Python

list1 = ['fisika', 'kimia', 1993, 2017]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

list1 = ['fisika', 'kimia', 1993, 2017]
print ("Nilai ada pada index 2 : ", list1[2])

list1[2] = 2001
print ("Nilai baru ada pada index 2 : ", list1[2])

#Contoh cara menghapus nilai pada list python

list1 = ['fisika', 'kimia', 1993, 2017]

print (list1)
del list1[2]
print ("Setelah dihapus nilai pada index 2 : ", list1)

x=['Andi','Budi','Caca',123,True]
print(x[len(x)-1])
print(type(x[-1]))

hari=['senin','selasa','rabu','kamis','jumat','sabtu','minggu']
now='rabu'; brpHari=-100
x=hari.index(now)       #cari index now
y=brpHari%len(hari)     #modulus (sisa bagi)
h=hari[(x+y)%len(hari)] #now ditambah hasil sisa bagi
print(h)

hari=['senin','selasa','rabu','kamis','jumat','sabtu','minggu']
print(hari[::2])            #start:end:step
print('senin' in hari)      #cek 'senin' di list hari
print(hari.index('senin'))  #nilai index 'senin'
print(hari.count('senin'))  #menghitung jumlah 'senin'
hari[0]='monday'            #mengganti index 0 'senin' menjadi 'monday'
print(hari)
hari.append('senin2')       #menyisipkan nilai 'senin2' di index terakhir
print(hari)
hari.insert(4,'senin3')     #menyisipkan nilai 'senin3' di index 4
print(hari)
hari.remove('senin2')       #menghapuskan elemen 'senin2'
print(hari)
hari.pop()                  #menghapuskan elemen terakhir
print(hari)
hari.pop(2)                 #menghapus elemen berdasarkan nilai index
print(hari)
hari.sort()                 #mengurutkan nilai elemen sesuai abjad
print(hari)
hari.sort(reverse=True)     #mengurutkan nilai elemen kebalikan dari abjad
print(hari)
hari.reverse()              #membalikkan urutan index dalam list
print(hari)
hari=hari[::-1]             #membalikkan urutan index dalam list
print(hari)
hari.clear()                #menghapus semua elemen
print(hari)

x=[1,2,3,4,5,6,7,8,9]
y=x[::2]
print(x)
print(y)
print(x+y)
print(y*2)

x='abcedf'
print(list(x))              #mengubah string menjadi list              

z=[[1,2,3],[4,5,6],[7,8,9]] #list di dalam list
print(z[1][1])              #mengambil nilai index 1, di list index 1