print("PT. KAI")
print("Alamat: Jalan Wolter Monginsidi No.112, Kestalan, Kec. Banjarsari, Kota Surakarta, Jawa Tengah 57713")
print("")
print("Selamat datang di Stasiun Balapan, Silahkan pilih menu untuk melanjutkan")
list_Menu = ["Pemesanan tiket", "Panduan refund tiket", "Customer Service"]
print("1. ", list_Menu[0])
print("2. ", list_Menu[1])
print("3. ", list_Menu[2])
print("=====================================")
while (True):
    menu=input("Pilih menu: ")
    if menu == "1":
            nama=input("Nama: ")
            no_ktp=input("Nomor KTP: ")
            tanggal=input("Tanggal keberangkatan (dd/mm/yy): ")
            print("")
            Tujuan=["Stasiun Purwosari","Stasiun Maguwo","Stasiun Tugu"]
            for n in range (3):
                print(n+1,Tujuan[n])
            tujuan=input("Pilih tujuan: ")
            if tujuan== "1":
                print("")
                print("Kelas:")
                Kelas=["Ekonomi","Bisnis"]
                for x in range (2):
                    print(x+1, Kelas[x])
                kelas=input("Pilih kelas: ")
                if kelas=="1":
                    hari=input("Apakah weekend? (y/n): ")
                    if hari=="y":
                        print("Tiket kereta = Rp. 2000")
                    else:
                        print("Tiket kereta = Rp. 1000")
                elif kelas=="2":
                    hari=input("Apakah weekend? (y/n): ")
                    if hari=="y":
                        print("Tiket kereta = Rp. 4000")
                    else:
                        print("Tiket kereta = Rp. 3000")
                else:
                    print("Kelas tidak valid, mohon inputkan kelas 1/2!")
             elif tujuan=="2":
                print("")
                print("Kelas:")
                Kelas=["Ekonomi","Bisnis"]
                for x in range (2):
                    print(x+1, Kelas[x])
                kelas=input("Pilih kelas: ")
                if kelas=="1"
                    hari=input("Apakah weekend? (y/n): ")
                    if hari=="y":
                         print("Tiket kereta = Rp. 3000")
                    else:
                         print("Tiket kereta = Rp. 2000")
                elif kelas=="2":
                    hari=input("Apakah weekend? (y/n): ")
                    if hari=="y":
                         print("Tiket kereta = Rp. 5000")
                    else:
                         print("Tiket kereta = Rp. 4000")
                else:
                    print("Kelas tidak valid, mohon inputkan kelas 1/2!")
                
                    
