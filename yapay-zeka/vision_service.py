# -*- coding: utf-8 -*-
"""
Görsel Doğrulama Servisi - Google Cloud Vision API Entegrasyonu

Bu modül, alışveriş sırasında kişinin sepete koyduğu ürünün
alışveriş listesindeki ürünle eşleşip eşleşmediğini kontrol eder.

Kurulum:
  1. Google Cloud Console'dan Vision API'yi etkinleştirin
  2. Servis hesabı oluşturup JSON key dosyasını indirin
  3. GOOGLE_APPLICATION_CREDENTIALS ortam değişkenini ayarlayın:
     export GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"
"""

import os
import io
import base64

# Google Vision API kullanılabilirliğini kontrol et
try:
    from google.cloud import vision
    VISION_API_AVAILABLE = True
except ImportError:
    VISION_API_AVAILABLE = False


# Türkçe ürün eşleştirme sözlüğü
# Vision API'den dönen İngilizce etiketleri Türkçe ürün isimleriyle eşleştirir
PRODUCT_LABEL_MAP = {
    # Süt ürünleri
    "milk": ["süt"],
    "yogurt": ["yoğurt"],
    "cheese": ["peynir", "beyaz peynir", "kaşar peyniri"],
    "butter": ["tereyağı"],
    "cream": ["krema"],
    "egg": ["yumurta"],
    "eggs": ["yumurta"],
    # İçecekler
    "ayran": ["ayran"],
    "juice": ["meyve suyu"],
    "water": ["su"],
    "beverage": ["içecek"],
    # Sebzeler
    "tomato": ["domates"],
    "onion": ["soğan"],
    "potato": ["patates"],
    "pepper": ["biber", "sivri biber"],
    "carrot": ["havuç"],
    "eggplant": ["patlıcan"],
    "zucchini": ["kabak"],
    "parsley": ["maydanoz"],
    "garlic": ["sarımsak"],
    "lettuce": ["marul"],
    "cucumber": ["salatalık"],
    "lemon": ["limon"],
    # Meyveler
    "apple": ["elma"],
    "banana": ["muz"],
    "orange": ["portakal"],
    "grape": ["üzüm"],
    "watermelon": ["karpuz"],
    "strawberry": ["çilek"],
    # Et ve protein
    "meat": ["et", "kıyma", "kuşbaşı et"],
    "chicken": ["tavuk"],
    "fish": ["balık"],
    "ground meat": ["kıyma"],
    # Bakkaliye
    "bread": ["ekmek"],
    "rice": ["pirinç"],
    "pasta": ["makarna"],
    "flour": ["un"],
    "sugar": ["şeker"],
    "oil": ["sıvı yağ", "zeytinyağı"],
    "olive oil": ["zeytinyağı"],
    "salt": ["tuz"],
    "chocolate": ["çikolata"],
    # Konserve ve sos
    "tomato paste": ["salça", "domates salçası"],
    "canned food": ["konserve"],
}


def _normalize_product_name(name: str) -> str:
    """Ürün adını karşılaştırma için normalize eder."""
    tr_map = str.maketrans("IİÖÜÇŞĞ", "ıiöüçşğ")
    return name.translate(tr_map).lower().strip()


def _find_matching_turkish_products(labels: list[str]) -> list[str]:
    """Vision API etiketlerini Türkçe ürün isimlerine çevirir."""
    turkish_products = []
    for label in labels:
        label_lower = label.lower().strip()
        if label_lower in PRODUCT_LABEL_MAP:
            turkish_products.extend(PRODUCT_LABEL_MAP[label_lower])
        else:
            # Kısmi eşleşme dene
            for key, values in PRODUCT_LABEL_MAP.items():
                if key in label_lower or label_lower in key:
                    turkish_products.extend(values)
                    break
    return list(set(turkish_products))


def _check_product_match(expected: str, detected_labels: list[str]) -> dict:
    """
    Beklenen ürünün tespit edilen etiketlerle eşleşip eşleşmediğini kontrol eder.

    Returns:
        dict: Eşleşme sonucu
    """
    expected_normalized = _normalize_product_name(expected)
    turkish_products = _find_matching_turkish_products(detected_labels)

    # Doğrudan eşleşme kontrolü
    for product in turkish_products:
        if _normalize_product_name(product) == expected_normalized:
            return {
                "eslesme": True,
                "beklenen_urun": expected,
                "tespit_edilen": turkish_products,
                "uyari_mesaji": "",
                "guven_skoru": 0.95,
            }
        # Kısmi eşleşme (ürün adı içinde geçiyorsa)
        if (expected_normalized in _normalize_product_name(product)
                or _normalize_product_name(product) in expected_normalized):
            return {
                "eslesme": True,
                "beklenen_urun": expected,
                "tespit_edilen": turkish_products,
                "uyari_mesaji": "",
                "guven_skoru": 0.80,
            }

    # Eşleşme yok - uyarı oluştur
    detected_str = ", ".join(turkish_products) if turkish_products else "bilinmeyen ürün"
    return {
        "eslesme": False,
        "beklenen_urun": expected,
        "tespit_edilen": turkish_products,
        "uyari_mesaji": (
            f"Dikkat! Listenizde '{expected}' var, "
            f"ancak şu anda '{detected_str}' ekleniyor."
        ),
        "guven_skoru": 0.0,
    }


def verify_product_from_image_bytes(image_bytes: bytes, expected_product: str) -> dict:
    """
    Ürün görselini (bytes) analiz eder ve beklenen ürünle karşılaştırır.

    Args:
        image_bytes: Ürün fotoğrafının byte verisi
        expected_product: Alışveriş listesindeki beklenen ürün adı

    Returns:
        dict: Doğrulama sonucu
    """
    if not VISION_API_AVAILABLE:
        return {
            "eslesme": False,
            "beklenen_urun": expected_product,
            "tespit_edilen": [],
            "uyari_mesaji": (
                "Google Cloud Vision API yüklü değil. "
                "Kurulum: pip install google-cloud-vision"
            ),
            "guven_skoru": 0.0,
        }

    try:
        client = vision.ImageAnnotatorClient()
        image = vision.Image(content=image_bytes)

        # Etiket tespiti
        label_response = client.label_detection(image=image)
        labels = [label.description for label in label_response.label_annotations]

        # Logo tespiti (marka bilgisi için)
        logo_response = client.logo_detection(image=image)
        logos = [logo.description for logo in logo_response.logo_annotations]

        # Metin tespiti (ürün üzerindeki yazılar)
        text_response = client.text_detection(image=image)
        texts = []
        if text_response.text_annotations:
            texts = [text_response.text_annotations[0].description]

        all_labels = labels + logos
        return _check_product_match(expected_product, all_labels)

    except Exception as e:
        return {
            "eslesme": False,
            "beklenen_urun": expected_product,
            "tespit_edilen": [],
            "uyari_mesaji": f"Görsel analiz sırasında hata oluştu: {str(e)}",
            "guven_skoru": 0.0,
        }


def verify_product_from_base64(image_base64: str, expected_product: str) -> dict:
    """
    Base64 kodlu görseli analiz eder.

    Args:
        image_base64: Base64 kodlu ürün görseli
        expected_product: Alışveriş listesindeki beklenen ürün adı

    Returns:
        dict: Doğrulama sonucu
    """
    try:
        image_bytes = base64.b64decode(image_base64)
        return verify_product_from_image_bytes(image_bytes, expected_product)
    except Exception as e:
        return {
            "eslesme": False,
            "beklenen_urun": expected_product,
            "tespit_edilen": [],
            "uyari_mesaji": f"Base64 çözümleme hatası: {str(e)}",
            "guven_skoru": 0.0,
        }


def verify_product_demo(expected_product: str, simulated_labels: list[str]) -> dict:
    """
    Demo/test modu: Gerçek görsel olmadan simüle edilmiş etiketlerle test eder.
    Google Vision API kurulmadan test yapabilmek için kullanılır.

    Args:
        expected_product: Beklenen ürün adı
        simulated_labels: Simüle edilmiş etiketler (İngilizce)

    Returns:
        dict: Doğrulama sonucu
    """
    return _check_product_match(expected_product, simulated_labels)
