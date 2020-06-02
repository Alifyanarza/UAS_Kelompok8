# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:06:53 2020

@author: ACER
"""

print("PT. KAI")
print("Alamat: Jalan Wolter Monginsidi No.112, Kestalan, Kec. Banjarsari, Kota Surakarta, Jawa Tengah 57713")
print("=====================================")
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
            if tujuan=="1":
                 print("")
                 print("Kelas:")
                 Kelas=["Ekonomi","Bisnis"]
                 for x in range (2):
                     print(x+1,Kelas[x])
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
                     print(x+1,Kelas[x])
                 kelas=input("Pilih kelas: ")
                 if kelas=="1":
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
                 print("Kelas:")
                 Kelas=["Ekonomi","Bisnis"]
                 for x in range (2):
                     print(x+1,Kelas[x])
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
        print("Office phone  : ", listCS[0])
        print("Contact center: ", listCS[1])
        print("Jam pelayanan : ", listCS[2])
        print("")
        print("Terima kasih")
    else:
        print("Menu tidak valid, pilih menu 1-3!")
        ulang=input("Kembali ke menu (y/n)? ")
        if ulang=='y':
            continue
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    