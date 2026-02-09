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
Veriler Row Level Security (RLS) ile korunmaktadır. Okuma ve yazma kuralları SQL editöründen tanımlanır.
