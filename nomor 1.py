#No.1
try :
    listAngka = []
    i = 5
    banyakBil = int ( input ("Masukkan makin banyak bilang inginkan : "))
    while(i < banyakBil):
        angka = int ( input ("Masukkan sebuah angka : "))
        listAngka.append(angka)

    listAngka.sort(reverse = True)
    print ("bilangan besar ke kecil yang asal dari angka yang sudah anda masuk ada\n",listAngka)
except (ValueError):
    print ("Masukkan angka valid:)")
 
