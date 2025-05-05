# 🧰 KÁLLÓ-Fém termék scraper – Scrapy + Flask projekt

## ✍️ Készítette
   Gyarmati Bence
   2025. május
   Tesztfeladat – ASL Labs

Ez a projekt egy Python alapú webes scraper, amely a [https://kallofem.hu/shop/group/keriteselemek](https://kallofem.hu/shop/group/keriteselemek) oldalon található összes terméket gyűjti le.  
A begyűjtött adatokat JSON fájlba menti, és letölthetővé teszi egy weboldalon keresztül.

## 🔗 Online kipróbálható itt:
**https://kallofem-scraper.onrender.com**

- Nyomd meg a „Termékek frissítése” gombot
- Várd meg, hogy lefusson a scraper (kb. 1 perc)
- Amint lefutott a scraper megjelenik egy rövid részlet és a letöltési link az `output.json` fájlhoz.

## 🔍 Gyűjtött adatok

Minden termékről a következő információk kerülnek mentésre JSON formátumban:

- **Terméknév**
- **Ár**
- **Termékkép URL**

## 👩‍💻 Használt technológiák

- Python 3
- Scrapy
- Flask
- JSON export
- Render (ingyenes deploy)

## 🖥️ Lokális futtatás

1. Klónozd a repót:

```bash
git clone https://github.com/kiliamdev/kallofem-scraper.git
cd kallofem-scraper
