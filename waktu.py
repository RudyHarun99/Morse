import datetime as dt
x=dt.datetime.now()

listhari={
     'Monday':'Senin',
     'Tuesday':'Selasa',
     'Wednesday':'Rabu',
     'Thursday':'Kamis',
     'Friday':'Jumat',
     'Saturday':'Sabtu',
     'Sunday':'Minggu'
}

listbulan={
    '1':'Januari',
    '2':'Februari',
    '3':'Maret',
    '4':'April',
    '5':'Mei',
    '6':'Juni',
    '7':'Juli',
    '8':'Agustus',
    '9':'September',
    '10':'Oktober',
    '11':'November',
    '12':'Desember'
}

class sekarang:
    def __init__(self):
        self.hari=listhari[x.strftime('%A')]
        self.tanggal=x.strftime('%d')
        self.bulan=listbulan[x.strftime('%m')]
        self.tahun=x.strftime('%Y')
        self.jam=x.strftime('%H')
        self.menit=x.strftime('%M')
        self.detik=x.strftime('%S')

waktu=sekarang()