# Bankamatik Uygulaması

MustafaHesap = {
    'ad': 'Mustafa GÖK',
    'hesapNo': '13245678',
    'bakiye': 5000,
    'ekHesap': 1500
}

YasinHesap = {
    'ad': 'Yasin Gök',
    'hesapNo': '12368678',
    'bakiye': 10000,
    'ekHesap': 3000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar 
        print('Lütfen Paranızı Almayi Unutmayin.')
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('Ek hesaptan para cekmek ister misiniz?(yes/no)')

            if ekHesapKullanimi == 'yes':
                ekhesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapKullanilacakMiktar
                print('Lütfen Paranızı Almayi Unutmayin.')
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} No lu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('Üzgünüz bakiyeniz yetersiz')
            bakiyeSorgula(hesap)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")

paraCek(MustafaHesap, 3000)

print('*****************')

paraCek(MustafaHesap, 3000)

