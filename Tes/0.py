# r untuk read
# data=open('data.txt','r')

# a untuk append
# data=open('data.txt','a')

# w untuk write
# data=open('data.txt','w')
# data.write('Coba')
# data.write('\nCoding Python')

# print(data.readable())
# data=open('filebaru.txt','w')
# data.write('FileBaru')
# print(data.read())
# print(data.readlines())
# print(data.readline(2))

# data=open('data.py','w')
# data.write('x=12')

# data=open('data.py','a')
# data.write('\nprint(x)')

# copy isi data.txt ke data.py
# buka dulu datanya
# data=open('data.txt','r')
# masukkan bacaan data ke variabel
# x=data.read()
# buka file data.py
# data=open('data.py','w')
# write variabel yg ada isi data.txt
# data.write(x)

# data=open('data.txt','r')
# x=data.read().split(', ')[::-1]

# output=open('x.txt','a')
# for i in x:
#     output.write(i+'\n')

# baca file di dalam folder data
# data=open('./data/data.csv','r')

# baca file di luar folder python
# data=open('./../data.csv','r')

# data=open('file.csv','r')
# x=data.read().split('\n')
# mylist=[]
# for i in x:
#     mylist.append(i.split(','))
# print(mylist)

# membaca csv menjadi list
# import csv
# with open('0.csv','r') as x:
#     baca=csv.reader(x)
#     print(list(baca))

# # mengubah list menjadi dictionary
# x=['no','nama']
# y=[12,'Andi']
# print(dict(zip(x,y)))

# # membaca csv menjadi dictionary
# import csv
# with open('0.csv','r') as x:
#     baca=csv.DictReader(x)
#     for i in baca:
#         print(dict(i))

# # menulis csv dari python
# import csv
# data=[
#     {'nama':'Andi'},
#     {'nama':'Budi'},
#     {'nama':'Caca'}
# ]
# # newline=untuk memisahkan antar row
# with open('0.csv','w',newline='') as x:
#     kolom=['nama']
#     a=csv.DictWriter(x,fieldnames=kolom) # memasukkan nilai header kolom
#     a.writeheader() # untuk menulis header kolom
#     a.writerows(data)

# import csv
# data=[
#     {'nama':'Andi','usia':21,'kota':'jakarta'},
#     {'nama':'Budi','usia':21,'kota':'jakarta'},
#     {'nama':'Caca','usia':21,'kota':'jakarta'}
# ]

# # delimiter, tanda pemisah antar data (,:!|)
# with open('0.csv','w',newline='') as x:
#     kolom=['nama','usia','kota']
#     a=csv.DictWriter(x,fieldnames=kolom,delimiter='!')
#     a.writeheader()
#     a.writerows(data)

# cara membaca file json dari python
import json
with open('1.json','r') as x:
    out=json.load(x)
print(out)
print(type(out))
print(type(out[0]))

# menulis file json baru diisi dengan isi 1.json
with open('haha.json','w') as y:
    json.dump(out,y)