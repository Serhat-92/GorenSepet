# PROJE DETAY RAPORU (PDR)
**Takım Adı:** [Takım Adı Buraya]
**Proje Adı:** Engelsiz Alışveriş
**Kategori:** Engelsiz Yaşam Teknolojileri

## 1. Proje Özeti (Abstract)
Bu proje, görme, işitme ve bedensel engelli bireylerin market alışverişlerini bağımsız ve güvenli bir şekilde yapabilmelerini sağlamayı amaçlamaktadır. Geliştirilen mobil uygulama; sesli komut sistemi, yapay zeka destekli ürün doğrulama ve konum bazlı personel çağırma sistemi ile engelsiz bir alışveriş deneyimi sunmaktadır.

## 2. Sorun ve Çözüm

### 2.1. Sorun
Engelli bireyler, marketlerde ürünlerin yerini bulmakta, fiyat etiketlerini okumakta ve personel desteğine ulaşmakta zorluk yaşamaktadır. Mevcut çözümler genellikle bir refakatçiye bağımlılık gerektirmekte, bu da bireyin özgürlüğünü kısıtlamaktadır.

### 2.2. Çözüm
"Engelsiz Alışveriş" mobil uygulaması şu çözümleri sunar:
*   **Görme Engelliler İçin:** TalkBack/VoiceOver uyumlu arayüz ve sesli yönlendirme.
*   **İşitme Engelliler İçin:** Görsel bildirimler ve işaret dili desteği (gelecek planı).
*   **Personel Çağırma Sistemi:** Mağaza içindeki engelli birey, tek tuşla konumunu bildirerek en yakın personelden yardım talep edebilir.

## 3. Yöntem ve Teknik Mimari

Projemiz, ölçeklenebilir bulut mimarisi ve çapraz platform mobil uygulama teknolojileri üzerine inşa edilmiştir.

### 3.1. Backend Mimarisi (Supabase)
Veritabanı, kimlik doğrulama ve gerçek zamanlı veri akışı için **Supabase (PostgreSQL)** kullanılmıştır.

*   **Veritabanı Şeması:**
    *   `profiles`: Kullanıcı ve personel bilgileri (engel durumu, yetki seviyesi).
    *   `products`: Ürünlerin barkod, fiyat ve görsel bilgileri.
    *   `help_requests`: Konum (enlem/boylam) içeren yardım talepleri.
*   **Güvenlik (Row Level Security - RLS):**
    *   Veri güvenliği veritabanı seviyesinde sağlanmıştır.
    *   *Kural:* Kullanıcılar sadece kendi yardım taleplerini görebilir.
    *   *Kural:* Yetkili personeller (`is_staff = true`) tüm aktif çağrıları görebilir.
*   **API & Entegrasyon:** Mobil uygulama ile backend arasındaki güvenli iletişim RESTful API ve WebSocket üzerinden sağlanır.

### 3.2. Mobil Uygulama
*   **Teknoloji:** React Native (Expo)
*   **Uyumluluk:** iOS ve Android
*   **Özellikler:**
    *   Supabase istemcisi ile güvenli oturum açma.
    *   Kamera entegrasyonu (Barkod okuma ve yapay zeka analizi için).
    *   Konum servisleri entegrasyonu.

## 4. Yenilikçi Yönler (İnovasyon)
1.  **Akıllı Eşleşme Algoritması:** Yardım çağrılarını, mağaza içindeki personelin konumuna ve uygunluk durumuna göre otomatik olarak optimize eder.
2.  **Hibrit Güvenlik Modeli:** Hem fiziksel güvenlik (personel yardımı) hem de dijital güvenlik (yanlış ürün alımını engelleyen AI) bir arada sunulmaktadır.

## 5. Proje Takvimi ve Durum

| Aşama | Açıklama | Durum |
| :--- | :--- | :--- |
| **1. Aşama** | Analiz, Veritabanı Tasarımı ve Supabase Kurulumu | ✅ **Tamamlandı** |
| **2. Aşama** | Mobil Uygulama Temel Kurulumu ve Backend Bağlantısı | ✅ **Tamamlandı** |
| **3. Aşama** | Arayüz Kodlaması (UI/UX) ve Navigasyon | ⏳ Devam Ediyor |
| **4. Aşama** | Yapay Zeka (Görüntü İşleme) Entegrasyonu | 📅 Planlandı |
| **5. Aşama** | Saha Testleri ve Teknofest Sunumu | 📅 Planlandı |

## 6. Kaynakça
*   Supabase Documentation (supabase.com/docs)
*   React Native Accessibility Guidelines
*   WCAG (Web Content Accessibility Guidelines) 2.1
