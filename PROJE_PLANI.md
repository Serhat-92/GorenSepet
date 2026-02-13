# Engelsiz Alışveriş - Teknofest Proje Planı

## 1. Proje Değerlendirmesi
Fikriniz "Engelsiz Yaşam Teknolojileri" kategorisi için oldukça uygun ve sosyal etkisi yüksek bir proje. Teknofest bu tarz sosyal sorumluluk projelerine çok önem veriyor.

**Güçlü Yönleri:**
*   Gerçek bir ihtiyaca çözüm üretiyor.
*   Toplumsal farkındalık yaratıyor.
*   Uygulanabilirliği yüksek.

## 2. Önerilen Özellikler (Neler Eklenebilir?)

### Temel Özellikler (MVP - Minimum Viable Product)
*   **Kolay Yardım Çağrısı:** Kullanıcı mağazaya girdiğinde tek tuşla veya sesli komutla "Yardıma ihtiyacım var" diyebilmeli.
*   **Personel Bildirimi:** Mağaza çalışanlarının kullandığı bir panel veya uygulama olmalı. Yardım çağrısı düştüğünde kime, hangi reiona (reyona) gidileceği bildirilmeli.
*   **Alışveriş Listesi:** Sesli veya yazılı olarak alışveriş listesi oluşturma.
*   **Profil Yönetimi:** Kullanıcının engel durumu ve ihtiyaç duyduğu yardım tipi (görme, bedensel, işitme vb.) belirtilmeli.

### İleri Seviye Özellikler (Teknofest İçin Fark Yaratacaklar)
*   **Eşleşmeli Yardım Sistemi (Uber Modeli):**
    1.  Kullanıcı yardım butonuna basar (veya sesle ister).
    2.  Mağazadaki *tüm* uygun personellere bildirim gider.
    3.  Çağrıyı ilk kabul eden personel, kullanıcıyla "eşleşir".
    4.  **Geri Bildirim:** Eşleşme sağlandığı an engelli bireyin telefonu titrer ve sesli olarak "Personel yola çıktı" onayı verilir. Diğer personellerden bildirim silinir.
*   **Akıllı Konum Bildirimi:** Personel çağrıyı kabul ettiğinde, kullanıcının Bluetooth Beacon konumu personelin ekranında harita üzerinde görünür.

### Yapay Zeka (AI) Entegrasyonu
*   **Akıllı Alışveriş Asistanı (NLP):** Kullanıcı "Kısır yapacağım" dediğinde, yapay zeka gerekli malzemeleri (Bulgur, salça, maydanoz vb.) otomatik olarak alışveriş listesine ekler.

### Güvenlik ve Doğrulama (Trust & Safety) - AI Destekli
Engelli bireyin yanlış veya istenmeyen ürün almasını önlemek için yapay zeka devreye girer:
1.  **AI Görsel Doğrulama (Computer Vision):** Personel ürünü sepete koyarken kamera ürünü görür. Yapay zeka, bu ürünün engelli bireyin alışveriş listesindeki ürünle eşleşip eşleşmediğini anlık olarak analiz eder.
2.  **Otomatik Uyarı Sistemi:** Eğer personel yanlışlıkla "Süt" yerine "Ayran" alırsa, yapay zeka anında sesli olarak **"Dikkat! Listenizde Süt var, ancak şu an Ayran ekleniyor."** uyarısını yapar.
3.  **Personel Puanlama Sistemi:** Alışveriş sonunda kullanıcı personele puan verir. Düşük puanlı personeller sistemden incelenir.

## 3. Yol Haritası (Roadmap)

### 1. Aşama: Analiz ve Tasarım (1-2 Hafta)
*   Hedef Kitlenin İhtiyaçlarının Netleştirilmesi.
*   Ekip İçi Görev Dağılımı (Frontend, Backend, Tasarım, Dokümantasyon).
*   Mockup ve UI/UX Tasarımlarının (Figma/Adobe XD) Hazırlanması. *Engelliler için erişilebilirlik standartlarına (WCAG) uygun renk ve buton tasarımları çok önemli.*

### 2. Aşama: Geliştirme (4-6 Hafta)
*   **Teknoloji Seçimi:**
    *   **Mobil:** React Native (JavaScript/TypeScript ile hem iOS hem Android, geniş topluluk desteği).
    *   **Backend:** Supabase (Açık kaynaklı Firebase alternatifi. Çok daha hızlı (PostgreSQL tabanlı) ve Row Level Security (RLS) ile banka seviyesinde güvenlik sağlar).
*   **Prototip:** Temel fonksiyonların (Giriş, Yardım İste, Bildirim Al) kodlanması.

### 3. Aşama: Test ve İyileştirme (2 Hafta)
*   Uygulamanın farklı engel grupları tarafından test edilmesi (Simülasyon yapılabilir).
*   Geri bildirimlere göre arayüz iyileştirmeleri.

### 4. Aşama: Teknofest Hazırlığı
*   Proje Detay Raporu (PDR) yazımı.
*   Tanıtım videosu çekimi.
*   Sunum hazırlığı.

## 4. Ekip Görev Dağılımı (5 Kişilik Kadro)

Herkesin bir ana görevi, bir de yan görevi olmalı. Böylece kimse boş kalmaz.

### 1. Takım Kaptanı & Backend (Supabase) Sorumlusu
*   **Ana Görev:** Proje takvimi, Raporlama (PDR), Sunum Hazırlığı.
*   **Teknik Görev:** Supabase Kurulumu, Veritabanı (PostgreSQL) Tasarımı, Güvenlik Kuralları (RLS).
    *   **Veritabanı Şeması:** `profiles` (Kullanıcılar), `products` (Ürünler), `help_requests` (Yardım Çağrıları).
    *   **Güvenlik:** RLS (Row Level Security) ile kullanıcı verilerinin izolasyonu.
*   **Yan Görev:** Diğer üyelere kod desteği.

### 2. Mobil Geliştirici Lideri (React Native - UI/UX)
*   **Ana Görev:** Uygulamanın genel iskeletini kurmak (Navigation), ekran tasarımlarını (Login, Home) kodlamak.
*   **Yan Görev:** Uygulamanın renk paleti ve kullanıcı deneyimi (Erişilebilirlik) standartlarını belirlemek.

### 3. Mobil Geliştirici (Fonksiyonel & Mantık)
*   **Ana Görev:** Sesli Komut (Voice-to-Text) ve Metin Okuma (Text-to-Speech) entegrasyonu.
*   **Yan Görev:** Bluetooth Beacon entegrasyonu (Personel çağırma mantığı).

### 4. Yapay Zeka (AI) & Algoritma Sorumlusu
*   **Ana Görev:** "Akıllı Alışveriş Listesi" (NLP) algoritmasını yazmak. (Python veya JS ile basit bir API).
*   **Teknik Görev:** Güvenlik için görsel doğrulama (Google Vision API veya benzeri) mantığını araştırıp entegre etmek.

### 5. Test, Dokümantasyon & Medya Sorumlusu
*   **Ana Görev:** Uygulamayı sürekli test edip hataları (bug) bulmak ve GitHub'a girmek.
*   **Yan Görev:** Teknofest tanıtım videosunu çekmek, proje raporlarını yazmak, sunum görsellerini hazırlamak.

## 5. Başlangıç İçin Tavsiyeler
*   GitHub üzerinde bir organizasyon kurun.
*   Hemen bir "Hello World" projesi oluşturup herkesin ortam kurulumlarını tamamlayın.
*   Tasarım yapmadan kodlamaya başlamayın.
