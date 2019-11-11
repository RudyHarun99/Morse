# #class=cetakan object
# class mobil:
#     warna='merah'
#     tahun=2010
# print(mobil)
# print(type(mobil))

# #create object mobil1
# mobil1=mobil()
# print(mobil1)
# print(mobil1.warna)
# print(mobil1.tahun)

# mobil2=mobil()
# print(mobil2.warna)
# print(mobil2.tahun)

# class MobilCustom():
#     def __init__(self,warna,tahun,model): #garisbawahnya dua
#         self.color=warna
#         self.year=tahun
#         self.model=model
#     #method
#     def jadul(self):
#         if self.year<2010:
#             return True
#         else: return False
#     def tes(self):
#         print(self.color,self.year,self.model,self.jadul())

# #syntatic sugar
# mobil1=MobilCustom('pink','','X')
# mobil2=MobilCustom('blue',2010,['A','B'])
# print(mobil1.year)
# print(mobil2.model)

# mobilA=MobilCustom('merah',1998,'X')
# mobilB=MobilCustom('merah',2018,'Z')
# print(mobilA.year)
# print(mobilA.jadul())

# print(mobilA.tes())

# class mobil:
#     def __init__(self,color,seat):
#         self.warna=color
#         self.bangku=seat

# # class car(mobil):   #inheritance
# #     def __init__(self,soundsys):
# #         self.suara=soundsys

# class car(mobil):   #inheritance cara1
#     pass

# class car(mobil):   #inheritance cara2
#     def __init__(self,color,seat):
#         mobil.__init__(self,color,seat)

# class car(mobil):   #inheritance cara3
#     def __init__(self,color,seat):
#         super().__init__(color,seat)

# mobil1=mobil('pink',4)
# car1=car('black',8)
# print(mobil1.warna,mobil1.bangku)
# print(car1.warna,car1.bangku)
# print(car1.warna,car1.bangku)

# class X:
#     def __init__(self,nama,gelar):
#         self.nama=nama
#         self.gelar=gelar

# class Y(X):
#     def __init__(self,nama,gelar,univ):
#         super().__init__(nama,gelar)
#         self.kampus=univ

# objX = X('Andi','M.Sc')
# objY = Y('Budi','Dr.','UNPAD')
# objZ = Y('Caca','S.T','UI')
# print(objY.nama,objY.gelar,objY.kampus)

# from pprint import pprint
# pprint(vars(objY))

# print(vars(objX))
# print(vars(objY))

# print(objY.nama)
# print(getattr(objY,'nama'))     #ambil nilai atribut 'nama'
# print(hasattr(objY,'warna'))    #cek apakah punya atribut 'warna' hasilnya True or False
# print(hasattr(objY,'usia'))     #cek apakah punya atribut 'usia'

# objY.warna='merah'
# print(vars(objY))
# objZ.usia=23
# print(vars(objZ))
# setattr(objZ,'alamat','BSD')
# print(vars(objZ))
# delattr(objZ,'alamat')
# print(vars(objZ))

# class a:
#     nama='A'
#     usia=21

# obja=a()
# print(obja.nama)
# print(obja.usia)

# del a.nama  #menghapus atribut nama di class a
# print(obja.usia)
# # print(obja.nama)

# class student:
#     def __init__(self,nama,usia):
#         self.name=nama
#         self.age=usia

# data=[
#     {'nama':'Andi','usia':21},
#     {'nama':'Budi','usia':22},
#     {'nama':'Caca','usia':23},
#     {'nama':'Deni','usia':24}
# ]

# Andi=student('Andi',21)
# Budi=student('Budi',22)
# Caca=student('Caca',23)
# Deni=student('Deni',24)

# def createobj(i):
#     nama=i['nama']
#     vars()[nama]=student(i['nama'],i['usia'])
#     return vars()[nama]

# datanew=list(map(createobj,data))
# print(datanew[0].name)
# print(datanew[0].age)

# def createobj(i):
#     return student(i['nama'],i['usia'])

# datanew=list(map(createobj,data))
# print(datanew[0].name)
# print(datanew[0].age)

# datanew=list(map(lambda i:student(i['nama'],i['usia']),data))
# print(datanew[0].name)
# print(datanew[0].age)

# class persegi:
#     def __init__(self,sisi):
#         self.sisi=sisi
#         self.keliling=self.sisi*4
#         self.luas=self.sisi**2

# persegiA=persegi(4)
# persegiB=persegi(8)
# persegiC=persegi(10)
# print(vars(persegiA))
# print(vars(persegiB))
# print(vars(persegiC))

#class keromawi PR
#class keangkalatin PR

# class manusia:
#     def __init__(self,nama):
#         self.name=nama

# obja=manusia('Andi')
# print(vars(obja))

# class orang:
#     nama='Budi'

# objb=orang()
# print(objb.nama)

# class pria(manusia):  #inheritance dari manusia
#     pass

# class pria(manusia):    #inheritance dari manusia
#     def __init__(self,nama):
#         manusia.__init__(self,nama)
#         self.gender='Laki-laki'

# class wanita(manusia):
#     def __init__(self,nama):
#         manusia.__init__(self,nama)
#         self.gender='Perempuan'

# obja=manusia('Andi')
# objb=pria('Andi')
# objc=wanita('Andi')
# print(vars(obja))
# print(vars(objb))
# print(vars(objc))

# multilevel inheritance
# class X:
#     def __init__(self,x):
#         self.a=x

# class Y(X): #inheritance dari x
#     def __init__(self,x,y):
#         X.__init__(self,x)
#         self.b=y

# class Z(Y): #inheritance dari y
#     def __init__(self,x,y,z):
#         Y.__init__(self,x,y)
#         self.c=z

# obja=Z('Andi','PNS',True)
# print(vars(obja))

# multiple inheritance
# class X:
#     def __init__(self,name,age):
#         self.nama=name
#         self.usia=age
#     def pensiun(self):
#         return 55-self.usia

# class Y(X):
#     def __init__(self,name,age,city):
#         X.__init__(self,name,age)
#         self.kota=city
# objB=X('Banu',19)
# objA=Y('Ali',12,'Jakarta')
# print(objA.kota)

# multiple inheritance
# class karnivora:
#     def __init__(self):
#         self.daging=True
#         self.nama='Karnivora'

# class herbivora:
#     def __init__(self):
#         self.tumbuhan=True
#         self.nama='Herbivora'

# class omnivora(karnivora,herbivora):    #inheritance dari karnivora dan herbivora
#     def __init__(self):
#         karnivora.__init__(self)
#         herbivora.__init__(self)
#         self.mcD=True
#         self.nama='Omnivora'

# obja=omnivora()
# print(vars(obja))
# print(omnivora.__mro__)