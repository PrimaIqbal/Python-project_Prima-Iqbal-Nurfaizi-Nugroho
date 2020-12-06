# NO.7
nama_buah = []
harga_buah = []
def buahMurah(buah) :

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
buahMahal(buah)
    for x,v in buah.items() :
        d = "%s : %d" % (x,v)
    nilai_max = max(harga_buah)
    i = 0
    while i != len(harga_buah) :
        if nilai_max in list_harga :
            print(nama_buah[i])
        i += 1
    return d

