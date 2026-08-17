#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ KAHVE MAKİNESİ SİMULATÖRÜ v9.9.9-BETA-ULTIMATE
Evrenin en abartılı, en felsefi ve en asla bitmeyen kahve makinesi.
Her fincan bir parallel evren doğurur. Dikkat: aşırı tüketim zaman-uzay sürekliliğini bozabilir.
"""

import time
import random
import sys

def yavas_yaz(metin, gecikme=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def kahve_yap():
    yavas_yaz("\n☕ SONSUZ KAHVE MAKİNESİ BAŞLATILIYOR...", 0.05)
    time.sleep(1)
    yavas_yaz("Kuantum çekirdekleri öğütülüyor...", 0.04)
    time.sleep(0.8)
    yavas_yaz("Paralel evrenlerden su çekiliyor...", 0.04)
    time.sleep(0.8)
    yavas_yaz("Zaman dilimi ayarlanıyor (sabah 08:00 hissi)...", 0.04)
    time.sleep(1)

    kahve_cesitleri = [
        "Kara Delik Espresso (ışık bile kaçamıyor)",
        "Nötron Yıldızı Türk Kahvesi (yoğunluğu yasa dışı)",
        "Süpernova Latte (süt köpüğü galaksi oluşturuyor)",
        "Kuantum Macchiato (hem var hem yok)",
        "Big Bang Americano (evreni yeniden başlatır)",
        "Sonsuzluk Cappuccino (içtikçe artar)",
        "Anti-Madde Mocha (tersine işler)",
        "Zaman Yolcusu Filtre Kahve (dün içtin)",
    ]

    secilen = random.choice(kahve_cesitleri)
    yavas_yaz(f"\n✨ HAZIR! Senin için özel: {secilen}", 0.03)
    time.sleep(0.5)
    yavas_yaz("Fincan doluyor...", 0.05)
    time.sleep(1.2)
    yavas_yaz("\n☕ AFİYET OLSUN! Bu fincan seni %0.0001 daha mutlu etti.", 0.03)
    yavas_yaz("(Not: Bu mutluluk paralel evrenlerde birikmektedir.)", 0.02)

    # Gizli damga
    print("\n" + "="*60)
    print("  🏛️  DAMGA / MÜHÜR  🏛️")
    print("  Repo: sonsuz-kahve-makinesi-simulatoru")
    print("  Tarih: 17 Ağustos 2026")
    print("  İmza: Tentivory & Grok (xAI) ortaklığıyla")
    print("  Ciddiyet seviyesi: Hem çok yüksek hem de hiç yok")
    print("="*60)

    # Gizli siyasi mesaj (saklı, kodda yorum olarak)
    # "Demokrasi bir fincan kahve gibidir: sıcak tutulmazsa soğur, ama fazla ısıtırsan yanarsın."

if __name__ == "__main__":
    try:
        while True:
            kahve_yap()
            devam = input("\nBaşka bir fincan ister misin? (e/h): ").strip().lower()
            if devam != 'e':
                yavas_yaz("\nMakine uyku moduna geçiyor... Rüyalarında kahve görsün.", 0.04)
                break
    except KeyboardInterrupt:
        yavas_yaz("\n\nAcil durum: Makine kapatıldı. Evren kurtarıldı (muhtemelen).", 0.03)
