buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
status = True
print ("-----memprogram penjualan buah-----")
print ("Yuuk,daftar harga buah kilo gram")
while (status == True):
    print ("\nMenu : ")
    print ("A. Beli buah \nB. Tambah daftar harga buah \nC. Hapus buah dari daftar harga \nD. Keluar dari aplikasi")
    menu = input ("Pilihan Anda (huruf BESAR) : ")
    print() 
    harga = []
    if (menu == 'A'):
        while True :
            beli = input ("Silahkan anda ingin membeli buah nama apa : ")
            if beli:
                try:
                    kilo = int ( input ("Perhitungan jumlah kilo gram       : "))
                    konfirmasi = input ("\nIngin beli buah lagi? (y/n) : ")
                    if (konfirmasi != 'y'):
                        print("Total harga                 : Rp",harga)
                        break    
                except:
                    print ("Silahkan,masuk jumlah kilogram yang valid")
            
            elif (beli == '') or (beli not in buah):
                print ("Ayo,Dibeli buah yang harga lebih murah")
                print ("Buah yang ingin Anda beli tidak ada di daftar")
            
    elif (menu == 'B'):
        i = True
        while (i == True) :
            buah_baru = input ("Silahkan anda ingin membeli buah nama apa :")
            if (buah_baru in buah):
                print (buah_baru, "sudah ada daftar didalam yang baru")
            elif (buah_baru not in buah):    
                try:
                    harga_baru = int ( input ("Harga kilo gram : Rp"))
                    print (buah_baru, "Hasilnya tambah")
                    print ("Daftar harga yang terbaru")
                    for data in buah:
                        print ("( Harga Rp",buah.get(data1),")")
                        i = False
                    print()
                except:
                    print ("Masuk harga yang valid")
    elif (menu == 'C'):
        j = True
        while (j == True):
            hapus = input ("Nama buah yang akan dihapus : ")
            if (hapus not in buah):
                print ("Buah", hapus, "Disini tidak ada daftar")
            elif (hapus in buah):
                del buah[hapus]
                print ("Daftar yang harga terbaru")
                for data in buah:
                        print ("( Harga Rp",buah.get(data1),")")
                j = False
    elif (menu == 'D'):
        print("Terimakasih telah datang kami")
        break
