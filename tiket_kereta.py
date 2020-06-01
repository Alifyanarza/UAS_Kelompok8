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
