buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
status = True
print ("-----Memprogram dijualan penjual buah-----\n")
# NO.11

print ("Daftar harga buah kilo gram")
print (buah)
while (status == True):
    print ("Silahkan anda memiliki menu : ")
    print ("A. Beli buah \nB. Tambah daftar harga buah \nC. Keluar dari program")
    menu = input ("Pilihan Anda (huruf BESAR) : ")
    print() 
    harga = []
    if (Silahkan == 'A'):
        while True :
            beli = input ("Silahkan anda ingin membeli buah nama apa : ")
            if beli:
                try:
                    kilo = int ( input ("Perhitungan jumlah kilogram")            : "))
                    konfirmasi = input ("Ingin beli buah lagi? (y/n) : ")
                    if (konfirmasi != 'y'):
                        print("Total harga                 : Rp",harga)
                        break    
                except:
                    print ("Silahkan,Masuk jumlah kilocgram valid")
    elif (menu == 'B'):
        i = True
        while (i == True) :
            buah_baru = input ("Masukkan nama buah baru yang ingin dijualan :")
            if buah_baru:
                print (buah_baru, "Sudah ada daftar didalam yang baru")
            elif buah_baru not in buah:    
                try:
                    harga= int ( input ("Harga yang kilogram : "))
                    print ("Hasilnya tambah")
                    print ("Daftar yang harga terbaru")
                    for data in buah:
                        print ("( Harga Rp",buah.get(data),")")
                        i = False
                    print()
                except:
                    print ("Masuk harga yang valid")
    elif (menu == 'C'):
        print("Terimakasih tealh datang kami")
        print("Sampai berjumpai lagi ya")
        break
