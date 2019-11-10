waktu=19
rasio1=1/7; rasio2=1/4; rasio3=1/2
ibu=round(((rasio2*waktu)+rasio3)/(rasio2-rasio1))
print('Usia ibu :',ibu)
anak=rasio1*ibu+waktu
print('Usia anak :',int(anak))
usialahir=ibu-anak
print('Usia ibu saat melahirkan :',int(usialahir))