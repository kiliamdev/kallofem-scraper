# 🧰 KÁLLÓ-Fém termék adatgyűjtés – Scrapy projekt

Ez a projekt egy Scrapy-alapú webes adatgyűjtő (web scraper), amely a https://kallofem.hu/shop/group/keriteselemek oldalon található összes terméket gyűjti össze.

## 🔍 Gyűjtött adatok

Minden termékről a következő információk kerülnek mentésre JSON formátumban:

- **Terméknév**
- **Ár**
- **Termékkép URL**

## 👩‍💻 Használt technológiák

- Python 3
- Scrapy
- JSON export
- Render deploy

## ▶️ Használat helyben (lokálisan)

1. Klónozd a repót:
   ```bash
   git clone https://github.com/felhasznalonev/kallofem-scraper.git
   cd kallofem-scraper


