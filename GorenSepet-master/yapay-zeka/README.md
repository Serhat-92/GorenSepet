# GorenSepet - Yapay Zeka Modulu

Engelsiz Alisveris projesi icin yapay zeka servisleri.

## Ozellikler

### 1. Akilli Alisveris Asistani (NLP)
Kullanici dogal dilde ne yapmak istedigini yazar, yapay zeka gerekli malzemeleri otomatik olarak dondurur.

**Ornekler:**
- `"Kisir yapacagim"` -> Bulgur, salca, maydanoz, limon vb.
- `"Mercimek corbasi pisirmek istiyorum"` -> Mercimek, havuc, sogan vb.
- `"Menemen icin ne lazim"` -> Yumurta, domates, biber vb.

20 Turkce yemek tarifi desteklenmektedir.

### 2. AI Gorsel Dogrulama (Computer Vision)
Kisi urunu sepete koyarken kamera urunu gorur. Yapay zeka, bu urunun alisveris listesindeki urunle eslesip eslesmedigini anlik olarak analiz eder.

**Google Cloud Vision API** entegrasyonu ile:
- Etiket tespiti (Label Detection)
- Logo tespiti (Logo Detection)
- Metin tespiti (OCR)

### 3. Otomatik Uyari Sistemi
Eger kisi yanlislikla yanlis urun alirsa, yapay zeka anlik uyari mesaji dondurur:

> "Dikkat! Listenizde 'Sut' var, ancak su anda 'Ayran' ekleniyor."

### 4. Personel Puanlama Sistemi
Alisveris sonunda kullanici personeline puan verir (1-5). Dusuk puanli personel sistem tarafindan incelemeye alinir.

## Kurulum

```bash
pip install -r requirements.txt
```

### Google Vision API (Opsiyonel)
Gorsel dogrulama icin Google Cloud Vision API gereklidir:
1. Google Cloud Console'dan Vision API'yi etkinlestirin
2. Servis hesabi olusturup JSON key dosyasini indirin
3. Ortam degiskenini ayarlayin:
```bash
set GOOGLE_APPLICATION_CREDENTIALS=key.json
```

> Not: Vision API olmadan demo modu ile test yapabilirsiniz.

## Calistirma

```bash
uvicorn main:app --reload --port 8000
```

API Dokumantasyonu: http://localhost:8000/docs

## API Endpoint'leri

### NLP
| Metod | Endpoint | Aciklama |
|-------|----------|----------|
| POST | `/api/parse-recipe` | Metin -> malzeme listesi |
| GET | `/api/recipes` | Tum tarif listesi |
| GET | `/api/recipes/{isim}` | Tarif detayi |

### Gorsel Dogrulama
| Metod | Endpoint | Aciklama |
|-------|----------|----------|
| POST | `/api/verify-product` | Kameradan gorsel dogrulama |
| POST | `/api/verify-product-base64` | Base64 gorsel dogrulama |
| POST | `/api/verify-product-demo` | Demo modu (API key gerekmez) |

### Personel Puanlama
| Metod | Endpoint | Aciklama |
|-------|----------|----------|
| POST | `/api/staff/rate` | Personele puan ver |
| GET | `/api/staff/{id}/rating` | Ortalama puan sorgula |
| GET | `/api/staff/low-rated` | Dusuk puanli personeller |
| GET | `/api/staff/{id}/reviews` | Personel yorumlari |

## Test

```bash
python -X utf8 test_ai.py
```

46 birim test icermektedir.

## Dosya Yapisi

```
GorenSepet-AI/
├── main.py            # FastAPI ana uygulama (tum endpoint'ler)
├── nlp_engine.py      # NLP motoru (dogal dil -> yemek tespiti)
├── recipes_db.py      # 20 Turkce yemek tarifi veritabani
├── vision_service.py  # Google Vision API gorsel dogrulama
├── staff_rating.py    # Personel puanlama sistemi
├── models.py          # Pydantic veri modelleri
├── requirements.txt   # Python bagimliliklari
├── test_ai.py         # Birim testler
├── .gitignore
└── README.md
```

## Teknolojiler

- **Python 3.13**
- **FastAPI** - Web framework
- **Pydantic** - Veri dogrulama
- **Google Cloud Vision API** - Gorsel analiz
- **Uvicorn** - ASGI sunucusu
