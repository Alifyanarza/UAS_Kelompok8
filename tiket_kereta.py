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
               print("Jadwal keberangkatan minggu ini: ")
               list_jadwal = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
               print("1. ", list_jadwal[0])
               print("2. ", list_jadwal[1])
               print("3. ", list_jadwal[2])
               print("4. ", list_jadwal[3])
               print("5. ", list_jadwal[4])
               print("6. ", list_jadwal[5])
               print("7. ", list_jadwal[6])
               hari=input("Pilih hari (dalam nomor sesuai list): ")
               if hari not in ['1', '2', '3', '4', '5', '6', '7']:
                   print("Nomor hari tidak valid, mohon inputkan antara 1-7")
                   break
               else:
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
               print("Jadwal keberangkatan minggu ini: ")
               list_jadwal = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
               print("1. ", list_jadwal[0])
               print("2. ", list_jadwal[1])
               print("3. ", list_jadwal[2])
               print("4. ", list_jadwal[3])
               print("5. ", list_jadwal[4])
               print("6. ", list_jadwal[5])
               print("7. ", list_jadwal[6])
               hari=input("Pilih hari (dalam nomor sesuai list): ")
               if hari not in ['1', '2', '3', '4', '5', '6', '7']:
                   print("Nomor hari tidak valid, mohon inputkan antara 1-7")
                   break
               else:
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
            else:
                print("")
                print("Kelas: ")
                Kelas=["Ekonomi","Bisnis"]
                for x in range (2):
                    print(x+1, kelas[x])
                kelas=input("Pilih kelas: ")
                if kelas=="1":
                    hari=input("Apakah weekend? (y/n): ")
                    if hari=="y":
                        print("Tiket kereta = Rp. 5000")
                    else:
                        print("Tiket kereta = Rp. 4000")
                elif kelas=="2":
                    hari=input("Apakah weekend? (y/n): ")
                    if hari=="y":
                        print("Tiket kereta = Rp. 9000")
                    else:
                        print("Tiket kereta = Rp. 7000")
                else:
                    print("Kelas tidak valid, mohon inputkan kelas 1/2!")
            print("")
            
            print("Kode pembayaran: ", no_ktp)
            print("Silahkan melakukan transaksi sesuai kode pembayaran anda di loket yang tersedia.")
            print("Terimakasih atas kepercayaannya, semoga selamat sampai tujuan.")
            print("Apakah anda ingin menghentikan program? (y/n): ")
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
        
                    
