days={
    'senin':'monday',
    'selasa':'tuesday',
    'rabu':'wednesday',
    'kamis':'thursday',
    'jumat':'friday',
    'sabtu':'saturday',
    'minggu':'sunday'
}
hari=input('Ketik nama hari :')
# print(f'{hari.upper()}={days.get(hari.lower(),"Ga ada!")}')
listind=list(days.keys())
listing=list(days.values())
ing=listing.index(hari)
ind=listind[ing]
print(ind)