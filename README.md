# Bankacılık- Console Uygulaması

Bu proje basit bir banka console uygulamasıdır. Öğrencilerin öğrendiği
Python konularını (değişken, döngü, koşul, liste, sözlük, fonksiyon,
class, modüler yapı, pandas, matplotlib) tek bir örnekte pekiştirmek
için hazırlanmıştır.

## Dosyalar

| Dosya         | Görevi                                                        |
|---------------|----------------------------------------------------------------|
| `models.py`   | Tek bir hesabı temsil eden `Account` sınıfı                    |
| `bank.py`     | Tüm hesapları yöneten `Bank` sınıfı                             |
| `reports.py`  | pandas ile özet tablo, matplotlib ile grafik oluşturma          |
| `main.py`     | Programı başlatan ve menüyü çalıştıran ana dosya                |

## Nasıl Çalıştırılır?

1. Gerekli kütüphaneleri kurun (yoksa):
   ```
   pip install pandas matplotlib
   ```

2. Tüm dosyaları aynı klasöre koyun.

3. Terminalden çalıştırın:
   ```
   python main.py
   ```

4. Açılan menüden numara girerek işlem seçin (1-9).

## Menü Seçenekleri

1. Hesap Oluştur
2. Para Yatır
3. Para Çek
4. Para Transfer Et
5. Tüm Hesapları Listele
6. Hesap İşlem Özeti (pandas ile tablo)
7. Hesap Bakiye Grafiği (matplotlib ile çizgi grafik)
8. Tüm Hesapların Bakiye Grafiği (matplotlib ile bar grafik)
9. Çıkış
