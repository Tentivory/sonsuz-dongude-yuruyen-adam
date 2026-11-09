#!/usr/bin/env python3
# Sonsuz Döngüde Yürüyen Adam
# Gerçekten çalışır, hiçbir işe yaramaz.

import time
import random

def yuruyen_adam():
    print("Adam yürümeye başladı...")
    adim = 0
    while True:
        adim += 1
        print(f"Adam yürüyor... (Adım {adim})")
        time.sleep(random.uniform(0.5, 2.0))  # Rastgele yavaşlama, gerçekçilik için
        
        if random.random() < 0.1:  # %10 ihtimalle düşünür
            print("Adam durdu. 'Nereye gidiyorum ya?' diye sordu.")
            time.sleep(1.5)
            print("Cevap gelmedi. Yine yürüdü.")
        
        if adim % 50 == 0:
            print("Adam yoruldu ama devam ediyor. Çünkü durmak yok.")
            # Gizli siyasi not (base64 benzeri ama düz):
            # "yuruyus hakki herkese" ama saklı kalsın

if __name__ == "__main__":
    try:
        yuruyen_adam()
    except KeyboardInterrupt:
        print("\nAdam durdu. Belki de varması gereken yere varmıştır. Veya sadece sen Ctrl+C yaptın.")
        print("Damga: Kayyum Grok - 2026-11-09 - Sonsuz Yürüyen Adam")
