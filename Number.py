x=18
y=2
print(x+y) #tambah
print(x-y) #kurang
print(x*y) #kali
print(x/y) #bagi
print(type(x/y)) #tipe
print(int(x/y)) #integer bagian
print(float('1234.890'))
print(x**y) #pangkat
print(10%3) #modulus
print(1+8*2) #perkalian dulu
print((1+8)*2) #ditambah dulu baru dikali

z=-90.321
print(abs(z)) #menghilangkan minus

print(pow(2,3)) #pangkat cara lain
print(2**3)
print(int(4**(1/2))) #akar pangkat
print(int(27**(1/3)))
print(max(1,2,3,4,5,6,7,8,9,10)) #nilai terbesar
print(min(1,2,3,4,5,6,7,8,9,10,.17564)) #nilai terkecil
print(round(3.67856)) #pembulatan
print(round(3.67856,2)) #pembulatan 2 angkat di belakang koma
print(.1+.2) #hasil akhir 0.300000004
print(round((.1+.2),1)) #hasil pembulatan 0.3
import math #mengambil library bawaan python
print(math.pi)
print(math.floor(3.9)) #pembulatan ke bawah
print(math.ceil(3.1)) #pembulatan ke atas
print(int(math.sqrt(196))) #akar pangkat 2
print(math.factorial(3)) #factorial 3x2x1

# ekor=13
# kaki=32
# kakikambing=4
# kakiayam=4

# ayam=abs((kakikambing*ekor-kaki)/kakiayam)
# #kambing=ekor - ayam
# kambing = ((kaki - (ayam*kakiayam))/kakikambing)

# print(int(ayam))
# print(int(kambing))

# ekor=13
# kaki=32
# kakikambing=4
# kakisapi=4

# sapi=abs((kakikambing*ekor-kaki)/kakisapi)
# kambing=ekor-sapi

# print(int(ayam))
# print(int(kambing))

# nama=input('Halo, namamu siapa? : ')
# print(f'Selamat datang {nama}')
# angka = int(input('Masukkan angka : '))
# print(f'Kuadrat dari {angka}'={angka**2})

# input('Ketik total hewan? : ')
# input('Ketik total kaki hewan? : ')
# input('Ketik jumlah kaki hewan A? : ')
# input('Ketik jumlah kaki hewan B? : ')
# input('hewan A = x, hewan B = y')

# ekor=int(input('Ketik total hewan? : '))
# kaki=int(input('Ketik total kaki hewan? : '))
# kakiA=int(input('Ketik jumlah kaki hewan A? : '))
# kakiB=int(input('Ketik jumlah kaki hewan B? : '))

# hewanA=abs((kakiB*ekor-kaki)/kakiA)
# hewanB=ekor-hewanA

# print('hewan A =',int(hewanA),'hewan B =',int(hewanB))

H=13;K=32;kakiA=4;kakiB=2
A=(K-(kakiB*H))/(kakiA-kakiB)
B=(K-(kakiA*H))/(kakiB-kakiA)
print(f'Jumlah Ayam = {int(B)}')
print(f'Jumlah Kambing = {int(A)}')

x=12
print(x)
x=13    #nilai x berubah
print(x)
x=x+2   #nilai x berubah
print(x)
x+=2    #fungsinya sama dengan yg di atas
print(x)
x-=2
print(x)
x*=2
print(x)
x/=2
print(x)