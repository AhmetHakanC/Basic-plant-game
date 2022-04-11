import random
import time

#Koşullar (Bu kısım otomatik)
ihtiyac_sicaklik = []
ihtiyac_su = []
sicaklik_alt = random.randint(-20,100)
while True:
    sicaklik_ust = random.randint(-20,100)
    if(sicaklik_ust < sicaklik_alt):
        continue
    else:
        break

su_ihtiyaci_alt = random.randint(1,200)
while True:
    su_ihtiyaci_ust = random.randint(1,200)
    if(su_ihtiyaci_ust < su_ihtiyaci_alt):
        continue
    else:
        break

ihtiyac_sicaklik.append(sicaklik_alt)
ihtiyac_su.append(su_ihtiyaci_alt)
ihtiyac_sicaklik.append(sicaklik_ust)
ihtiyac_su.append(su_ihtiyaci_ust)
print("Bitki oluşturuldu")


#Güncel Bitki
olum = 0 #otomatik
su = random.randint(ihtiyac_su[0],ihtiyac_su[1])
derece = random.randint(ihtiyac_sicaklik[0],ihtiyac_sicaklik[1])
bitki = () #kullanıcıdan alınıyor
sulama = [] #otomatik
eklenen_su = 0 #otomatik
eklenen_sicaklik = 0 #otomatik
klima = 0 #otomatik

#------------------------------
dur = 0 #otomatik
isimler = ["Mahmut","Selami","Kubilay","KingHakan","Hasan","Zülfikar","Yağmur","Funda"] #otomatik
a = 0.1 #otomatik
for i in range(100):
    sulama.append(a)
    a += 0.1
    a = round(a, 1)


def bitki_guncel():
    print("Güncel hava şartları: ")
    print("     Havadaki nem: ", nemler)
    print("     Ortam sıcaklığındaki değişim: ", havalar,"\n")

    print("Bitkinin(",bitki,")yaşaması için uygun koşullar: ")
    print("     Su koşulları: ",su_ihtiyaci_alt,su_ihtiyaci_ust)
    print("     Sıcaklık Koşulları: ",sicaklik_alt,sicaklik_ust,"\n")

    print("Bitkinin(",bitki,") Güncel Durumu:")
    print("     Bitkinin(",bitki,") su durumu: ",su)
    print("     Sıcaklık: ",derece,"\n")
#------------------------------

"""Bu kısım güncel hava şartlarını barındırıyor"""
havalar = 0
nemler = 0
ort_hava = [-2,-1,1,2]
ort_nem = [-2,-1,1,2]
ort_hava_kont = random.choice(ort_hava)
ort_nem_kont = random.choice(ort_nem)

if(ort_hava_kont == -2):
    havalar = random.choice(sulama[49:100])
    havalar *= -1
elif(ort_hava_kont == -1):
    havalar = random.choice(sulama[0:49])
    havalar *= -1
elif(ort_hava_kont == 1):
    havalar = random.choice(sulama[49:100])
elif(ort_hava_kont == 2):
    havalar = random.choice(sulama[0:49])

#---------------

if(ort_nem_kont == -2):
    nemler = random.choice(sulama[49:100])
    nemler *= -1
elif(ort_nem_kont == -1):
    nemler = random.choice(sulama[0:49])
    nemler *= -1
elif(ort_nem_kont == 1):
    nemler = random.choice(sulama[49:100])
elif(ort_nem_kont == 2):
    nemler = random.choice(sulama[0:49])
"""Üstteki kısım güncel hava şartlarını barındırıyor"""
print("Güncel hava şartları: ")
print("Havadaki nem: ",nemler)
print("Ortam sıcaklığındaki değişim: ",havalar)
time.sleep(1)

while True:
    if(su > su_ihtiyaci_ust or su < su_ihtiyaci_alt):
        olum = 1
    if(derece > sicaklik_ust or derece < sicaklik_alt):
        olum = 1
    if (olum == 1):
        print("Bitki öldü.")
        break
    su += nemler
    derece += havalar
    #-------------------------------------
    while (dur == 0):
        bitki = input("Bitkinize isim verin: ")
        if (bitki != ""):
            print("İsim verildi. İsim: ", bitki)
            dur = 1
            break
        elif (bitki == ""):
            bitki = random.choice(isimler)
            print("Bitkinize rastgele bir isim verildi. İsim: ", bitki)
            dur = 1
            break
    #-------------------------------------
    while True:
        c = input("İşlem yapmak için '1' yazın geçmek için 'Enter'a bas: ")
        if(c == "1"):
            while True:
                derece = round(derece, 2)
                su = round(su, 2)
                print("""
                1. Bitkinin Durumu
                2. Bitkiyi Sula
                3. Sıcaklığı ayarla
                4. Havalandırmayı aç
                """)
                b = int(input("Yapmak istediğiniz işlemi seçiniz: "))
                print("\n")
                if(b == 1):
                    bitki_guncel()
                    break
                elif(b == 2):
                    print("Bitki Sulama işlemi seçildi")
                    while True:
                        b2 = input("Sulama miktarını belirtiniz(çok az, az, çok, çok fazla -- Geri dönmek için: 'q' yazın): ")
                        if(b2 == "q" or b2 == "Q"):
                            break
                        elif(b2 == "çok az" or b2 == "Çok Az" or b2 == "ÇOK AZ" or b2 == "Çok az" or b2 == "çokaz" or b2 == "cok az"):
                            eklenen_su = random.choice(sulama[0:25])
                            su += eklenen_su
                            print("Su eklendi. Eklenen miktar: ",eklenen_su)
                            break
                        elif(b2 == "az" or b2 == "Az" or b2 == "AZ"):
                            eklenen_su = random.choice(sulama[24:50])
                            su += eklenen_su
                            print("Su eklendi. Eklenen miktar: ", eklenen_su)
                            break
                        elif(b2 == "çok" or b2 == "Çok" or b2 == "ÇOK"):
                            eklenen_su = random.choice(sulama[49:75])
                            su += eklenen_su
                            print("Su eklendi. Eklenen miktar: ", eklenen_su)
                            break
                        elif (b2 == "çok fazla" or b2 == "Çok Fazla" or b2 == "ÇOK FAZLA"):
                            eklenen_su = random.choice(sulama[49:100])
                            su += eklenen_su
                            print("Su eklendi. Eklenen miktar: ", eklenen_su)
                            break
                    break
                elif(b == 3):
                    print("Sıcaklık ayarlama işlemi seçildi.")
                    while True:
                        f = input("Hangi yönde bir değişim yapmak istiyorsunuz?(eksi-artı -- çıkmak için 'q' ya basın):")
                        if(f == "eksi" or f == "Eksi"):
                            while True:
                                b3 = input("Ayarlanacak sıcaklık miktarını belirtiniz(çok az, az, çok, çok fazla -- Geri dönmek için: 'q' yazın): ")
                                if (b3 == "q" or b3 == "Q"):
                                    break
                                elif (b3 == "çok az" or b3 == "Çok Az" or b3 == "ÇOK AZ" or b3 == "Çok az"):
                                    eklenen_sicaklik = random.choice(sulama[0:25])
                                    eklenen_sicaklik *= -1
                                    derece += eklenen_sicaklik
                                    print("Ortam sıcaklığı değiştirildi. Değişim: ", eklenen_sicaklik)
                                    break
                                elif (b3 == "az" or b3 == "Az" or b3 == "AZ"):
                                    eklenen_sicaklik = random.choice(sulama[24:50])
                                    eklenen_sicaklik *= -1
                                    derece += eklenen_sicaklik
                                    print("Ortam sıcaklığı değiştirildi. Değişim: ", eklenen_sicaklik)
                                    break
                                elif (b3 == "çok" or b3 == "Çok" or b3 == "ÇOK"):
                                    eklenen_sicaklik = random.choice(sulama[49:75])
                                    eklenen_sicaklik *= -1
                                    derece += eklenen_sicaklik
                                    print("Ortam sıcaklığı değiştirildi. Değişim: ", eklenen_sicaklik)
                                    break
                                elif (b3 == "çok fazla" or b3 == "Çok Fazla" or b3 == "ÇOK FAZLA"):
                                    eklenen_sicaklik = random.choice(sulama[49:100])
                                    eklenen_sicaklik *= -1
                                    derece += eklenen_sicaklik
                                    print("Ortam sıcaklığı değiştirildi. Değişim: ", eklenen_sicaklik)
                                    break
                            break
                        elif(f == "artı" or f == "Artı"):
                            while True:
                                b3 = input("Ayarlanacak sıcaklık miktarını belirtiniz(çok az, az, çok, çok fazla -- Geri dönmek için: 'q' yazın): ")
                                if (b3 == "q" or b3 == "Q"):
                                    break
                                elif (b3 == "çok az" or b3 == "Çok Az" or b3 == "ÇOK AZ" or b3 == "Çok az"):
                                    eklenen_sicaklik = random.choice(sulama[0:25])
                                    derece += eklenen_sicaklik
                                    print("Ortam sıcaklığı değiştirildi. Değişim: ", eklenen_sicaklik)
                                    break
                                elif (b3 == "az" or b3 == "Az" or b3 == "AZ"):
                                    eklenen_sicaklik = random.choice(sulama[24:50])
                                    derece += eklenen_sicaklik
                                    print("Ortam sıcaklığı değiştirildi. Değişim: ", eklenen_sicaklik)
                                    break
                                elif (b3 == "çok" or b3 == "Çok" or b3 == "ÇOK"):
                                    eklenen_sicaklik = random.choice(sulama[49:75])
                                    derece += eklenen_sicaklik
                                    print("Ortam sıcaklığı değiştirildi. Değişim: ", eklenen_sicaklik)
                                    break
                                elif (b3 == "çok fazla" or b3 == "Çok Fazla" or b3 == "ÇOK FAZLA"):
                                    eklenen_sicaklik = random.choice(sulama[49:100])
                                    derece += eklenen_sicaklik
                                    print("Ortam sıcaklığı değiştirildi. Değişim: ", eklenen_sicaklik)
                                    break
                            break
                        elif(f == "q"):
                            break
                    break
                elif(b == 4):
                    print("Havalandırma ayarlama seçildi")
                    while True:
                        b4 = input("Açmak için 'Enter'a basın. Geri dönmek için 'q' ya basın.")
                        if(b4 == "q" or b4 == "Q"):
                            break
                        elif(b4 == ""):
                            klima = random.choice(sulama)
                            su -= klima
                            su = round(su,2)
                            derece -= klima/2
                            derece = round(derece,2)
                            print("Klima açıldı. Hava değişimi: ",klima)
                            print("Suya Etkisi: "
                                  "Eski su değeri: ",su+klima,
                                  "Yeni su değeri: ",su)
                            print("Sıcaklığa etkisi: ",-1*klima/2)
                            time.sleep(3)
                            break
                        break
                    break
                else:
                    print("Lütfen geçerli bir şey girin.")
                    continue
        elif(c == ""):
            print("Süreç devam ediyor.")
            break
        else:
            print("Lütfen geçerli bir şey girin.")