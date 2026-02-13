# Engelsiz Alışveriş (Teknofest Projesi)

Görme engelli bireylerin market alışverişlerini kimseye ihtiyaç duymadan veya kolayca yardım alarak yapabilmelerini sağlayan mobil uygulama projesi.

## Özellikler
*   **Sesli Asistan:** Tam sesli kontrol ile ürün arama ve yardım isteme.
*   **Eşleşmeli Yardım:** Mağaza personeli ile görme engelli bireyi Bluetooth Beacon teknolojisi ile eşleştirme.
*   **Akıllı Liste:** Yapay zeka destekli alışveriş listesi oluşturma.
*   **Güvenli Alışveriş:** AI destekli görsel doğrulama ile yanlış ürün alımının önüne geçme.

## Teknolojiler
*   **Mobil:** React Native (Expo)
*   **Backend:** Supabase (PostgreSQL)
*   **Yapay Zeka:** Python / Google Cloud Vision API


## Kurulum
Her klasörün kendi içinde detaylı (`README.md`) kurulum rehberi vardır.

### Mobil Uygulama
1.  `mobil-uygulama` klasörüne gidin.
2.  `npm install` komutunu çalıştırın.
3.  `npx expo start` ile başlatın.

### Backend (Supabase)
Veritabanı kurulumu ve `schema.sql` dosyası `backend` klasöründedir.
Supabase bağlantı bilgileri (URL ve Key) `mobil-uygulama/.env` dosyasında tanımlıdır.
