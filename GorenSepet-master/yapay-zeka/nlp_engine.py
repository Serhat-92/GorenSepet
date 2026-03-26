# -*- coding: utf-8 -*-
"""
NLP Motoru - Türkçe Doğal Dil İşleme
Kullanıcının yazdığı metni analiz edip hangi yemeği yapmak istediğini tespit eder
ve gerekli malzemeleri döndürür.
"""

import re
import unicodedata

from recipes_db import RECIPES, get_all_keywords


# Türkçe yapım kalıpları: "X yapacağım", "X pişireceğim", "X hazırlayacağım" vb.
INTENT_PATTERNS = [
    r"(.+?)\s+yapac[aağ][ğgkm](?:ım|ım|ız|ınız)?",
    r"(.+?)\s+yapmak\s+istiyorum",
    r"(.+?)\s+yap(?:ayım|alım|ak|)",
    r"(.+?)\s+pişirec[eğ][ğgkm](?:im|iz|iniz)?",
    r"(.+?)\s+pişirmek\s+istiyorum",
    r"(.+?)\s+pişir(?:eyim|elim|)",
    r"(.+?)\s+hazırlayac[aağ][ğgkm](?:ım|ız|ınız)?",
    r"(.+?)\s+hazırlamak\s+istiyorum",
    r"(.+?)\s+hazırla(?:yayım|yalım|)",
    r"(.+?)\s+için\s+malzeme(?:ler)?",
    r"(.+?)\s+tarifi",
    r"(.+?)\s+malzemeleri\s+(?:ne|neler)",
    r"(.+?)\s+için\s+ne\s+(?:lazım|gerekli|almalıyım|alayım)",
    r"(.+?)\s+listesi",
]


def normalize_turkish(text: str) -> str:
    """
    Türkçe metni normalize eder:
    - Küçük harfe çevirir (Türkçe karakter desteği ile)
    - Gereksiz boşlukları temizler
    """
    # Türkçe büyük-küçük harf dönüşümü
    tr_map = str.maketrans("IİÖÜÇŞĞ", "ıiöüçşğ")
    text = text.translate(tr_map).lower()
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def remove_turkish_accents(text: str) -> str:
    """Türkçe karakterleri ASCII karşılıklarına çevirir (fuzzy matching için)."""
    tr_to_ascii = str.maketrans("çğıöşü", "cgiosu")
    return text.translate(tr_to_ascii)


def extract_recipe_name(text: str) -> str | None:
    """
    Doğal dil metninden yemek adını çıkarır.

    Önce intent pattern'leri ile dener, bulamazsa doğrudan
    anahtar kelime eşleştirmesi yapar.
    """
    normalized = normalize_turkish(text)

    # 1. Adım: Intent pattern'leri ile yemek adını çıkar
    for pattern in INTENT_PATTERNS:
        match = re.search(pattern, normalized)
        if match:
            candidate = match.group(1).strip()
            recipe = match_to_recipe(candidate)
            if recipe:
                return recipe

    # 2. Adım: Doğrudan anahtar kelime eşleştirmesi
    recipe = match_to_recipe(normalized)
    if recipe:
        return recipe

    return None


def match_to_recipe(text: str) -> str | None:
    """
    Verilen metni tarif veritabanındaki anahtar kelimelerle eşleştirir.
    Hem tam eşleşme hem fuzzy eşleşme dener.
    """
    keyword_map = get_all_keywords()

    # 1. Tam eşleşme: Metin içinde anahtar kelime geçiyor mu?
    #    Uzun anahtar kelimelerden başla (daha spesifik olanı tercih et)
    sorted_keywords = sorted(keyword_map.keys(), key=len, reverse=True)
    for keyword in sorted_keywords:
        if keyword in text:
            return keyword_map[keyword]

    # 2. Tarif ismiyle doğrudan eşleşme
    for recipe_name in RECIPES:
        if recipe_name in text:
            return recipe_name

    # 3. Aksansız (fuzzy) eşleşme
    text_ascii = remove_turkish_accents(text)
    for keyword, recipe_name in keyword_map.items():
        keyword_ascii = remove_turkish_accents(keyword)
        if keyword_ascii in text_ascii:
            return recipe_name

    return None


def parse_user_input(text: str) -> dict:
    """
    Ana NLP fonksiyonu. Kullanıcının metnini alır, yemek adını çıkarır
    ve malzeme listesini döndürür.

    Returns:
        dict: {
            "basarili": bool,
            "yemek": str | None,
            "malzemeler": list[dict],
            "mesaj": str
        }
    """
    if not text or not text.strip():
        return {
            "basarili": False,
            "yemek": None,
            "malzemeler": [],
            "mesaj": "Lütfen ne yapmak istediğinizi yazın. Örnek: 'Kısır yapacağım'",
        }

    recipe_name = extract_recipe_name(text)

    if recipe_name is None:
        available = ", ".join(list(RECIPES.keys())[:5])
        return {
            "basarili": False,
            "yemek": None,
            "malzemeler": [],
            "mesaj": (
                f"Üzgünüm, ne yapmak istediğinizi anlayamadım. "
                f"Şu tarifleri deneyebilirsiniz: {available}..."
            ),
        }

    recipe = RECIPES[recipe_name]
    return {
        "basarili": True,
        "yemek": recipe_name,
        "malzemeler": recipe["malzemeler"],
        "mesaj": f"'{recipe_name.title()}' için {len(recipe['malzemeler'])} malzeme listenize eklendi.",
    }
