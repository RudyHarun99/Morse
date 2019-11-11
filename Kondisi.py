# #Kondisi if adalah kondisi yang akan dieksekusi oleh program jika bernilai benar atau TRUE

# nilai = 9

# #jika kondisi benar/TRUE maka program akan mengeksekusi perintah dibawahnya
# if(nilai > 7):
#     print("Selamat Anda Lulus")

# #jika kondisi salah/FALSE maka program tidak akan mengeksekusi perintah dibawahnya
# if(nilai > 10):
#     print("Selamat Anda Lulus")
#     #Kondisi if else adalah jika kondisi bernilai TRUE maka akan dieksekusi pada if, tetapi jika bernilai FALSE maka akan dieksekusi kode pada else

# nilai = 3
# #Jika pernyataan pada if bernilai TRUE maka if akan dieksekusi, tetapi jika FALSE kode pada else yang akan dieksekusi.
# if(nilai > 7):
#     print("Selamat Anda Lulus")
# else:
#     print("Maaf Anda Tidak Lulus")
#     #Contoh penggunaan kondisi elif

# hari_ini = "Rabu"

# if(hari_ini == "Senin"):
#     print("Saya akan kuliah")
# elif(hari_ini == "Selasa"):
#     print("Saya akan kuliah")
# elif(hari_ini == "Rabu"):
#     print("Saya akan kuliah")
# elif(hari_ini == "Kamis"):
#     print("Saya akan kuliah")
# elif(hari_ini == "Jumat"):
#     print("Saya akan kuliah")
# elif(hari_ini == "Sabtu"):
#     print("Saya akan kuliah")
# elif(hari_ini == "Minggu"):
#     print("Saya akan libur")

# nilai=input('Nilai anda : ')
# x=int(nilai)
# if x>=82:
#     print('Grade anda A')
# elif x>=72 and x<=81:
#     print('Grade anda B')
# elif x>=62 and x<=71:
#     print('Grade anda C')
# elif x>=52 and x<=61:
#     print('Grade anda D')
# else:
#     print('Grade anda E')

# x=True; y=True
# if x and y:
#     print ('Anda x dan y')
# elif x and not y:
#     print('Anda x')
# elif not x and y:
#     print('Anda y')
# else:
#     print('Anda siapa?')

# x=True; y=False
# print(x and y)
# print(x or y)

days={
     'senin':'monday',
     'selasa':'tuesday',
     'rabu':'wednesday',
     'kamis':'thursday',
     'jumat':'friday',
     'sabtu':'saturday',
     'minggu':'sunday'
}
hari=input('Ketik nama hari (ENG/IDN) : ')
listind=list(days.keys())
listing=list(days.values())
if hari in listind:
    ind=listind.index(hari)
    ing=listing[ind]
    print('Bahasa Inggris dari',hari,'adalah',ing)
else:
    ing=listing.index(hari)
    ind=listind[ing]
    print('Bahasa Indonesia dari',hari,'adalah',ind)

# x=input('Masukkan massa : ')
# y=input('Masukkan tinggi : ')
# massa=int(x)
# tinggi=int(y)/100
# print('Massa',massa,'kg dan tinggi',tinggi,'m')
# imt=massa/tinggi**2
# if imt<18.5:
#     print('IMT =',round(imt,1),'artinya berat badan kurang')
# elif imt>=18.5 and imt<=24.9:
#     print('IMT =',round(imt,1),'artinya berat badan ideal')
# elif imt>=25.0 and imt<=29.9:
#     print('IMT =',round(imt,1),'artinya berat badan berlebih')
# elif imt>=30.0 and imt<=39.9:
#     print('IMT =',round(imt,1),'artinya berat badan sangat berlebih')
# else:
#     print('IMT =',round(imt,1),'artinya obesitas')

# a=input('Masukkan angka : ')
# angka=int(a)%2
# if angka==0:
#     print('Angka',a,'tergolong bilangan GENAP!')
# else:
#     print('Angka',a,'tergolong bilangan GANJIL!')