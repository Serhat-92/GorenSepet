# Engelsiz Alışveriş - Backend (Supabase)

Bu proje backend servisi olarak **Supabase** kullanmaktadır. Supabase, Firebase'in açık kaynaklı alternatifidir ve **PostgreSQL** veritabanı üzerine kuruludur.

## Kurulum
1.  [Supabase.com](https://supabase.com) adresinde yeni bir proje oluşturun.
2.  Proje Dashboard'undan `Settings > API` bölümüne gidin.
3.  `Project URL` ve `anon public key` değerlerini alın.
4.  Bu değerleri `mobil-uygulama/.env` dosyasına ekleyin.

## Veritabanı Yapısı
*   **users:** Kullanıcı profilleri (id, ad, soyad, engel_durumu).
*   **help_requests:** Yardım talepleri (konum, durum, atanmış_personel_id).
*   **products:** Ürün veritabanı (barkod, isim, fiyat).

## Güvenlik (RLS)
Veriler Row Level Security (RLS) ile korunmaktadır. Okuma ve yazma kuralları `schema.sql` dosyasında tanımlanmıştır.

## Veritabanı Kurulumu (SQL Çalıştırma)
Veritabanı tablolarını ve güvenlik kurallarını tek seferde oluşturmak için:
1.  Bu klasördeki `schema.sql` dosyasının içeriğini kopyalayın.
2.  Supabase Dashboard'a gidin.
3.  Sol menüden **SQL Editor**'ü seçin.
4.  Kodu yapıştırın ve **RUN** butonuna basın.
5.  *Success* mesajını gördüğünüzde kurulum tamamlanmıştır.

### Tablo Detayları
*   **profiles:** Kullanıcıların engel durumu ve personel yetkisi (`is_staff`) burada tutulur.
*   **products:** Barkod okuma sistemi için ürün veritabanı.
*   **help_requests:** Konum bazlı yardım çağrıları. RLS sayesinde herkes sadece kendi çağrısını görür, personeller hepsini görür.
