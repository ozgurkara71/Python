# import time
ayakkabi_barkod = {}
ayakkabi_bilgiler = {}
fonksiyon_say = 0
barkod_liste = []
last_barkod = 0
def dosyadan_alma():
    global fonksiyon_say
    global ayakkabi_barkod
    global ayakkabi_bilgiler
    global barkod_liste
    global last_barkod
    with open("21100011022.txt", "a+") as file_obj:
        file_obj.seek(0)
        line = file_obj.readline()
        if len(line) == 0:
            return
        else:
            file_obj.seek(0)
            for line in file_obj:
                (key, value) = line.split()
                if key == "Barkod:":
                    barkod = value
                    bool = False
                elif key == "tur:":
                    ayakkabi_bilgiler["tur"] = value
                elif key == "marka:":
                    ayakkabi_bilgiler["marka"] = value
                elif key == "fiyat:":
                    ayakkabi_bilgiler["fiyat"] = value
                elif key == "no:":
                    ayakkabi_bilgiler["no"] = value
                ayakkabi_barkod[barkod] = ayakkabi_bilgiler
                if bool == False:
                    ayakkabi_bilgiler = {}
                    bool = True
            keyss = list(ayakkabi_barkod.keys())
            keyss.sort()
            last_barkod = keyss[len(keyss) - 1]
            file_obj.seek(0)

def ekleme():
    print("<<<<<<<<<<<<<<<<<<<<<<<<<EKLEME EKRANI>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    with open("21100011022.txt", "a") as file_obj:
        global ayakkabi_barkod
        global ayakkabi_bilgiler
        global last_barkod
        son_girilen_barkodlar = []
        last_barkod = int(last_barkod)
        adet = int(input("Kac adet ayakkabi gireceksiniz: "))
        for i in range(adet):
            ayakkabi_bilgiler = {}
            last_barkod += 1
            barkod = last_barkod
            barkod = str(barkod)
            son_girilen_barkodlar.append(barkod)
            while True:
                tur = input("{}. ayakkabinin turunu(spor, dag...) girin: ".format(i+1))
                if tur.find(" ") == -1:
                    break
                else:
                    print("UYARI: degerleri girerken bosluk yerine alttan tire(_) kullanin!")
            while True:
                marka = input("{}. ayakkabinin markasini girin: ".format(i+1))
                if marka.find(" ") == -1:
                    break
                else:
                    print("UYARI: degerleri girerken bosluk yerine alttan tire(_) kullanin!")
            while True:
                fiyat = input("{} ayakkabinin fiyatini(TL) girin: ".format(i+1))
                if fiyat.find(" ") == -1:
                    break
                else:
                    print("UYARI: degerleri girerken bosluk yerine alttan tire(_) kullanin!")
            while True:
                no = input("{}. ayakkabinin numarasini girin: ".format(i+1))
                if no.find(" ") == -1:
                    break
                else:
                    print("UYARI: degerleri girerken bosluk yerine alttan tire(_) kullanin!")
            ayakkabi_bilgiler["tur"] = tur
            ayakkabi_bilgiler["marka"] = marka
            ayakkabi_bilgiler["fiyat"] = fiyat
            ayakkabi_bilgiler["no"] = no
            ayakkabi_barkod[barkod] = ayakkabi_bilgiler
        for key2, value2 in ayakkabi_barkod.items():
            if key2 in son_girilen_barkodlar:
                file_obj.write('Barkod: %s\n' % (key2))
                for key3, value3 in value2.items():
                    file_obj.write('%s: %s\n' % (key3, value3))

def listeleme():
    print("<<<<<<<<<<<<<<<<<<<<<<LİSTELEME EKRANI>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # time metodu ile dosyadan readline metodu ile mi sozlukten alma ile mi daha hizli olduguna bak
    # f_time = time.time()
    global ayakkabi_barkod
    if len(ayakkabi_barkod) == 0:
        print("Veri yok!")
    for key, value in ayakkabi_barkod.items():
        print("------------------------------------")
        print('Barkod: %s' % (key))
        for key2, value2 in value.items():
            print('%s: %s' % (key2, value2))
        print("------------------------------------")
    # s_time = time.time()
    # print(s_time - f_time)

def silme():
    print("<<<<<<<<<<<<<<<<<<<<<<<<<SİLME EKRANI>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    if len(ayakkabi_barkod) == 0:
        print("Veri yok!")
        return
    silinecek_barkod = input("Veri silinecek barkodu girin: ")
    kontrol = 0
    for i in ayakkabi_barkod.keys():
        if i == silinecek_barkod:
            kontrol = 1
            k = 0
            print("{}) Barkod: {}".format(k, i))
            for key, value in ayakkabi_barkod[i].items():
                k += 1
                print("{}) {}: {}".format(k, key, value))
            silinecek_veri_sec = int(input("Silinecek veriyi secin(0 hepsini siler): "))
            print("Veri siliniyor...")
            if silinecek_veri_sec == 0:
                ayakkabi_barkod.pop(i)
                print("Veri silindi.")
            else:
                silinecek_veri_sec_2 = 0
                for key3 in ayakkabi_barkod[i].keys():
                    silinecek_veri_sec_2 += 1
                    if silinecek_veri_sec == silinecek_veri_sec_2:
                        ayakkabi_barkod[i].pop(key3)
                        print("Veri silindi.")
                        break
            if silinecek_veri_sec < 0 or silinecek_veri_sec > k:
                print("Eksik ya da hatali tuslama yaptiniz. Ana menuye yonlendiriliyorsunuz...")
            break
    if kontrol == 0:
        print("Bu barkodda bir veri yok!")
    with open("21100011022.txt", "w") as file_obj:
        for key2, value2 in ayakkabi_barkod.items():
            file_obj.write('Barkod: %s\n' % (key2))
            for key2, value2 in value2.items():
                file_obj.write('%s: %s\n' % (key2, value2))

def guncelleme():
    print("<<<<<<<<<<<<<<<<<<<<<GUNCELLEME EKRANI>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    if len(ayakkabi_barkod) == 0:
        print("Veri yok!")
        return
    guncellenecek_barkod = input("Guncellemek istediginiz ayakkabiya ait barkodu girin: ")
    guncelleme_kontrol = 0
    for i in ayakkabi_barkod.keys():
        if i == guncellenecek_barkod:
            guncelleme_kontrol = 1
            k = 0
            for key, value in ayakkabi_barkod[i].items():
                k += 1
                print("{}) {}: {}".format(k, key, value))
            guncelleme_secim = int(input("Guncellemek istediginiz veriyi seciniz: "))
            guncelleme_secim_2 = 0
            for key2 in ayakkabi_barkod[i].keys():
                guncelleme_secim_2 += 1
                if guncelleme_secim == guncelleme_secim_2:
                    while True:
                        veri = input("Yeni ayakkabi verisini({}) girin: ".format(key2))
                        if veri.find(" ") == -1:
                            break
                        else:
                            print("UYARI: degerleri girerken bosluk yerine alttan tire(_) kullanin!")
                    ayakkabi_barkod[i][key2] = veri
                    break
            break
    if guncelleme_kontrol == 0 or k == 0:
        print("Guncellenecek ayakkabiya ait herhangi bir veri bulunamadi!")
    with open("21100011022.txt", "w") as file_obj:
        for key3, value3 in ayakkabi_barkod.items():
            file_obj.write('Barkod: %s\n' % (key3))
            for key4, value4 in value3.items():
                file_obj.write('%s: %s\n' % (key4, value4))

def ara():
    print("<<<<<<<<<<<<<<<<<<<<<<<<<ARAMA EKRANI>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    if len(ayakkabi_barkod) == 0:
        print("Veri yok!")
        return
    def markaya_gore_ara():
        bool = False
        aranan_marka = input("Hangi markaya ait urunleri lietelemek istiyorsunuz('marka' formatinda yazin!): ")
        for key, value in ayakkabi_barkod.items():
            for key2, value2 in ayakkabi_barkod[key].items():
                if aranan_marka == value2:
                    bool = True
                    print("------------------------------------")
                    print("Barkod: {}".format(key))
                    for item1, item2 in ayakkabi_barkod[key].items():
                        print('%s: %s' % (item1, item2))
                    print("------------------------------------")
        if bool == False:
            print("Aradiginiz markaya ait ayakkabi bulunmamaktadir!")
    def barkoda_gore_ara():
        barkoda_gore_ara_kontrol = 0
        aranan_barkod = input("Aradiginiz urune ait barkodu girin: ")
        for key, value in ayakkabi_barkod.items():
            if key == aranan_barkod:
                barkoda_gore_ara_kontrol = 1
                print("------------------------------------")
                print("Barkod: {}".format(key))
                for key2, value2 in value.items():
                    print("{}: {}".format(key2, value2))
                print("------------------------------------")
        if barkoda_gore_ara_kontrol == 0:
            print("aradiginiz barkodda bir ayakkabi bulunmamaktadir!")
    print("1) Markaya gore arama")
    print("2) Barkoda gore arama")
    arama_secim = int(input("Seciminiz: "))
    if arama_secim == 1:
        markaya_gore_ara()
    elif arama_secim == 2:
        barkoda_gore_ara()

def ne_kadar_vergi_verecegim():
    print("<<<<<<<<<<<<<<<<<<<<KDV HESAPLAMA EKRANI>>>>>>>>>>>>>>>>>>>>>>>>")
    if len(ayakkabi_barkod) == 0:
        print("Veri yok!")
        return
    toplam_fiyat = 0.0
    kdv_oran = float(input("KDV oranini girin: "))
    for keys, values in ayakkabi_barkod.items():
        for keys2, values2 in ayakkabi_barkod[keys].items():
            if keys2 == "fiyat":
                toplam_fiyat += int(ayakkabi_barkod[keys][keys2])
    toplam_vergi = toplam_fiyat*kdv_oran
    print("Ayakkabilarinizin toplam fiyati {} TL'dir.".format(toplam_fiyat))
    print("Odeyeceginiz toplam vergi: {} TL'dir.".format(toplam_vergi))
while 0 == 0:
    def menu():
        global fonksiyon_say
        if fonksiyon_say == 0:
            dosyadan_alma()
            fonksiyon_say += 1
        print("+                             MENU                              +")
        print("1) Ekleme")
        print("2) Listeleme")
        print("3) Arama")
        print("4) Guncelleme")
        print("5) Silme")
        print("6) KDV hesaplama")
        print("0) Cikis")
        print("+                                                               +")
        menu_secim = int(input("Seciminiz: "))
        if menu_secim == 1:
            ekleme()
        elif menu_secim == 2:
            listeleme()
        elif menu_secim == 3:
            ara()
        elif menu_secim == 4:
            guncelleme()
        elif menu_secim == 5:
            silme()
        elif menu_secim == 6:
            ne_kadar_vergi_verecegim()
        elif menu_secim == 0:
            exit()
        else:
            print("Eksik ya da hatali tuslama yaptiniz. Tekrar deneyin!")
    menu()
