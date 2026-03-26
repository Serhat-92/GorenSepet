# PROJE DETAY RAPORU (PDR) TASLAĞI
**Takım Adı:** [Takım Adı Buraya]
**Proje Adı:** GörenSepet
**Kategori:** Engelsiz Yaşam Teknolojileri

## 1. Proje Özeti (Abstract)
Bu proje, görme, işitme ve bedensel engelli bireylerin market alışverişlerini bağımsız ve güvenli bir şekilde yapabilmelerini sağlamayı amaçlamaktadır. Mobil uygulama üzerinden sesli komut sistemi, yapay zeka destekli ürün doğrulama ve personel çağırma sistemi ile engelsiz bir alışveriş deneyimi sunulmaktadır.

## 2. Sorun ve Çözüm
### Sorun
Engelli bireyler, marketlerde ürünlerin yerini bulmakta, fiyat etiketlerini okumakta ve personel desteğine ulaşmakta zorluk yaşamaktadır. Mevcut çözümler (refakatçi ile alışveriş) bireyin bağımsızlığını kısıtlamaktadır.

### Çözüm
Geliştirdiğimiz "Engelsiz Alışveriş" mobil uygulaması:
*   **Görme Engelliler İçin:** Sesli ürün arama ve navigasyon.
*   **İşitme Engelliler İçin:** İşaret dili desteği (planlanan) ve görsel bildirimler.
*   **Tüm Kullanıcılar İçin:** Tek tuşla konum bazlı personel yardımı (Uber benzeri sistem).

## 3. Yöntem ve Teknik Mimari
Projemiz modern bulut teknolojileri ve yapay zeka servislerini kullanmaktadır.

### 3.1. Backend Mimarisi (Supabase)
Veritabanı ve kimlik doğrulama işlemleri için açık kaynaklı **Supabase (PostgreSQL)** kullanılmıştır.
*   **Veritabanı:** İlişkisel veritabanı yapısı ile kullanıcılar, ürünler ve yardım talepleri yönetilmektedir.
*   **Güvenlik:** Row Level Security (RLS) kuralları ile her kullanıcının verisi izole edilmiştir.
*   **Realtime:** Personel ile kullanıcı arasındaki etkileşim (Yardım kabulü, konum takibi) WebSocket üzerinden anlık olarak sağlanır.

### 3.2. Mobil Uygulama
*   **Framework:** React Native ile çapraz platform (iOS & Android) geliştirme.
*   **Erişilebilirlik:** Ekran okuyucu (TalkBack/VoiceOver) uyumlu arayüz tasarımı.

## 4. Yenilikçi Yönler (İnovasyon)
*   **Akıllı Eşleşme:** Yardım çağrılarının en yakın personele otomatik atanması.
*   **Yapay Zeka Doğrulama:** (Geliştirme Aşamasında) Sepete eklenen ürünün doğruluğunun kamera ile kontrol edilmesi.

## 5. Proje Takvimi
1.  **Hafta 1-2:** Analiz, Tasarım ve Veritabanı Kurulumu (Tamamlandı).
2.  **Hafta 3-4:** Mobil Uygulama Arayüz Kodlaması.
3.  **Hafta 5-6:** Backend Entegrasyonu ve Testler.

## 6. Kaynakça
*   Supabase Documentation
*   React Native Accessibility Guidelines
*   WCAG (Web Content Accessibility Guidelines) 2.1
