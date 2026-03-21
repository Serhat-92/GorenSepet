# -*- coding: utf-8 -*-
"""
Yapay Zeka Modülleri Test Dosyası
NLP motoru ve Görsel Doğrulama servisini test eder.

Çalıştırmak için:
    cd backend/ai
    python test_ai.py
"""

import sys

# ==================== NLP MOTOR TESTLERİ ====================

from nlp_engine import parse_user_input, normalize_turkish, extract_recipe_name
from vision_service import verify_product_demo

passed = 0
failed = 0


def test(name: str, condition: bool):
    global passed, failed
    if condition:
        passed += 1
        print(f"  [OK] {name}")
    else:
        failed += 1
        print(f"  [FAIL] {name}")


print("=" * 60)
print("NLP MOTOR TESTLERİ")
print("=" * 60)

# --- normalize_turkish testleri ---
print("\n--- normalize_turkish ---")
test("Büyük harf dönüşümü", normalize_turkish("KISIR") == "kısır")
test("Boşluk temizleme", normalize_turkish("  kısır  ") == "kısır")
test("Karışık harf", normalize_turkish("Mercimek Çorbası") == "mercimek çorbası")

# --- parse_user_input testleri ---
print("\n--- parse_user_input: Temel Kalıplar ---")

# "X yapacağım" kalıbı
result = parse_user_input("Kısır yapacağım")
test("'Kısır yapacağım' -> kısır bulunmalı", result["basarili"] and result["yemek"] == "kısır")

result = parse_user_input("Menemen yapacağım")
test("'Menemen yapacağım' -> menemen bulunmalı", result["basarili"] and result["yemek"] == "menemen")

# "X pişirmek istiyorum" kalıbı
result = parse_user_input("Mercimek çorbası pişirmek istiyorum")
test("'Mercimek çorbası pişirmek istiyorum'", result["basarili"] and result["yemek"] == "mercimek çorbası")

# "X için ne lazım" kalıbı
result = parse_user_input("Karnıyarık için ne lazım")
test("'Karnıyarık için ne lazım'", result["basarili"] and result["yemek"] == "karnıyarık")

# "X hazırlayacağım" kalıbı
result = parse_user_input("Çiğ köfte hazırlayacağım")
test("'Çiğ köfte hazırlayacağım'", result["basarili"] and result["yemek"] == "çiğ köfte")

# "X tarifi" kalıbı
result = parse_user_input("Yaprak sarma tarifi")
test("'Yaprak sarma tarifi'", result["basarili"] and result["yemek"] == "yaprak sarma")

# "X malzemeleri ne" kalıbı
result = parse_user_input("Ezogelin çorbası malzemeleri ne")
test("'Ezogelin çorbası malzemeleri ne'", result["basarili"] and result["yemek"] == "ezogelin çorbası")

# Doğrudan yemek adı
result = parse_user_input("kısır")
test("Doğrudan 'kısır'", result["basarili"] and result["yemek"] == "kısır")

print("\n--- parse_user_input: Malzeme Kontrolü ---")

result = parse_user_input("Kısır yapacağım")
malzeme_adlari = [m["ad"] for m in result["malzemeler"]]
test("Kısır: Bulgur içermeli", "İnce Bulgur" in malzeme_adlari)
test("Kısır: Salça içermeli", "Salça (Domates)" in malzeme_adlari)
test("Kısır: Maydanoz içermeli", "Maydanoz" in malzeme_adlari)
test("Kısır: Malzeme sayısı > 5", len(result["malzemeler"]) > 5)

result = parse_user_input("Menemen yapacağım")
malzeme_adlari = [m["ad"] for m in result["malzemeler"]]
test("Menemen: Yumurta içermeli", "Yumurta" in malzeme_adlari)
test("Menemen: Domates içermeli", "Domates" in malzeme_adlari)

print("\n--- parse_user_input: Hata Durumları ---")

result = parse_user_input("")
test("Boş metin -> basarili=False", not result["basarili"])

result = parse_user_input("Hava nasıl?")
test("Alakasız metin -> basarili=False", not result["basarili"])

result = parse_user_input("xyz abc 123")
test("Anlamsız metin -> basarili=False", not result["basarili"])

print("\n--- parse_user_input: Fuzzy Eşleşme ---")

result = parse_user_input("kisir yapacağım")  # ı -> i
test("Aksansız 'kisir' -> kısır", result["basarili"] and result["yemek"] == "kısır")

result = parse_user_input("cig kofte yapacağım")
test("Aksansız 'cig kofte' -> çiğ köfte", result["basarili"] and result["yemek"] == "çiğ köfte")


# ==================== GÖRSEL DOĞRULAMA TESTLERİ ====================

print("\n" + "=" * 60)
print("GÖRSEL DOĞRULAMA TESTLERİ")
print("=" * 60)

print("\n--- verify_product_demo ---")

# Doğru ürün: Süt bekleniyor, milk tespit edildi
result = verify_product_demo("Süt", ["milk", "bottle", "dairy product"])
test("Sut vs milk -> eslesme", result["eslesme"] is True)
test("Sut: guven skoru > 0.5", result["guven_skoru"] > 0.5)

# Yanlış ürün: Süt bekleniyor, ayran tespit edildi
result = verify_product_demo("Süt", ["ayran", "bottle", "dairy product"])
test("Sut vs ayran -> eslesme YOK", result["eslesme"] is False)
test("Uyarı mesajı içeriyor", "Dikkat" in result["uyari_mesaji"])
test("Uyarı 'Süt' içeriyor", "Süt" in result["uyari_mesaji"])

# Doğru ürün: Domates bekleniyor, tomato tespit edildi
result = verify_product_demo("Domates", ["tomato", "vegetable", "red"])
test("Domates vs tomato -> eslesme", result["eslesme"] is True)

# Yanlış ürün: Yumurta bekleniyor, cheese tespit edildi
result = verify_product_demo("Yumurta", ["cheese", "dairy", "white"])
test("Yumurta vs cheese -> eslesme YOK", result["eslesme"] is False)
test("Uyarı mesajı var", len(result["uyari_mesaji"]) > 0)

# Bilinmeyen etiketler
result = verify_product_demo("Süt", ["unknown_object", "thing"])
test("Bilinmeyen etiket -> eslesme YOK", result["eslesme"] is False)


# ==================== PERSONEL PUANLAMA TESTLERİ ====================

from staff_rating import (
    personel_puanla,
    personel_ortalama_getir,
    dusuk_puanli_personelleri_getir,
    personel_yorumlarini_getir,
    _ratings,
)

print("\n" + "=" * 60)
print("PERSONEL PUANLAMA TESTLERİ")
print("=" * 60)

# Onceki test verilerini temizle
_ratings.clear()

print("\n--- personel_puanla ---")

result = personel_puanla("user1", "staff1", 5, "Harika yardim")
test("Basarili puanlama", result["basarili"])
test("Puan 5 donmeli", result["puan"] == 5)

result = personel_puanla("user1", "staff1", 0)
test("Gecersiz puan (0) -> basarisiz", not result["basarili"])

result = personel_puanla("user1", "staff1", 6)
test("Gecersiz puan (6) -> basarisiz", not result["basarili"])

result = personel_puanla("", "staff1", 3)
test("Bos kullanici ID -> basarisiz", not result["basarili"])

print("\n--- personel_ortalama_getir ---")

_ratings.clear()
personel_puanla("user1", "staff1", 5)
personel_puanla("user2", "staff1", 4)
personel_puanla("user3", "staff1", 3)
result = personel_ortalama_getir("staff1")
test("Ortalama puan 4.0", result["ortalama_puan"] == 4.0)
test("3 degerlendirme", result["degerlendirme_sayisi"] == 3)
test("Inceleme gerekli degil (4.0 > 3.0)", not result["inceleme_gerekli"])

print("\n--- Dusuk puanli personel tespiti ---")

_ratings.clear()
personel_puanla("user1", "staff_bad", 1)
personel_puanla("user2", "staff_bad", 2)
personel_puanla("user3", "staff_bad", 1)
result = personel_ortalama_getir("staff_bad")
test("Dusuk puan: ortalama < 3.0", result["ortalama_puan"] < 3.0)
test("Dusuk puan: inceleme gerekli", result["inceleme_gerekli"])
test("UYARI mesaji var", "UYARI" in result["mesaj"])

print("\n--- dusuk_puanli_personelleri_getir ---")

# Iyi personeli de ekle
personel_puanla("user1", "staff_good", 5)
personel_puanla("user2", "staff_good", 5)
personel_puanla("user3", "staff_good", 5)
result = dusuk_puanli_personelleri_getir()
test("Sadece 1 dusuk puanli personel", len(result) == 1)
test("Dusuk puanli personel staff_bad", result[0]["personel_id"] == "staff_bad")

print("\n--- personel_yorumlarini_getir ---")

yorumlar = personel_yorumlarini_getir("staff_bad")
test("3 yorum var", len(yorumlar) == 3)

# Hic degerlendirme olmayan personel
result = personel_ortalama_getir("yok_personel")
test("Bilinmeyen personel: 0 degerlendirme", result["degerlendirme_sayisi"] == 0)


# ==================== SONUÇ ====================

print("\n" + "=" * 60)
total = passed + failed
print(f"SONUÇ: {passed}/{total} test başarılı")
if failed > 0:
    print(f"       {failed} test BAŞARISIZ!")
else:
    print("       Tüm testler geçti!")
print("=" * 60)

sys.exit(0 if failed == 0 else 1)
