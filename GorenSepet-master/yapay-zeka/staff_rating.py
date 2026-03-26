# -*- coding: utf-8 -*-
"""
Personel Puanlama Servisi

Alışveriş sonunda kullanıcı, kendisine yardım eden personele puan verir.
Düşük puanlı personel sistem tarafından incelemeye alınır.
"""

from datetime import datetime

# Bellek içi veri deposu (gerçek projede Supabase/PostgreSQL kullanılacak)
_ratings: list[dict] = []

# Düşük puan eşiği: Bu değerin altındaki ortalamaya sahip personel incelemeye alınır
DUSUK_PUAN_ESIGI = 3.0
# İnceleme için minimum değerlendirme sayısı
MIN_DEGERLENDIRME_SAYISI = 3


def personel_puanla(
    kullanici_id: str,
    personel_id: str,
    puan: int,
    yorum: str = "",
) -> dict:
    """
    Personele puan verir.

    Args:
        kullanici_id: Puan veren kullanıcının ID'si
        personel_id: Puanlanan personelin ID'si
        puan: 1-5 arası puan
        yorum: Opsiyonel kullanıcı yorumu

    Returns:
        dict: Puanlama sonucu
    """
    if not 1 <= puan <= 5:
        return {
            "basarili": False,
            "mesaj": "Puan 1 ile 5 arasinda olmalidir.",
        }

    if not kullanici_id or not personel_id:
        return {
            "basarili": False,
            "mesaj": "Kullanici ve personel ID'si zorunludur.",
        }

    rating = {
        "kullanici_id": kullanici_id,
        "personel_id": personel_id,
        "puan": puan,
        "yorum": yorum,
        "tarih": datetime.now().isoformat(),
    }
    _ratings.append(rating)

    return {
        "basarili": True,
        "mesaj": f"Personele {puan}/5 puan verildi. Tesekkurler!",
        "puan": puan,
    }


def personel_ortalama_getir(personel_id: str) -> dict:
    """
    Bir personelin ortalama puanini ve degerlendirme sayisini dondurur.

    Args:
        personel_id: Personelin ID'si

    Returns:
        dict: Ortalama puan bilgisi
    """
    personel_puanlari = [r for r in _ratings if r["personel_id"] == personel_id]

    if not personel_puanlari:
        return {
            "personel_id": personel_id,
            "ortalama_puan": 0.0,
            "degerlendirme_sayisi": 0,
            "inceleme_gerekli": False,
            "mesaj": "Bu personel henuz degerlendirilmemis.",
        }

    toplam = sum(r["puan"] for r in personel_puanlari)
    sayi = len(personel_puanlari)
    ortalama = toplam / sayi

    inceleme = (ortalama < DUSUK_PUAN_ESIGI and sayi >= MIN_DEGERLENDIRME_SAYISI)

    mesaj = ""
    if inceleme:
        mesaj = (
            f"UYARI: Personelin ortalama puani {ortalama:.1f}/5 "
            f"({sayi} degerlendirme). Inceleme gerekli!"
        )

    return {
        "personel_id": personel_id,
        "ortalama_puan": round(ortalama, 2),
        "degerlendirme_sayisi": sayi,
        "inceleme_gerekli": inceleme,
        "mesaj": mesaj,
    }


def dusuk_puanli_personelleri_getir() -> list[dict]:
    """
    Inceleme gerektiren (dusuk puanli) tum personelleri listeler.

    Returns:
        list[dict]: Dusuk puanli personel listesi
    """
    # Tum benzersiz personel ID'lerini bul
    personel_idler = set(r["personel_id"] for r in _ratings)

    dusuk_puanlilar = []
    for pid in personel_idler:
        sonuc = personel_ortalama_getir(pid)
        if sonuc["inceleme_gerekli"]:
            dusuk_puanlilar.append(sonuc)

    # En dusuk puandan en yuksege sirala
    dusuk_puanlilar.sort(key=lambda x: x["ortalama_puan"])
    return dusuk_puanlilar


def personel_yorumlarini_getir(personel_id: str) -> list[dict]:
    """
    Bir personele yapilan tum degerlendirmeleri dondurur.

    Args:
        personel_id: Personelin ID'si

    Returns:
        list[dict]: Degerlendirme listesi
    """
    return [
        {
            "kullanici_id": r["kullanici_id"],
            "puan": r["puan"],
            "yorum": r["yorum"],
            "tarih": r["tarih"],
        }
        for r in _ratings
        if r["personel_id"] == personel_id
    ]
