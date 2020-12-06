#No.4

sayur = ['Bayam', 'Kangkung', 'Wortel', 'Selada']
print ("----TOKO BELANJA SAYUR----")
print ("Silahkan dipilihan menu di bawah selanjutnya")
while True:
    print ("Menu: \nA. Tambah sayur lain \nB. Hapus data sayur \nC. Tampilkan keranjang \nD. Keluar \n")
    pilih = input ("Silahkan untuk anda Pilihan (Harusnya huruf BESAR) : ")
    if (pilih == 'A'):
        tambah = str ( input (" ketik 1 sayur ditambahkan : "))
        print (tambah, "Telahmasuk keranjang")
        sayur.append (tambah)
    elif (pilih == 'B'):
        i = False 
        while (i == False):
            try:
                hapus = str ( input ("Ketik satu sayur dihapus : "))
                print(hapus, "Sudah dihapus keranjang")
                i = False
            except:
                print ("Belum ada ketemu keranjang")
    elif (pilih == 'D'):
        keluar = input ("Mohon keluar dari memprogram? (y/n) : ")
        if keluar == 'y':
            break
