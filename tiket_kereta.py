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
            print("Daftar kereta: ")
            list_kereta = ["Kereta Kencana", "Kereta Argo"]
            print("1. ", list_kereta[0])
            print("2. ", list_kereta[1])
            kereta=input("Pilih Kereta: ")
            if kereta=="1":
                   print("Jadwal keberangkatan")
                   tanggal=input("Tanggal keberangkatan (hh/bb/tt): ")
                   print("Daftar jam keberangkatan: ")
                   list_jam = ["06.00", "12.00", "18.00"]
                   print("1. ", list_jam[0])
                   print("2. ", list_jam[1])
                   print("3. ", list_jam[2])
                   jam=input("Pilih jam (dalam nomor 1-3 sesuai daftar): ")
                   if jam not in ['1', '2', '3']:
                       print("Nomor jam tidak valid, mohon inputkan antara 1-3")
                       break
                   else:
                       print("Jadwal berhasil di booking, silahkan lanjut!")
            elif kereta=="2":
                   print("Jadwal keberangkatan")
                   tanggal=input("Tanggal keberangkatan (hh/bb/tt): ")
                   print("Daftar jam keberangkatan: ")
                   list_jam = ["09.00", "15.00", "21.00"]
                   print("1. ", list_jam[0])
                   print("2. ", list_jam[1])
                   print("3. ", list_jam[2])
                   jam=input("Pilih jam (dalam nomor 1-3 sesuai daftar): ")
                   if jam not in ['1', '2', '3']:
                       print("Nomor jam tidak valid, mohon inputkan antara 1-3")
                       break
                   else:
                       print("Jadwal berhasil di booking, silahkan lanjut!")
            else:
                print("Mohon inputkan nomor kereta antara 1-2!")
                break
            
            print("")
            print("Daftar Tujuan: ")
            Tujuan=["Stasiun Purwosari","Stasiun Maguwo","Stasiun Tugu"]
            for n in range (3):
                print(n+1,Tujuan[n])
            tujuan=input("Pilih tujuan: ")
            if tujuan== "1":
                print("")
                print("Kelas: ")
                Kelas=["Ekonomi","Bisnis"]
                for x in range (2):
                    print(x+1, Kelas[x])
                kelas=input("Pilih kelas: ")
                if kelas=="1":
                    pesan=input("Jumlah tiket yang dipesan (1 orang maksimal dapat memesan 3 tiket): ")
                    if pesan=="1":
                        D = 1*2000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="2":
                        D = 2*2000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="3":
                        D = 3*2000
                        print("Total harga tiket anda sebesar Rp.", D)
                    else: 
                        print("Maksimal pemesanan adalah 3 tiket!")
                        break      
                elif kelas=="2":
                    pesan=input("Jumlah tiket yang dipesan (1 orang maksimal dapat memeasan 3 tiket):")
                    if pesan=="1":
                        D = 1*4000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="2":
                        D = 2*4000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="3":
                        D = 3*4000
                        print("Total harga tiket anda sebesar Rp.", D)
                    else:
                        print("Maksimal pemesanan adalah 3 tiket!")
                        break
                else:
                    print("Kelas tidak valid, mohon input kelas 1/2!")
            elif tujuan=="2":
                print("")
                print("Kelas: ")
                Kelas=["Ekonomi","Bisnis"]
                for x in range (2):
                    print(x+1, Kelas[x])
                kelas=input("Pilih kelas: ")
                if kelas=="1":
                    pesan=input("Jumlah tiket yang dipesan (1 orang maksimal dapat memesan 3 tiket): ")
                    if pesan=="1":
                        D = 1*3000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="2":
                        D = 2*3000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="3":
                        D = 3*3000
                        print("Total harga tiket anda sebesar Rp.", D)
                    else: 
                        print("Maksimal pemesanan adalah 3 tiket!")
                        break
                elif kelas=="2":
                    pesan=input("Jumlah tiket yang dipesan (1 orang maksimal dapat memesan 3 tiket): ")
                    if pesan=="1":
                        D = 1*5000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="2":
                        D = 2*5000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="3":
                        D = 3*5000
                        print("Total harga tiket anda sebesar Rp.", D)
                    else: 
                        print("Maksimal pemesanan adalah 3 tiket!")
                        break
                else:
                    print("Kelas tidak valid, mohon inputkan kelas 1/2!")
            elif tujuan=="3":
                if kelas=="1":
                    pesan=input("Jumlah tiket yang dipesan (1 orang maksimal dapat memesan 3 tiket): ")
                    if pesan=="1":
                        D = 1*3000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="2":
                        D = 2*3000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="3":
                        D = 3*3000
                        print("Total harga tiket anda sebesar Rp.", D)
                    else: 
                        print("Maksimal pemesanan adalah 3 tiket!")
                        break
                elif kelas=="2":
                    pesan=input("Jumlah tiket yang dipesan (1 orang maksimal dapat memesan 3 tiket): ")
                    if pesan=="1":
                        D = 1*5000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="2":
                        D = 2*5000
                        print("Total harga tiket anda sebesar Rp.", D)
                    elif pesan=="3":
                        D = 3*5000
                        print("Total harga tiket anda sebesar Rp.", D)
                    else: 
                        print("Maksimal pemesanan adalah 3 tiket!")
                        break
                else:
                    print("Kelas tidak valid, mohon inputkan kelas 1/2!")
            else:
                print("Tujuan tidak valid, mohon inputkan kelas 1/2/3!")       
            print("Kode pembayaran: ", no_ktp)
            print("Silahkan melakukan transaksi sesuai kode pembayaran anda di loket yang tersedia.")
            print("Terimakasih atas kepercayaannya, semoga selamat sampai tujuan.")
            o=input("Apakah anda ingin menghentikan program? (y/n): ")
            if o=='y':
                break              
    elif menu=="2":
        print("Panduan refund tiket kereta:")
        print("1. Isi formulir pembatalan disertai keterangan pembatalan tiket")
        print("2. Sertakan bukti transaksi")
        print("3. Serahkan kepada petugas loket yang tersedia")
        print("")
        print("Terimakasih!")
    elif menu=="3":
        print("Mohon hubungi kontak kami apabila ada kendala dan meminta bantuan.")
        listCS = ["(0271)714039", "121 / (021)121", "09.00-16.00"]
        print("Office phone : ", listCS[0])
        print("Contact center : ", listCS[1])
        print("Jam pelayanan : ", listCS[2])
        print("")
        print("Terima kasih")
    else:
        print("Menu tidak valid, pilih menu 1-3!")
        ulang=input("Kembali ke menu (y/n)?")
        if ulang=='y':
            continue
        
                    
