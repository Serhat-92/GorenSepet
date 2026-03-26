# -*- coding: utf-8 -*-
"""
Türkçe Yemek Tarifleri Veritabanı
Her yemek için gerekli malzemeler ve kategorileri tanımlanmıştır.
"""

RECIPES = {
    # --- Ana Yemekler ---
    "kısır": {
        "malzemeler": [
            {"ad": "İnce Bulgur", "miktar": "2 su bardağı", "kategori": "baklagil"},
            {"ad": "Salça (Domates)", "miktar": "2 yemek kaşığı", "kategori": "sos"},
            {"ad": "Salça (Biber)", "miktar": "1 yemek kaşığı", "kategori": "sos"},
            {"ad": "Maydanoz", "miktar": "1 demet", "kategori": "sebze"},
            {"ad": "Yeşil Soğan", "miktar": "4 adet", "kategori": "sebze"},
            {"ad": "Domates", "miktar": "2 adet", "kategori": "sebze"},
            {"ad": "Limon", "miktar": "2 adet", "kategori": "meyve"},
            {"ad": "Zeytinyağı", "miktar": "4 yemek kaşığı", "kategori": "yağ"},
            {"ad": "Nar Ekşisi", "miktar": "2 yemek kaşığı", "kategori": "sos"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Pul Biber", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Nane (Kuru)", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
        ],
        "kategori": "salata",
        "anahtar_kelimeler": ["kısır", "kisir", "bulgur salatası"],
    },
    "mercimek çorbası": {
        "malzemeler": [
            {"ad": "Kırmızı Mercimek", "miktar": "1.5 su bardağı", "kategori": "baklagil"},
            {"ad": "Soğan", "miktar": "1 adet", "kategori": "sebze"},
            {"ad": "Havuç", "miktar": "1 adet", "kategori": "sebze"},
            {"ad": "Patates", "miktar": "1 adet", "kategori": "sebze"},
            {"ad": "Salça (Domates)", "miktar": "1 yemek kaşığı", "kategori": "sos"},
            {"ad": "Tereyağı", "miktar": "1 yemek kaşığı", "kategori": "süt ürünü"},
            {"ad": "Zeytinyağı", "miktar": "2 yemek kaşığı", "kategori": "yağ"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Karabiber", "miktar": "yarım tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Pul Biber", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Limon", "miktar": "1 adet", "kategori": "meyve"},
        ],
        "kategori": "çorba",
        "anahtar_kelimeler": ["mercimek çorbası", "mercimek corbasi", "çorba"],
    },
    "menemen": {
        "malzemeler": [
            {"ad": "Yumurta", "miktar": "4 adet", "kategori": "süt ürünü"},
            {"ad": "Domates", "miktar": "3 adet", "kategori": "sebze"},
            {"ad": "Sivri Biber", "miktar": "3 adet", "kategori": "sebze"},
            {"ad": "Soğan", "miktar": "1 adet", "kategori": "sebze"},
            {"ad": "Zeytinyağı", "miktar": "2 yemek kaşığı", "kategori": "yağ"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Karabiber", "miktar": "yarım tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Pul Biber", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
        ],
        "kategori": "kahvaltı",
        "anahtar_kelimeler": ["menemen", "yumurtalı menemen"],
    },
    "karnıyarık": {
        "malzemeler": [
            {"ad": "Patlıcan", "miktar": "6 adet", "kategori": "sebze"},
            {"ad": "Kıyma", "miktar": "300 gr", "kategori": "et"},
            {"ad": "Soğan", "miktar": "2 adet", "kategori": "sebze"},
            {"ad": "Domates", "miktar": "2 adet", "kategori": "sebze"},
            {"ad": "Sivri Biber", "miktar": "3 adet", "kategori": "sebze"},
            {"ad": "Sarımsak", "miktar": "2 diş", "kategori": "sebze"},
            {"ad": "Salça (Domates)", "miktar": "1 yemek kaşığı", "kategori": "sos"},
            {"ad": "Sıvı Yağ", "miktar": "kızartma için", "kategori": "yağ"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Karabiber", "miktar": "yarım tatlı kaşığı", "kategori": "baharat"},
        ],
        "kategori": "ana yemek",
        "anahtar_kelimeler": ["karnıyarık", "karniyarik", "patlıcan"],
    },
    "imam bayıldı": {
        "malzemeler": [
            {"ad": "Patlıcan", "miktar": "6 adet", "kategori": "sebze"},
            {"ad": "Soğan", "miktar": "3 adet", "kategori": "sebze"},
            {"ad": "Domates", "miktar": "4 adet", "kategori": "sebze"},
            {"ad": "Sarımsak", "miktar": "4 diş", "kategori": "sebze"},
            {"ad": "Zeytinyağı", "miktar": "1 çay bardağı", "kategori": "yağ"},
            {"ad": "Maydanoz", "miktar": "yarım demet", "kategori": "sebze"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Şeker", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
        ],
        "kategori": "zeytinyağlı",
        "anahtar_kelimeler": ["imam bayıldı", "imam bayildi"],
    },
    "çiğ köfte": {
        "malzemeler": [
            {"ad": "İnce Bulgur", "miktar": "2 su bardağı", "kategori": "baklagil"},
            {"ad": "İsot (Pul Biber)", "miktar": "3 yemek kaşığı", "kategori": "baharat"},
            {"ad": "Salça (Domates)", "miktar": "2 yemek kaşığı", "kategori": "sos"},
            {"ad": "Salça (Biber)", "miktar": "1 yemek kaşığı", "kategori": "sos"},
            {"ad": "Soğan", "miktar": "2 adet", "kategori": "sebze"},
            {"ad": "Sarımsak", "miktar": "3 diş", "kategori": "sebze"},
            {"ad": "Yeşil Soğan", "miktar": "3 adet", "kategori": "sebze"},
            {"ad": "Maydanoz", "miktar": "1 demet", "kategori": "sebze"},
            {"ad": "Limon", "miktar": "2 adet", "kategori": "meyve"},
            {"ad": "Zeytinyağı", "miktar": "3 yemek kaşığı", "kategori": "yağ"},
            {"ad": "Nar Ekşisi", "miktar": "2 yemek kaşığı", "kategori": "sos"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Kimyon", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
        ],
        "kategori": "meze",
        "anahtar_kelimeler": ["çiğ köfte", "cig kofte", "çiğköfte"],
    },
    "yaprak sarma": {
        "malzemeler": [
            {"ad": "Asma Yaprağı", "miktar": "50 adet (1 kavanoz)", "kategori": "sebze"},
            {"ad": "Pirinç (Baldo)", "miktar": "1.5 su bardağı", "kategori": "baklagil"},
            {"ad": "Soğan", "miktar": "3 adet", "kategori": "sebze"},
            {"ad": "Domates", "miktar": "1 adet", "kategori": "sebze"},
            {"ad": "Maydanoz", "miktar": "1 demet", "kategori": "sebze"},
            {"ad": "Dereotu", "miktar": "yarım demet", "kategori": "sebze"},
            {"ad": "Nane (Taze)", "miktar": "yarım demet", "kategori": "sebze"},
            {"ad": "Zeytinyağı", "miktar": "yarım çay bardağı", "kategori": "yağ"},
            {"ad": "Limon", "miktar": "2 adet", "kategori": "meyve"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Karabiber", "miktar": "yarım tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Pul Biber", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
        ],
        "kategori": "zeytinyağlı",
        "anahtar_kelimeler": ["yaprak sarma", "sarma", "zeytinyağlı sarma"],
    },
    "etli pilav": {
        "malzemeler": [
            {"ad": "Pirinç (Baldo)", "miktar": "2 su bardağı", "kategori": "baklagil"},
            {"ad": "Kuşbaşı Et", "miktar": "300 gr", "kategori": "et"},
            {"ad": "Soğan", "miktar": "1 adet", "kategori": "sebze"},
            {"ad": "Tereyağı", "miktar": "2 yemek kaşığı", "kategori": "süt ürünü"},
            {"ad": "Sıvı Yağ", "miktar": "1 yemek kaşığı", "kategori": "yağ"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Karabiber", "miktar": "yarım tatlı kaşığı", "kategori": "baharat"},
        ],
        "kategori": "ana yemek",
        "anahtar_kelimeler": ["etli pilav", "pilav"],
    },
    "su böreği": {
        "malzemeler": [
            {"ad": "Yufka", "miktar": "6 adet", "kategori": "hamur"},
            {"ad": "Beyaz Peynir", "miktar": "400 gr", "kategori": "süt ürünü"},
            {"ad": "Yumurta", "miktar": "3 adet", "kategori": "süt ürünü"},
            {"ad": "Süt", "miktar": "1 su bardağı", "kategori": "süt ürünü"},
            {"ad": "Sıvı Yağ", "miktar": "yarım çay bardağı", "kategori": "yağ"},
            {"ad": "Maydanoz", "miktar": "1 demet", "kategori": "sebze"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
        ],
        "kategori": "börek",
        "anahtar_kelimeler": ["su böreği", "su boregi", "börek"],
    },
    "ezogelin çorbası": {
        "malzemeler": [
            {"ad": "Kırmızı Mercimek", "miktar": "1 su bardağı", "kategori": "baklagil"},
            {"ad": "Pirinç", "miktar": "3 yemek kaşığı", "kategori": "baklagil"},
            {"ad": "Bulgur", "miktar": "3 yemek kaşığı", "kategori": "baklagil"},
            {"ad": "Soğan", "miktar": "1 adet", "kategori": "sebze"},
            {"ad": "Salça (Domates)", "miktar": "1 yemek kaşığı", "kategori": "sos"},
            {"ad": "Salça (Biber)", "miktar": "1 tatlı kaşığı", "kategori": "sos"},
            {"ad": "Tereyağı", "miktar": "1 yemek kaşığı", "kategori": "süt ürünü"},
            {"ad": "Nane (Kuru)", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Pul Biber", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
        ],
        "kategori": "çorba",
        "anahtar_kelimeler": ["ezogelin çorbası", "ezogelin corbasi", "ezogelin"],
    },
    "iskender kebap": {
        "malzemeler": [
            {"ad": "Dana Et (Dönerlik)", "miktar": "500 gr", "kategori": "et"},
            {"ad": "Pide", "miktar": "2 adet", "kategori": "hamur"},
            {"ad": "Yoğurt", "miktar": "1 su bardağı", "kategori": "süt ürünü"},
            {"ad": "Domates", "miktar": "3 adet", "kategori": "sebze"},
            {"ad": "Sivri Biber", "miktar": "2 adet", "kategori": "sebze"},
            {"ad": "Tereyağı", "miktar": "3 yemek kaşığı", "kategori": "süt ürünü"},
            {"ad": "Salça (Domates)", "miktar": "1 yemek kaşığı", "kategori": "sos"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Karabiber", "miktar": "yarım tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Pul Biber", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
        ],
        "kategori": "kebap",
        "anahtar_kelimeler": ["iskender", "iskender kebap"],
    },
    "türlü": {
        "malzemeler": [
            {"ad": "Patlıcan", "miktar": "2 adet", "kategori": "sebze"},
            {"ad": "Kabak", "miktar": "2 adet", "kategori": "sebze"},
            {"ad": "Patates", "miktar": "2 adet", "kategori": "sebze"},
            {"ad": "Domates", "miktar": "3 adet", "kategori": "sebze"},
            {"ad": "Sivri Biber", "miktar": "4 adet", "kategori": "sebze"},
            {"ad": "Soğan", "miktar": "1 adet", "kategori": "sebze"},
            {"ad": "Sarımsak", "miktar": "3 diş", "kategori": "sebze"},
            {"ad": "Zeytinyağı", "miktar": "3 yemek kaşığı", "kategori": "yağ"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Karabiber", "miktar": "yarım tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Pul Biber", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
        ],
        "kategori": "ana yemek",
        "anahtar_kelimeler": ["türlü", "turlu", "sebze yemeği"],
    },
    "makarna": {
        "malzemeler": [
            {"ad": "Makarna (Penne)", "miktar": "500 gr", "kategori": "hamur"},
            {"ad": "Domates", "miktar": "3 adet", "kategori": "sebze"},
            {"ad": "Sarımsak", "miktar": "2 diş", "kategori": "sebze"},
            {"ad": "Zeytinyağı", "miktar": "3 yemek kaşığı", "kategori": "yağ"},
            {"ad": "Salça (Domates)", "miktar": "1 yemek kaşığı", "kategori": "sos"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Karabiber", "miktar": "yarım tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Fesleğen (Kuru)", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
        ],
        "kategori": "ana yemek",
        "anahtar_kelimeler": ["makarna", "soslu makarna"],
    },
    "omlet": {
        "malzemeler": [
            {"ad": "Yumurta", "miktar": "3 adet", "kategori": "süt ürünü"},
            {"ad": "Süt", "miktar": "2 yemek kaşığı", "kategori": "süt ürünü"},
            {"ad": "Kaşar Peyniri", "miktar": "50 gr", "kategori": "süt ürünü"},
            {"ad": "Tereyağı", "miktar": "1 yemek kaşığı", "kategori": "süt ürünü"},
            {"ad": "Tuz", "miktar": "bir tutam", "kategori": "baharat"},
            {"ad": "Karabiber", "miktar": "bir tutam", "kategori": "baharat"},
        ],
        "kategori": "kahvaltı",
        "anahtar_kelimeler": ["omlet", "yumurta"],
    },
    "lazanya": {
        "malzemeler": [
            {"ad": "Lazanya Yaprakları", "miktar": "1 paket", "kategori": "hamur"},
            {"ad": "Kıyma", "miktar": "400 gr", "kategori": "et"},
            {"ad": "Soğan", "miktar": "1 adet", "kategori": "sebze"},
            {"ad": "Sarımsak", "miktar": "2 diş", "kategori": "sebze"},
            {"ad": "Domates (Konserve)", "miktar": "1 kutu", "kategori": "sebze"},
            {"ad": "Salça (Domates)", "miktar": "1 yemek kaşığı", "kategori": "sos"},
            {"ad": "Süt", "miktar": "3 su bardağı", "kategori": "süt ürünü"},
            {"ad": "Un", "miktar": "3 yemek kaşığı", "kategori": "hamur"},
            {"ad": "Tereyağı", "miktar": "2 yemek kaşığı", "kategori": "süt ürünü"},
            {"ad": "Kaşar Peyniri", "miktar": "200 gr", "kategori": "süt ürünü"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Karabiber", "miktar": "yarım tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Muskat", "miktar": "bir tutam", "kategori": "baharat"},
        ],
        "kategori": "ana yemek",
        "anahtar_kelimeler": ["lazanya"],
    },
    "mercimek köftesi": {
        "malzemeler": [
            {"ad": "Kırmızı Mercimek", "miktar": "1.5 su bardağı", "kategori": "baklagil"},
            {"ad": "İnce Bulgur", "miktar": "1.5 su bardağı", "kategori": "baklagil"},
            {"ad": "Soğan", "miktar": "2 adet", "kategori": "sebze"},
            {"ad": "Yeşil Soğan", "miktar": "4 adet", "kategori": "sebze"},
            {"ad": "Maydanoz", "miktar": "1 demet", "kategori": "sebze"},
            {"ad": "Salça (Domates)", "miktar": "2 yemek kaşığı", "kategori": "sos"},
            {"ad": "Zeytinyağı", "miktar": "3 yemek kaşığı", "kategori": "yağ"},
            {"ad": "Limon", "miktar": "1 adet", "kategori": "meyve"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Pul Biber", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Kimyon", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
        ],
        "kategori": "meze",
        "anahtar_kelimeler": ["mercimek köftesi", "mercimek koftesi"],
    },
    "tarhana çorbası": {
        "malzemeler": [
            {"ad": "Tarhana", "miktar": "3 yemek kaşığı", "kategori": "baklagil"},
            {"ad": "Domates", "miktar": "1 adet", "kategori": "sebze"},
            {"ad": "Sivri Biber", "miktar": "1 adet", "kategori": "sebze"},
            {"ad": "Tereyağı", "miktar": "1 yemek kaşığı", "kategori": "süt ürünü"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Nane (Kuru)", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Pul Biber", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
        ],
        "kategori": "çorba",
        "anahtar_kelimeler": ["tarhana çorbası", "tarhana corbasi", "tarhana"],
    },
    "zeytinyağlı fasulye": {
        "malzemeler": [
            {"ad": "Taze Fasulye", "miktar": "500 gr", "kategori": "sebze"},
            {"ad": "Soğan", "miktar": "1 adet", "kategori": "sebze"},
            {"ad": "Domates", "miktar": "2 adet", "kategori": "sebze"},
            {"ad": "Sarımsak", "miktar": "2 diş", "kategori": "sebze"},
            {"ad": "Zeytinyağı", "miktar": "4 yemek kaşığı", "kategori": "yağ"},
            {"ad": "Şeker", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
        ],
        "kategori": "zeytinyağlı",
        "anahtar_kelimeler": ["zeytinyağlı fasulye", "taze fasulye", "fasulye"],
    },
    "patates kızartması": {
        "malzemeler": [
            {"ad": "Patates", "miktar": "4 adet", "kategori": "sebze"},
            {"ad": "Sıvı Yağ", "miktar": "kızartma için", "kategori": "yağ"},
            {"ad": "Tuz", "miktar": "1 tatlı kaşığı", "kategori": "baharat"},
        ],
        "kategori": "garnitür",
        "anahtar_kelimeler": ["patates kızartması", "patates", "kızartma"],
    },
    "pancake": {
        "malzemeler": [
            {"ad": "Un", "miktar": "1.5 su bardağı", "kategori": "hamur"},
            {"ad": "Süt", "miktar": "1 su bardağı", "kategori": "süt ürünü"},
            {"ad": "Yumurta", "miktar": "1 adet", "kategori": "süt ürünü"},
            {"ad": "Şeker", "miktar": "2 yemek kaşığı", "kategori": "baharat"},
            {"ad": "Kabartma Tozu", "miktar": "1 paket", "kategori": "baharat"},
            {"ad": "Tereyağı", "miktar": "1 yemek kaşığı", "kategori": "süt ürünü"},
            {"ad": "Vanilya", "miktar": "1 paket", "kategori": "baharat"},
        ],
        "kategori": "kahvaltı",
        "anahtar_kelimeler": ["pancake", "pankek", "krep"],
    },
}


def get_all_recipe_names() -> list[str]:
    """Tüm tarif isimlerini döndürür."""
    return list(RECIPES.keys())


def get_recipe(name: str) -> dict | None:
    """İsme göre tarif döndürür."""
    return RECIPES.get(name)


def get_all_keywords() -> dict[str, str]:
    """Tüm anahtar kelimeleri ve eşleşen tarif isimlerini döndürür."""
    keyword_map = {}
    for recipe_name, recipe_data in RECIPES.items():
        for keyword in recipe_data["anahtar_kelimeler"]:
            keyword_map[keyword] = recipe_name
    return keyword_map
