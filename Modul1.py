# nama=input('Nama kamu : ')
# umur=input('Umur kamu : ')
# kelamin=input('Kelamin kamu : ')
# pekerjaan=input('Pekerjaan kamu : ')
# print('Nama :',nama)
# print('Umur :',umur)
# print('Kelamin :',kelamin)
# print('Pekerjaan :',pekerjaan)

# x=4; y=3; z=2
# w=((x+y*z)/(x*y))**z
# print(w)

# angka=input('Silahkan masukkan angka berapapun :')
# hitung=int(angka)**2
# print('Kuadrat dari',angka,'=',hitung)

# usiaAndi = 40
# usiaBudi = 20
# print(usiaAndi * usiaBudi)
# print(usiaAndi / usiaBudi)
# print(usiaAndi + usiaBudi)
# print(usiaAndi - usiaBudi)
# print(usiaAndi % usiaBudi)
# print(usiaBudi ** 2)

# usiaAndi = 40
# usiaBudi = 20
# usiaAndi += 3
# # usiaAndi = usiaAndi + 3
# usiaBudi *= 4
# # usiaBudi = usiaBudi * 3
# print(usiaAndi)
# print(usiaBudi)

# import math
# print(math.pi)
# print(math.fabs(-4.7))
# print(math.pow(8, 2))
# print(math.sqrt(64))

# import math
# print(round(4.7))
# print(round(4.4))
# print(math.floor(4.7))
# print(math.ceil(4.4))

# x = 'Halo Dunia'
# print(len(x))
# print(x.index('Dunia'))
# print(x.split(' '))
# print(x.lower())
# print(x.upper())
# print(x.capitalize())

# singleQuotes = 'single quotes'
# doubleQuotes = "double quotes"
# combineQuotes = "wrap lot's of other quotes"
# print(singleQuotes)
# print(doubleQuotes)
# print(combineQuotes)

# text = "I'm Baron, nice to meet you"
# print(text[1])
# print(text[2:])
# print(text[:4])
# print(text[2:5])
# print(text[:])

# angka1 = input("Masukkan Angka 1 : ")
# angka2 = input("Masukkan Angka 2 : ")
# print(angka1 + angka2)
# print(int(angka1) + int(angka2))
# angka1 = float(angka1)
# angka2 = float(angka2)
# print(angka1 + angka2)

# usia = 22
# nama = 'Andi'
# print(usia + usia)
# print(nama + ' ' + nama)
# print(nama + ' ' + str(usia))

# day=input('Masukkan jumlah hari = ')
# a=int(day)
# tahun=int((a-(a%360))/360)
# b=a%360
# bulan=int((b-(b%30))/30)
# c=b%30
# minggu=int((c-(c%7))/7)
# hari=c-(minggu*7)
# print(day,'dalam tahun, bulan, minggu, hari, adalah',tahun,'tahun',bulan,'bulan',minggu,'minggu',hari,'hari')

nama='Halo Dunia'
#jumlah huruf 'a'
cari='a'
x=nama.upper().replace(cari.upper(), '')
print(x)
jmlCari=len(nama)-len(x)
print(f'Jumlah huruf \'{cari}\' ada = {jmlCari}')