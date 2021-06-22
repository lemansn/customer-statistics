MIN_PUAN=1
MAX_PUAN=5

iadeli = 0          #en az 1 tane iade eden kullanici sayi
kullanici_say=0     #toplam kullanicilarin sayi
iade_say=0          #iade olunan urun sayisi
ikiden_az=0         #puan ortalamasi ikiden az olan kullanici sayi
MAX=max_satin=max_ad=max_iade=max_puan=0 #max satin alan kullanici icin istenen degerler
say_bes_vermeyen = 0 #hic bir urune 5 puan vermeyen kullanici sayi

kullanici_no = int(input('Kullanıcı numarasını girin(0 ya da 0’dan küçük bir değer girerseniz program biter): '))

while kullanici_no > 0:
    siparis_say = int(input('Sipariş verdiğiniz ürün sayısını giriniz: '))
    while siparis_say <= 0:
        siparis_say = int(input('Sipariş verdiğiniz ürün sayısını giriniz: '))

    iade = int(input('İade ettiğiniz ürün sayısını giriniz: '))
    while iade > siparis_say or iade<0:
        iade = int(input('İade ettiğiniz ürün sayısını giriniz: '))
    if iade > 0:
        iadeli += 1
    iade_say += iade

    satin_aldi = siparis_say - iade  #satin alinan urunlerin sayi
    puan_top=0               #urunlere verilen toplam puan
    dort_ve_bes = 0          #4 veya 5 puan verilen urun sayi
    bes_vermeyen = True
    for satin_aldi in range(1, satin_aldi + 1):
        print('Satın aldığınız', satin_aldi, '. ürün için verdiğiniz puan', end='')
        puan = int(input(':'))

        while not puan in range(MIN_PUAN, MAX_PUAN+1):
            print('Satın aldığınız', satin_aldi, '. ürün için verdiğiniz puan', end='')
            puan = int(input(':'))
        puan_top += puan

        if puan == 4 or puan == 5:
            dort_ve_bes += 1

        if puan == 5:
            bes_vermeyen = False

    if bes_vermeyen:
        say_bes_vermeyen += 1

    #puan ortalamasinin 2'den dusuk olan kullanici sayinin bulunmasi
    ortalama = puan_top/satin_aldi
    if ortalama<2:
        ikiden_az+=1

    #en çok ürün satın alan kullanıcıyla iligili degerlerin bulunmasi
    if satin_aldi>MAX:
        MAX=satin_aldi
        max_ad = kullanici_no
        max_satin=satin_aldi
        max_iade = iade
        max_puan = puan_top

    kullanici_say+=1

    print(f"Kullanıcının siparis verdiyini alma oranı: %{format(((satin_aldi / siparis_say) * 100),'.2f')}")
    print(f"Kullanıcının satın aldığı ürünlere verdiği puanların ortalaması: {format(ortalama,'.2f')}")
    print(f"Kullanıcının 4 veya 5 puan verdiği ürünlerin satın aldığı ürünler içindeki oranı: %{format(((dort_ve_bes/satin_aldi)*100),'.2f')}")
    print('-----------------------')

    kullanici_no = int(input('Kullanıcı numarasını girin(0 ya da 0’dan küçük bir değer girerseniz program biter): '))

print(f"Kullanıcı başına iade edilen ortalama ürün sayısı: {format((iade_say/kullanici_say),'.2f')}")

print('Sipariş verdiği ürünlerin en az 1 tanesini iade eden kullanıcı sayısı:',iadeli,
      f"ve tüm kullanıcılar içindeki oranı: %{format(((iadeli/kullanici_say)*100),'.2f')}")

print('Satın aldığı hiçbir ürüne 5 puan vermeyen kullanıcı sayısı:',say_bes_vermeyen,
      f"ve tüm kullanıcılar içindeki oranı: %{format(((say_bes_vermeyen/kullanici_say)*100),'.2f')}")

print('Satın aldığı ürünlere verdiği puanların ortalaması 2’den düşük olan kullanıcı sayısı:',ikiden_az,
      f"ve tüm kullanıcılar içindeki oranı: %{format(((ikiden_az/kullanici_say)*100),'.2f')}")

print('En çok ürün satın alan kullanıcının numarası:',f'{max_ad},','satın aldığı ürün sayısı:',f'{max_satin},',
      'iade ettiği ürün sayısı:',max_iade,f"ve satın aldığı ürünlere verdiği puanların ortalaması: {format((max_puan/max_satin),'.2f')}")







