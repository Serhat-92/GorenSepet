# Engelsiz Alışveriş - Mobil Uygulama

Bu klasör, projenin mobil uygulama kodlarını içerir.

## Kurulum (Projeyi İndirenler İçin)

Projeyi bilgisayarınıza indirdikten sonra çalıştırmak için şu adımları izleyin:

1.  **Terminali Açın:** Bu klasörün (`mobil-uygulama`) içinde bir terminal açın.
2.  **Paketleri Yükleyin:** Aşağıdaki komutu yazıp enter'a basın:
    ```bash
    npm install
    ```
3.  **Uygulamayı Başlatın:**
    ```bash
    npx expo start
    ```

## Önemli Notlar
*   **API Anahtarları:** `.env` dosyası projeye dahil edilmiştir, bu sayede Supabase bağlantısı otomatik çalışacaktır.
*   **Veritabanı:** Eğer ürün sayısı 0 görünürse, Supabase panelinden örnek veri ekleyebilirsiniz.

## Dosya Yapısı
*   `App.js`: Ana giriş dosyası.
*   `src/services/supabase.js`: Veritabanı bağlantı ayarları.
*   `assets`: Resim ve ikon dosyaları.
