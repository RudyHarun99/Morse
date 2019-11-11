# #Contoh cara membuat Dictionary pada Python

# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print ("dict['Name']: ", dict['Name'])
# print ("dict['Age']: ", dict['Age'])

# #Update dictionary python

# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# dict['Age'] = 8 # Mengubah entri yang sudah ada
# dict['School'] = "DPS School" # Menambah entri baru

# print ("dict['Age']: ", dict['Age'])
# print ("dict['School']: ", dict['School'])

# #Contoh cara menghapus pada Dictionary Python

# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# del dict['Name'] # hapus entri dengan key 'Name'
# dict.clear()     # hapus semua entri di dict
# del dict         # hapus dictionary yang sudah ada

# print ("dict['Age']: ", dict['Age'])
# # print ("dict['School']: ", dict['School'])

# andi={
#     'name':'Andi',
#     'age':22,
#     'is_married':False,
#     'job':'PNS',
#     'cars':['Alphard','Xpander','Innova'],
#     'address':{
#         'street':'Mawar Ungu',
#         'RT':5,'RW':121,'kecamatan':'X',
#         'zipcode':123456,
#         'geo':{
#             'lat':111.11,
#             'lng':65.89
#         }}}
# print(andi['name'])
# print(andi['age'])
# print(andi['is_married'])
# print(andi.get('name'))
# print(andi.get('age'))
# print(andi.get('is_married'))
# print(andi.get('job'))  #none krn ga ada 'job'
# #print(andi['job']) error krn ga ada 'job'
# print(type(andi))

# andi['name']='Budi' #ubah nilai 'name' jadi 'Budi'
# print(andi)
# print(andi['cars'][0])
# print(andi['address']['geo'])

# andi['salary']=25000000 #menambah key dan value
# andi.update({'no_ktp':123456789})
# print(andi)

# print(list(andi))   #dicetak hanya key saja
# print(andi.keys())  #cek ada key apa aja
# print(list(andi.keys()))
# print(andi.values())    #cek ada value apa aja
# print(list(andi.values()))

# days={
#     'senin':'monday',
#     'selasa':'tuesday',
#     'rabu':'wednesday',
#     'kamis':'thursday',
#     'jumat':'friday',
#     'sabtu':'saturday',
#     'minggu':'sunday'
# }
# hari=input('Ketik nama hari :')
# # print(f'{hari.upper()}={days.get(hari.lower(),"Ga ada!")}')
# listind=list(days.keys())
# listing=list(days.values())
# ing=listing.index(hari)
# ind=listind[ing]
# print(ind)

# x={1:True,2:False}
# print(list(x.items()))  #mencetak keys dan values