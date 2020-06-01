print("PT. KAI")
print("")
print("Selamat datang di Stasiun Balapan, Silahkan pilih menu untuk melanjutkan")
print("|  1. Pesan tiket kereta")                                                               
print("|  2. Panduan refund tiket kereta")                                                                 
print("|  3. Customer service")
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
               else:
                hari=input("Apakah weekend? (y/n): ")
                if hari=="y":
                    print("Tiket kereta = Rp. 4000")
                else:
                    print("Tiket kereta = Rp. 3000")
                    
