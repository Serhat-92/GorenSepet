# GörenSepet Proje İş Akışı ve Mimari Çarkı

Aşağıdaki şemada GörenSepet (Engelsiz Alışveriş) uygulamasının tüm bileşenlerinin birbiriyle nasıl konuştuğunu ve kullanıcı (Görme Engelli Birey) ile nasıl etkileşime girdiğini görebilirsiniz.

## Genel Mimari ve Kullanıcı Akış Şeması

```mermaid
graph TD
    classDef user fill:#2c3e50,stroke:#34495e,color:#fff,stroke-width:2px,weight:bold;
    classDef mobile fill:#27ae60,stroke:#2ecc71,color:#fff,stroke-width:2px;
    classDef ai fill:#8e44ad,stroke:#9b59b6,color:#fff,stroke-width:2px;
    classDef db fill:#f39c12,stroke:#f1c40f,color:#fff,stroke-width:2px;
    classDef external fill:#d35400,stroke:#e67e22,color:#fff,stroke-width:2px;

    U(("👤 Görme Engelli<br/>Kullanıcı")):::user
    
    subgraph Mobil_Uygulama ["📱 Mobil Uygulama (React Native)"]
        app["GörenSepet Arayüzü"]:::mobile
        cam("Kamera (Görüntü Aktarımı)"):::mobile
        mic("Mikrofon (Ses Aktarımı)"):::mobile
        beacon("Konum / Beacon Servisi"):::mobile
    end
    
    subgraph Yapay_Zeka_Sunucusu ["🧠 Yapay Zeka (FastAPI - Python)"]
        nlp["NLP Servisi<br>(Tarif & Liste Oluşturma)"]:::ai
        vision["Görüntü Doğrulama Servisi"]:::ai
        rating["Personel Değerlendirme Modülü"]:::ai
    end
    
    subgraph Backend_Veritabani ["☁️ Backend (Supabase PostgreSQL)"]
        db_profiles[("Kullanıcı & Personel Verileri")]:::db
        db_products[("Ürün & Fiyat Kataloğu")]:::db
        db_requests[("Aktif Yardım Çağrıları")]:::db
    end
    
    U -->|"1️⃣ Sesli Komut: 'Menemen yapacağım'"| mic
    mic -.->|"Metni Gönder"| nlp
    nlp -.->|"Domates, Biber, Yumurta Listesi"| app
    app -->|"Sesli Geri Bildirim: 'Malzemeler Listeye Eklendi'"| U
    U -->|"2️⃣ Raftan ürün alır ve kameraya gösterir"| cam
    cam -.->|"Görseli İlet (API)"| vision
    vision -.->|"Görsel Analizi (Google Cloud)"| vision
    vision -.->|"Eşleşme Sonucu (Doğru/Yanlış Ürün)"| app
    app -->|"Sesli Geri Bildirim: 'Doğru Ürün' veya 'Dikkat Yanlış Ürün'"| U
    U -->|"3️⃣ Yardım Çağırır"| beacon
    beacon -.->|"Konum & İstek Kaydet"| db_requests
    db_requests -.->|"En Yakın Personele İlet"| db_profiles
    db_profiles -->|"Personel Müşteriyi Bulur"| U
    U -->|"4️⃣ Yardım Sonrası Puan Verir"| app
    app -.->|"Puanlama İsteği"| rating
    rating -.->|"Değerlendirmeyi Kaydet"| db_profiles
```

## Spesifik Akışlar: Yapay Zeka Ürün Doğrulama Süreci
Ürün doğrulama aşamasında yapay zekanın (Google Cloud Vision ve FastAPI arkasında) arka planda nasıl karar verdiği aşağıda detaylandırılmıştır.

```mermaid
sequenceDiagram
    participant User as Kullanıcı (Mobil)
    participant API as AI Sunucusu
    participant Cloud as Google Cloud Vision API
    
    User->>API: 1. Sipariş Listesindeki Ürün (örn: 'Süt') ve<br/>Kameradan Çekilen Fotoğrafı (Base64) gönderir
    API->>Cloud: 2. Fotoğrafı Etiket (Label) analizi için iletir
    Cloud-->>API: 3. Algılanan Etiketleri Döndürür<br/>(örn: ['bottle', 'ayran', 'dairy'])
    
    Note over API: API Türkçe çeviri ve eşleştirme mekanizmasını çalıştırır.
    
    alt Eşleşirse (Süt == milk/süt)
        API-->>User: {"eslesme": true, "guven_skoru": 0.95}
        Note over User: Uygulama: "Ürün doğru, sepete ekleyebilirsiniz." der.
    else Eşleşmezse (Süt != ayran)
        API-->>User: {"eslesme": false, "uyari_mesaji": "Dikkat! Listenizde 'Süt' var,<br/>ancak şu anda 'ayran' ekleniyor."}
        Note over User: Kullanıcı ürünü bırakır veya düzeltir.
    end
```

Bu şemalar, GörenSepet'in dört ana direğini (Mobil Girdi, Supabase Yönetimi, Yapay Zeka Beyni, Sesli Geri Bildirim) özetlemektedir. Mimarinin genişletilmesi veya yeni fonksiyonlar eklenmesi planlanıyorsa, bu çark üzerinden referans alınabilir.
