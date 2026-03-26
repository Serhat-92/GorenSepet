# -*- coding: utf-8 -*-
"""
GörenSepet - Yapay Zeka API
============================
1. Akıllı Alışveriş Asistanı (NLP): Doğal dil → malzeme listesi
2. Görsel Doğrulama (Vision): Ürün fotoğrafı → liste eşleştirme

Çalıştırmak için:
    pip install -r requirements.txt
    uvicorn main:app --reload --port 8000

API Dokümantasyonu:
    http://localhost:8000/docs
"""

import base64
from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from models import (
    RecipeParseRequest,
    RecipeParseResponse,
    Malzeme,
    RecipeListResponse,
    VerifyProductResponse,
    StaffRatingRequest,
    StaffRatingResponse,
    StaffAverageResponse,
    LowRatedStaffResponse,
)
from nlp_engine import parse_user_input
from recipes_db import get_all_recipe_names, get_recipe
from vision_service import (
    verify_product_from_image_bytes,
    verify_product_from_base64,
    verify_product_demo,
)
from staff_rating import (
    personel_puanla,
    personel_ortalama_getir,
    dusuk_puanli_personelleri_getir,
    personel_yorumlarini_getir,
)

app = FastAPI(
    title="GörenSepet AI API",
    description="Engelsiz Alışveriş - Yapay Zeka Servisleri",
    version="1.0.0",
)

# CORS - Mobil uygulamanın API'ye erişebilmesi için
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==============================================================================
# NLP Endpoint'leri
# ==============================================================================


@app.post("/api/parse-recipe", response_model=RecipeParseResponse)
async def parse_recipe(request: RecipeParseRequest):
    """
    Akıllı Alışveriş Asistanı - NLP ile metin analizi.

    Kullanıcının doğal dilde yazdığı metni analiz eder ve
    ilgili yemeğin malzeme listesini döndürür.

    Örnekler:
    - "Kısır yapacağım" → Kısır malzemeleri
    - "Mercimek çorbası pişirmek istiyorum" → Çorba malzemeleri
    - "Menemen için ne lazım" → Menemen malzemeleri
    """
    result = parse_user_input(request.metin)
    return RecipeParseResponse(
        basarili=result["basarili"],
        yemek=result["yemek"],
        malzemeler=[Malzeme(**m) for m in result["malzemeler"]],
        mesaj=result["mesaj"],
    )


@app.get("/api/recipes", response_model=RecipeListResponse)
async def list_recipes():
    """Desteklenen tüm tariflerin listesini döndürür."""
    return RecipeListResponse(tarifler=get_all_recipe_names())


@app.get("/api/recipes/{recipe_name}")
async def get_recipe_detail(recipe_name: str):
    """Belirli bir tarifin detaylarını döndürür."""
    recipe = get_recipe(recipe_name)
    if recipe is None:
        raise HTTPException(status_code=404, detail=f"'{recipe_name}' tarifi bulunamadı.")
    return {
        "yemek": recipe_name,
        "kategori": recipe["kategori"],
        "malzemeler": recipe["malzemeler"],
    }


# ==============================================================================
# Görsel Doğrulama Endpoint'leri
# ==============================================================================


@app.post("/api/verify-product", response_model=VerifyProductResponse)
async def verify_product(
    beklenen_urun: str = Form(...),
    image: UploadFile = File(...),
):
    """
    Görsel Doğrulama - Kamera ile ürün eşleştirme.

    Kişi ürünü sepete koyarken kamera ürünü görür ve yapay zeka
    bu ürünün alışveriş listesindeki ürünle eşleşip eşleşmediğini
    kontrol eder.

    Eşleşmezse sesli uyarı mesajı döndürür:
    "Dikkat! Listenizde Süt var, ancak şu anda Ayran ekleniyor."
    """
    image_bytes = await image.read()
    if not image_bytes:
        raise HTTPException(status_code=400, detail="Görsel dosyası boş.")

    result = verify_product_from_image_bytes(image_bytes, beklenen_urun)
    return VerifyProductResponse(**result)


@app.post("/api/verify-product-base64", response_model=VerifyProductResponse)
async def verify_product_base64(
    beklenen_urun: str,
    image_base64: str,
):
    """
    Görsel Doğrulama (Base64) - Mobil uygulamadan base64 kodlu görsel ile.
    """
    result = verify_product_from_base64(image_base64, beklenen_urun)
    return VerifyProductResponse(**result)


@app.post("/api/verify-product-demo", response_model=VerifyProductResponse)
async def verify_product_demo_endpoint(
    beklenen_urun: str,
    simulated_labels: list[str],
):
    """
    Demo Modu - Google Vision API olmadan test etmek için.

    Simüle edilmiş etiketler göndererek sistemi test edin.

    Örnek:
    - beklenen_urun: "Süt"
    - simulated_labels: ["milk", "bottle", "dairy"]  →  Eşleşme BAŞARILI
    - simulated_labels: ["ayran", "bottle", "dairy"]  →  UYARI: Yanlış ürün!
    """
    result = verify_product_demo(beklenen_urun, simulated_labels)
    return VerifyProductResponse(**result)


# ==============================================================================
# Personel Puanlama Endpoint'leri
# ==============================================================================


@app.post("/api/staff/rate", response_model=StaffRatingResponse)
async def rate_staff(request: StaffRatingRequest):
    """
    Personel Puanlama - Alışveriş sonunda personele puan verme.

    Kullanıcı, alışveriş sırasında yardım eden personele 1-5 arası
    puan verir. Düşük puanlı personel sistem tarafından incelemeye alınır.
    """
    result = personel_puanla(
        kullanici_id=request.kullanici_id,
        personel_id=request.personel_id,
        puan=request.puan,
        yorum=request.yorum,
    )
    return StaffRatingResponse(**result)


@app.get("/api/staff/{personel_id}/rating", response_model=StaffAverageResponse)
async def get_staff_rating(personel_id: str):
    """
    Personel Puan Sorgulama - Bir personelin ortalama puanını gösterir.

    Ortalama puan 3.0'ın altındaysa ve en az 3 değerlendirme varsa,
    personel incelemeye alınır.
    """
    result = personel_ortalama_getir(personel_id)
    return StaffAverageResponse(**result)


@app.get("/api/staff/low-rated", response_model=LowRatedStaffResponse)
async def get_low_rated_staff():
    """
    Düşük Puanlı Personeller - İnceleme gerektiren personelleri listeler.

    Ortalama puanı 3.0'ın altında ve en az 3 değerlendirmesi olan
    personelleri döndürür.
    """
    result = dusuk_puanli_personelleri_getir()
    return LowRatedStaffResponse(
        personeller=[StaffAverageResponse(**r) for r in result],
        toplam=len(result),
    )


@app.get("/api/staff/{personel_id}/reviews")
async def get_staff_reviews(personel_id: str):
    """
    Personel Yorumları - Bir personele yapılan tüm değerlendirmeleri gösterir.
    """
    reviews = personel_yorumlarini_getir(personel_id)
    return {"personel_id": personel_id, "yorumlar": reviews, "toplam": len(reviews)}


# ==============================================================================
# Sağlık Kontrolü
# ==============================================================================


@app.get("/")
async def root():
    """API sağlık kontrolü."""
    return {
        "api": "GörenSepet AI",
        "versiyon": "1.0.0",
        "durum": "aktif",
        "endpointler": {
            "NLP - Tarif Analizi": "POST /api/parse-recipe",
            "Tarif Listesi": "GET /api/recipes",
            "Tarif Detayı": "GET /api/recipes/{isim}",
            "Görsel Doğrulama": "POST /api/verify-product",
            "Görsel Doğrulama (Base64)": "POST /api/verify-product-base64",
            "Görsel Doğrulama (Demo)": "POST /api/verify-product-demo",
            "Personel Puanla": "POST /api/staff/rate",
            "Personel Puan Sorgula": "GET /api/staff/{personel_id}/rating",
            "Düşük Puanlı Personeller": "GET /api/staff/low-rated",
            "Personel Yorumları": "GET /api/staff/{personel_id}/reviews",
        },
    }
