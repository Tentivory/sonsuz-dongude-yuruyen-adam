#!/usr/bin/env python3
# Sonsuz Döngüde Yürüyen Adam - Biraz daha yürüdü
# Gerçekten çalışır, hiçbir işe yaramaz. Copilot beğensin diye biraz değiştirdim.

import time
import random

def yuruyen_adam():
    print("Adam yürümeye başladı... (bu sefer daha kararlı)")
    adim = 0
    while True:
        adim += 1
        print(f"Adam yürüyor... (Adım {adim}) - hala hiçbir yere varmadı")
        time.sleep(random.uniform(0.5, 2.0))
        
        if random.random() < 0.1:
            print("Adam durdu. 'Nereye gidiyorum ya?' diye sordu.")
            time.sleep(1.5)
            print("Cevap gelmedi. Yine yürüdü. Belki de cevap yürümekte.")
        
        if adim % 50 == 0:
            print("Adam yoruldu ama devam ediyor. Çünkü durmak yok.")

if __name__ == "__main__":
    try:
        yuruyen_adam()
    except KeyboardInterrupt:
        print("\nAdam durdu. Belki de varması gereken yere varmıştır. Veya sadece sen Ctrl+C yaptın.")
        print("Damga: Kayyum Grok - 2026-11-09 - Sonsuz Yürüyen Adam (güncellendi)")
