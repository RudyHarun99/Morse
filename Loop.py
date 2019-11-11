# #Contoh penggunaan While Loop

# count = 0
# while (count < 9):
#     print ('The count is:', count)
#     count = count + 1

# print ("Good bye!")

# #Contoh pengulangan for sederhana
# angka = [1,2,3,4,5]
# for x in angka:
#     print(x)

# #Contoh pengulangan for
# buah = ["nanas", "apel", "jeruk"]
# for makanan in buah:
#     print ("Saya suka makan", makanan)

#     # Contoh penggunaan Nested Loop

# i = 2
# while(i < 100):
#     j = 2
#     while(j <= (i/j)):
#         if not(i%j): break
#         j = j + 1
#     if (j > i/j) : print (i, " is prime")
#     i = i + 1

# print ("Good bye!")

# students=['Andi','Budi','Caca','Deni']
# index=0
# while index <= len(students)-1:
#     print(students[index])
#     index+=1

# x=[1,2,3,4,5,6,7,8,9,10]
# y=[]
# index=0
# while index <= len(x)-1:
#     y.append(x[index]**2) #append(menambahkan) nilai(x index ke sekian dipangkat 2)
#     index+=1
# print(y)

# x=[1,2,3,4,5,6,7,8,9,10]
# y=[]
# index=0
# while index <= len(x)-1:
#     if index==4:
#         break   #break fungsinya untuk menghentikan
#     y.append(x[index]**2) #append(menambahkan) nilai(x index ke sekian dipangkat 2)
#     index+=1
# print(y)

# i=1
# while i<10:
#     print(i)
#     if i==5:
#         break   #berhenti di 5
#     i+=1

# a=0
# while a<10:
#     a+=1
#     if a==5:
#         continue    #bila nilai a=5, skip, lanjut ke proses lagi, jadi nilai 5, dilewat
#     print(a)

# password='12345'
# inputuser=''
# while inputuser!=password:
#     inputuser=input('Ketik Password : ')
#     if inputuser!=password:
#         print('Password Salah!')
#     else:
#         print('Password Benar!')

# password='12345'
# inputuser=''
# jumlahinput=1
# batasinput=5
# lebih=False
# while inputuser!=password and not lebih:
#     if jumlahinput<=batasinput:
#         inputuser=input('Password Salah! Ketik Password : ')
#         jumlahinput+=1
#     else:
#         lebih=True
# if lebih:
#     print('Kesempatan habis, tunggu 24 jam')
# else:
#     print('Password Benar!')

# password='12345'
# ketik=input('Ketik Password : ')
# chance=5
# state=False
# while state==False:
#     if ketik==password:
#         state=True
#         print('Password Benar')
#     else:
#         ketik=input('Password Salah! Ketik password : ')
#         chance-=1
#         if chance==0:
#             break

# kota=['Jakarta','Bandung','Surabaya']
# i=0
# while i<len(kota):
#     print(kota[i])
#     i+=1

# for i in range(len(kota)):
#     print(kota[i])

# for namaKota in kota:
#     print(namaKota)

# x='Purwadhika'
# for i in x:
#     print(i)

# x=[1,2,3,4,5]
# for i in x:
#     print(i)

# for i in range(5):
#     print(i)

# for i in range(2,5):
#     print(i)

# for i in range(2,10,2):
#     print(i)
# else:
#     print('OK')

# for i in range(2,10):
#     print(i)
#     if i==7:
#         break

# for i in range(2,10):
#     if i==7:
#         break
#     print(i)

# for i in range(2,10):
#     if i==7:
#         continue
#     print(i)

# for i in range(1,11):
#     if i%2==0:
#         print('WOW')
#     else:
#         print(i)

# def fizzbuzz(x):
#     for i in range(1,x+1):
#         if i%3==0:
#             print('Fizz')
#         elif i%5==0:
#             print('Buzz')
#         elif i%3==0 and i%5==0:
#             print('FizzBuzz')
#         else:
#             print(i)

# print(fizzbuzz(20))

# x=[1,2,3,4,5,6,7]
# y=[]
# for i in range(len(x)):
#     y.append((len(x))-i)
# print(y)

# x=[1,2,3,4,5,6,7]
# y=['Andi','Budi','Caca']
# def balikposisi(mylist):
#     hasil=[]
#     for i in range(len(mylist)):
#         hasil.insert(0,mylist[i])
#     return hasil
# print(balikposisi(x))
# print(balikposisi(y))

# x=[1,2,3,4,5,6,7]
# y=['Andi','Budi','Caca']
# def balikposisi(mylist):
#     for e in range(round(len(mylist)/2)):
#         asli=mylist[e]
#         mylist[e]=mylist[len(mylist)-1-e]
#         mylist[len(mylist)-1-e]=asli
#     return mylist
# print(balikposisi(x))
# print(balikposisi(y))

# x='Lintang'
# y=list(x)

# def ubahvokal(kata):
#     output=''
#     for huruf in kata:
#         if huruf in 'aiueo':
#             output=output+'o'
#         else:
#             output=output+huruf
#     return output
# print(ubahvokal('lintang'))
# print(ubahvokal('kambing'))

# def Palindrome(kata):
#     kata1=''
#     hasil=[]
#     for i in range(len(kata)):
#         hasil.insert(0,kata[i])
#         kata1 = kata1.join(hasil)
#     if kata == kata1:
#         cek = "Palindrome"
#     else:
#         cek = "Bukan Palindrome"
#     return cek
# print(Palindrome('bantal'))

# x='bantal'
# def palindrome(kata):
#     if kata==kata[::-1]:
#         return True
#     else:
#         return False
# print(palindrome(x))

# def palindrome2(kata):
#     for i in range(round(len(kata)/2)):
#         palindromekah=False
#         if kata[i]==kata[len(kata)-1-i]:
#             palindromekah=True
#         else:
#             palindromekah=False
#             break
#         return palindromekah
# print(palindrome2('katak'))
# print(palindrome2('oppok'))

# star=''
# for i in range(5):
#     star+=' * '
#     print(star)

# def star(x):
#     star=''
#     for i in range(x):
#         star+=' * '
#         print(star)        
# star(3)

# def rstar(x):
#     star=''
#     for i in range(x):
#         star=' * '*(x-i)
#         print(star)
# rstar(3)

# star=''
# for i in range(5):
#     star+=str(i+1)+' '
#     print(star)

# # no 1
# def star(x):
#     star=''
#     for i in range(x):
#         star+=str(i+1)+' '
#         print(star)
# star(5)

# # no 2
# def star(x):
#     for i in range(x):
#         star = ''
#         for j in range(1,x+1-i):
#             star+=str(j)+' '
#         print(star)
# star(5)

# # no 3
# def star(x):
#     star=''
#     for i in range(x):
#         star=(str(i+1)+' ')*(i+1)
#         print(star)
# star(5)

# #no 4
# def rstar(x):
#     star=''
#     for i in range(x):
#         star=(str(i+1)+' ')*(x-i)
#         print(star)
# rstar(5)

# #no 4
# def rstar(x):
#     for i in range(x):
#         star=''
#         k=x-i
#         for j in range(k):
#             star+=str(i+1)+' '
#         print(star)
# rstar(5)

# no 5
# def star(x):
#     star=''
#     for i in range(x):
#         star+=str(x-i)+' '
#         print(star)
# star(5)

# # no 6
# def star(x):
#     for i in range(x):
#         star = ''
#         for j in range(1,x+1-i):
#             star+=str((x+1)-j)+' '
#         print(star)
# star(5)

# #no 6
# def rstar(x):
#     for i in range(x):
#         star=''
#         k=x-i
#         for j in range(k):
#             star+=str(x-j)+' '
#         print(star)
# rstar(5)

# for i in range(5):  #0 1 2 3 4
#     for j in range(7,9):    #7 8
#         print(i,'dan',j)    #print i:0 dan j:0, print i:1 dan j:1, dst

# print(2**3) #2 pangkat 3
# print(pow(2,3)) #2 pangkat 3

# import math
# print(math.pow(2,3))    #2 pangkat 3

# def pangkat(x,y):   #function pangkat
#     hasil=1
#     for i in range(y):
#         hasil*=x
#     print(hasil)
# pangkat(4,3)

# def pangkatB(x,y):  #fungsi rekursif (fungsi memanggil fungsi di dalam dirinya sendiri)
#     if(y==1):
#         return x                    #pangkatB(2,3)=2*pangkatB(2,2)
#     else:                           #pangkatB(2,2)=2*pangkatB(2,1)
#         return x*pangkatB(x,y-1)    #pangkatB(2,1)=2
# print(pangkatB(4,3))

# def factorial(x):   #fungsi rekursif factorial
#     if x<=2:
#         return x
#     else:
#         return x*factorial(x-1)
# print(factorial(4))

# def faktorial(x):
#     angka=1
#     for i in range(1,x+1):
#         angka*=i
#     return angka
# print(faktorial(0))

# def rstar(x):
#     star=''
#     for i in range(x):
#         star=' * '*(x-i)
#         print(star)
# rstar(3)
# def star(x):
#     star=''
#     for i in range(x):
#         star+=' * '
#         print(star)        
# star(3)