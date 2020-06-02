#Sumber : Program Tarif Parkir Bandara milik Elfira Vidian Paquita
#Program tiket kereta dimodifikasi dengan penggunaan list serta penambahan menu baru
#Menu yang ditambahkan yaitu menu refund dan costumer service

print ("Tarif Parkir")



while True : 
    gerbang=input("Pilih gerbang(1/2):")
    if gerbang=="2":
        roda=input("Jumlah roda(4/6):")
        if roda=="4":
            karcis=input("Apakah karcis ada?y/n:")
            if karcis=="n":
                biaya=100000
                print("Tarif Parkir:Rp",biaya)
            elif karcis=="y":
                w=float(input("Berapa lama anda parkir dalam jam?:"))
                if w>24: 
                    biaya=50000
                    print("Tarif Parkir:Rp",biaya)
                elif 12<w<=24:
                    biaya=55000
                    print("Tarif Parkir:Rp",biaya)
                elif 5<w<=12:
                    biaya=25000
                    print("Tarif Parkir:Rp",biaya)
                elif 5<w<1:
                    biaya=6000+2000*(w-1)
                    print("Tarif Parkir:Rp",biaya)
                else:
                    biaya=6000
                    print("Tarif Parkir:Rp",biaya)
        elif roda=="6":
            karcis=input("Apakah karcis ada?y/n:")
            if karcis=="n":
                tarif=100000
                print("Tarif Parkir:Rp",tarif)
            elif karcis=="y":
                waktu=float(input("Berapa lama anda parkir dalam jam?:"))
                if w>24:
                    biaya=70000
                    print("Tarif Parkir:Rp",biaya)
                elif 12<w<=24:
                    biaya=70000
                    print("Tarif Parkir:Rp",biaya)
                elif 5<w<=12:
                    biaya=35000
                    print("Tarif Parkir:Rp",biaya)
                elif 5<w<1:
                    biaya=8000+3500*(w-1)
                    print("Tarif Parkir:Rp",biaya)
            else:
                biaya=8000
                print("Tarif Parkir:Rp",biaya)
    else: 
        karcis=input("Apakah karcis ada?y/n:")
        if karcis=="n":
            biaya=50000
            print("Tarif Parkir:Rp",biaya)
        elif karcis=="y":
            w=float(input("Berapa lama anda parkir dalam jam?:"))
            if w<=24:
                biaya=3000
                print("Tarif Parkir:Rp",biaya)
            else:
                biaya=25000
                print("Tarif Parkir:Rp",biaya)
    p = input("Apakah anda ingin menghentikan program? y/n:")
    if p == 'y':
        break
        

                    
                    
    


