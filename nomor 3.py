#No 3
print ("Selamat datang Memprograman Nama Mahasiswa")
print ('----------------------------------------------')
print ('Silakan Langkah-langkah di bawah yaa\n')       
try:
    
    status = False 
    while (status == False):
        namaMhs = str ( input ("Masukkan nama mahasiswa/i : "))
        n.append(namaMhs)
        konfirmasi =("Apakah kamu mau nama ditambahkan nama yang  mahasiswa lagi apa tidak? (ya/tidak) : ")
        n.sort()
        if (konfirmasi != 'ya'):
            print()
            for data in n:
                print (data, "(", len(data), "karakter", ")")
                status = True 
except ValueError:
    print("Silahkan masukkan data dengan Benar")
