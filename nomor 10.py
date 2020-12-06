buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print ("-----Memprogram dijualna buah-----")
print ("Daftar harga buat buah kilogram")
print (buah)
harga = []
while True :
    beli = input ("Silahkan nama buah dibeli  angka  : ")
    if beli:
        try:
            kilo = int ( input ("Perhitungan jumlah kilogram             : "))
            harga1 = kilo * buah
            konfirmasi = input ("Anka keingina membali buah lagi? : ")
            if (konfirmasi != 'y'):
                print("Total harga                 : Rp", harga)
                break    
        except:
            print ("Silahkan, masuk jumlah kilo gram valid")
    elif (beli == '') or (Membeli not in buah):
        print ("Ayo,Dibeli buah yang harga lebih murah")
        print ("Buah yang ingin Anda beli tidak ada di daftar")
