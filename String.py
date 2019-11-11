# string
print("Jum'at")
print('Jum\'at')
print('Purwadhika\tSchool') #tab
print('Purwadhika\nSchool') #newline
nama = 'Purwadhika'
print(nama + ' School')
print(nama,'School')
nama = 'Rudy'
usia = 36
print('Saya '+nama+' usia '+str(usia))
print('Saya',nama,'usia',usia)
print('Saya %s usia %d'%(nama,usia))
print('Saya {} usia {}'.format(nama,usia))
print(f'Saya {nama} usia {usia}')
nama = 'Rudy Harun'
print(nama.lower())
print(nama.upper())
x = 'hahaha'
print(x.islower())
print(x.isupper())
print(nama.lower().isupper())
print(nama.upper().islower())
print(len(nama))
print(len(nama)+4)
print(nama[0])
print(nama[0:8])
print(nama[3:len(nama):2])
print(nama[-2])
print(nama.index('H'))
print(nama.index('u'))
print(nama.replace('Harun','Boy'))
print(len(nama.replace(' ','')))
nama='Purwadhika Startup & Coding School'
print(len(nama.replace(' ','')))
print(nama.lower().count('startup'))
print(nama.lower().count('c'))

kutipantiga = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (kutipantiga)

nama='Hari ini Hari tidak masuk sekolah'
#jumlah huruf 'h'
cari='h'
x=nama.upper().replace(cari.upper(), '')
print(x)
jmlCari=len(nama)-len(x)
print(f'Jumlah huruf \'{cari}\' ada = {jmlCari}')

nama='Hari ini Hari tidak masuk sekolah karena hari Minggu'
#jumlah huruf 'hari'
cari='hari'
x=nama.upper().replace(cari.upper(), '')
print(x)
jmlCari=int((len(nama)-len(x))/len(cari))
print(f'Jumlah kata \'{cari}\' ada = {jmlCari}')

x='abcdefghijklmnopqrstuvwxyz'
print(x[0])
print(x[0:10])      #start:end
print(x[:10])       #start:end (klo start 0)
print(x[0:10:2])    #start:end:step
print(x[:10:2])     
print(x[::2])       #start:end:step (klo start dan end 0)
print('g' in x)     #mencari 'g' di x true/false
print(x.count('g')) #menghitung 'g' di x

x='abcdefghijklmnopqrstuggvwxyzg'
print(x.count('g')) #menghitung 'g' di x

kalimat='Hari ini Andi tidak kuliah'
cari='h'
print(cari.lower() in kalimat.lower())
print(kalimat.lower().count(cari.lower()))