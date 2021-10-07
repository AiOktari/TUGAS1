listnama = []
listtelepon = []

while True:
    print("Selamat Datang!")
    print("--Menu--")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    pilihan = int(input("Silahkan pilih menu yang anda inginkan = "))
    
    if pilihan == 1:
        for x in listnama:
            print("Nama:",x)
            for y in listtelepon:
                if x == y:
                    print("No. Telepon: ",y)
    
    elif pilihan == 2:
        nama = input("Nama : ")
        listnama.append(nama) 
        telepon = input("No. Telepon: ")
        listtelepon.append(telepon)
    elif pilihan == 3:
        print("Program selesai, sampai jumpa!")
        break
    else:
        print("Menu tidak tersedia.")


