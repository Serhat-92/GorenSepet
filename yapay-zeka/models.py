# -*- coding: utf-8 -*-
"""
Pydantic modelleri - API istek ve yanıt şemaları
"""

from pydantic import BaseModel


# --- NLP İstekleri ---

class RecipeParseRequest(BaseModel):
    """Kullanıcının doğal dil girdisi."""
    metin: str  # Örn: "Kısır yapacağım"


class Malzeme(BaseModel):
    """Tek bir malzeme."""
    ad: str
    miktar: str
    kategori: str


class RecipeParseResponse(BaseModel):
    """NLP parse sonucu."""
    basarili: bool
    yemek: str | None = None
    malzemeler: list[Malzeme] = []
    mesaj: str = ""


class RecipeListResponse(BaseModel):
    """Tüm tariflerin listesi."""
    tarifler: list[str]


# --- Görsel Doğrulama İstekleri ---

class VerifyProductRequest(BaseModel):
    """Görsel doğrulama isteği (base64 yerine URL kullanılabilir)."""
    beklenen_urun: str  # Listede beklenen ürün adı, Örn: "Süt"
    image_url: str | None = None  # Ürün görseli URL'i (opsiyonel)


class VerifyProductResponse(BaseModel):
    """Görsel doğrulama sonucu."""
    eslesme: bool
    beklenen_urun: str
    tespit_edilen: list[str] = []
    uyari_mesaji: str = ""
    guven_skoru: float = 0.0


# --- Personel Puanlama İstekleri ---

class StaffRatingRequest(BaseModel):
    """Personel puanlama isteği."""
    kullanici_id: str
    personel_id: str
    puan: int  # 1-5 arası
    yorum: str = ""


class StaffRatingResponse(BaseModel):
    """Puanlama sonucu."""
    basarili: bool
    mesaj: str
    puan: int | None = None


class StaffAverageResponse(BaseModel):
    """Personel ortalama puan bilgisi."""
    personel_id: str
    ortalama_puan: float
    degerlendirme_sayisi: int
    inceleme_gerekli: bool
    mesaj: str = ""


class LowRatedStaffResponse(BaseModel):
    """Düşük puanlı personel listesi."""
    personeller: list[StaffAverageResponse]
    toplam: int
