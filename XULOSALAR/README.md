# 📋 MUVOFIQLIK XULOSALARI KATALOGI
## ISO/IEC 17025:2019 § 7.8.6 va § 8.3 bo'yicha

> **EURO PROF TEST | Akkreditatsiyalangan Kalibrovka Laboratoriyasi**

---

## 📚 KATALOG MAQSADI

Ushbu katalog **EURO PROF TEST** laboratoriyasida foydalaniladigan o'lchov asboblari uchun **muvofiqlik xulosalari** (Statements of Conformity) ni tizimlashtiradi.

Har bir uskuna uchun:
- ✅ Kalibrovka sertifikati asosida to'liq tahlil
- ✅ ISO/IEC 17025:2019 talablariga muvofiqlik
- ✅ DevOps/dasturchilar uchun qulay YAML format
- ✅ Versiya nazorati (Git) uchun optimallashtirilgan
- ✅ Avtomatik tekshirish uchun strukturaviy ma'lumotlar

---

## 📂 FAYL STRUKTURASI

```
XULOSALAR/
├── README.md                                    # Ushbu fayl
├── MUVOFIQLIK_XULOSASI_TEMPLATE.md             # Bo'sh shablon
│
├── ISD3_2023387_MUVOFIQLIK_2026.md              # Brake Tester ISD-3
├── MEGAOMMETR_93753_MUVOFIQLIK_2024.md          # Megaommetr ЦС0202-2
│
└── [KEYINGI_USKUNALAR]/                         # Yangi uskunalar shu yerga
```

---

## 🔧 MAVJUD USKUNALAR RO'YXATI

### 1. **Brake Tester ISD-3** (СЕНСОРИКА М, №2023.387)

```yaml
equipment_id: "EPT-BT-ISD3-001"
document: "ISD3_2023387_MUVOFIQLIK_2026.md"
status: "✅ MUVOFIQ"
valid_until: "2027-01-02"
certificate: "ZD202601020251"
laboratory: "Shenzhen Zhongjidian (CNASL17800)"
standard: "JJG 1160-2019"
parameters:
  - "Tezlik: 0.72–180 km/h (±3.0 km/h)"
  - "Siljish: 1–200 m (±0.5%)"
last_updated: "2026-01-02"
```

**Ko'rish**: [ISD3_2023387_MUVOFIQLIK_2026.md](./ISD3_2023387_MUVOFIQLIK_2026.md)

---

### 2. **Megaommetr ЦС0202-2** (зав. №93753)

```yaml
equipment_id: "EPT-MM-CS0202-001"
document: "MEGAOMMETR_93753_MUVOFIQLIK_2024.md"
status: "✅ MUVOFIQ"
valid_until: "2026-05-13"
certificate: "UZ-07/206-2024"
laboratory: "O'zbekiston Milliy Metrologiya Instituti"
standard: "GOST 8.366-79"
parameters:
  - "Qarshilik: 200 kΩ – 100 GΩ (±2.5%)"
  - "Kuchlanish: 100V – 2500V"
last_updated: "2024-11-13"
```

**Ko'rish**: [MEGAOMMETR_93753_MUVOFIQLIK_2024.md](./MEGAOMMETR_93753_MUVOFIQLIK_2024.md)

---

## 📋 YANGI USKUNA QO'SHISH (WORKFLOW)

### 1️⃣ Kalibrovka sertifikatini qabul qilish

```bash
# Sertifikat faylini saqlash
certificates/
├── ZD202601020251.pdf
└── UZ-07-206-2024.pdf
```

### 2️⃣ Shablon nusxasini yaratish

```bash
cd XULOSALAR/
cp MUVOFIQLIK_XULOSASI_TEMPLATE.md YANGI_USKUNA_YYYY.md
```

### 3️⃣ Ma'lumotlarni to'ldirish

Quyidagi bo'limlarni sertifikat asosida to'ldiring:

- **Section 1**: Tashkilot va buyurtmachi
- **Section 2**: Uskuna identifikatsiyasi
- **Section 3**: Kalibrovka ma'lumotlari
- **Section 4**: Kalibrovka natijalari (jadvallar)
- **Section 5**: Muvofiqlik xulosasi
- **Section 6**: Imzolar

### 4️⃣ YAML validatsiyasini tekshirish

```bash
# Python bilan YAML bloklarini tekshirish
python3 scripts/validate_yaml.py YANGI_USKUNA_YYYY.md
```

### 5️⃣ Git'ga commit qilish

```bash
git add XULOSALAR/YANGI_USKUNA_YYYY.md
git commit -m "feat: Add conformity assessment for [USKUNA NOMI]"
git push origin main
```

---

## 🔍 MUVOFIQLIK XULOSASI ELEMENTI

Har bir hujjat quyidagi elementlarni o'z ichiga oladi:

### Metadata (Yuqorida)

```yaml
document_id: "EPT-YYYY-XXX"
revision: "1.0"
status: "APPROVED | DRAFT | EXPIRED"
issue_date: "YYYY-MM-DD"
valid_until: "YYYY-MM-DD"
classification: "CONFIDENTIAL - Client Use Only"
standard_compliance: "ISO/IEC 17025:2019 § 7.8.6, § 8.3"
```

### Core Content (Asosiy qism)

1. **Tashkilot va buyurtmachi** - Laboratoriya va mijoz ma'lumotlari
2. **Uskuna identifikatsiyasi** - Model, seriya, spetsifikatsiyalar
3. **Kalibrovka ma'lumotlari** - Sertifikat, laboratoriya, metod
4. **Kalibrovka natijalari** - Jadvallar, grafiklar, tahlil
5. **Muvofiqlik xulosasi** - Qaror, asoslar, cheklovlar
6. **Tasdiqlash** - Imzolar, muhur, tasdiqlar
7. **Qo'shimcha** - Traceability, ISO compliance, tavsiyalar
8. **Ilovalar** - Bog'liq hujjatlar ro'yxati

---

## 📊 AVTOMATIK HISOBOTLAR

### Amal qilish muddati monitoringi

```bash
# Python script - keyingi 90 kun ichida muddati tugaydigan uskunalar
python3 scripts/check_expiry.py --days 90
```

**Natija**:
```
⚠️ DIQQAT: Quyidagi uskunalar kalibrovkani talab qiladi:

1. Megaommetr ЦС0202-2 (№93753)
   Muddati: 2026-05-13 (120 kun qoldi)
   Fayl: MEGAOMMETR_93753_MUVOFIQLIK_2024.md
```

### Muvofiqlik holati summary

```bash
python3 scripts/generate_summary.py
```

**Natija**:
```
📊 MUVOFIQLIK XULOSALARI SUMMARY
================================

Jami uskunalar: 2
✅ Muvofiq: 2 (100%)
❌ Mos emas: 0 (0%)
⏰ Muddati o'tayotgan (30 kun): 0

Kalibrovka laboratoriyalari:
- Shenzhen Zhongjidian: 1
- UzNIM: 1
```

---

## 🔐 ISO/IEC 17025:2019 TALABLARI

Ushbu katalog quyidagi ISO 17025 bo'limlariga javob beradi:

### § 6.4 Jihozlar (Equipment)

- ✅ Har bir uskuna identifikatsiyalangan
- ✅ Kalibrovka holati aniq
- ✅ Kalibrovka sertifikatlari saqlanadi
- ✅ Kuzatuvchanlik (traceability) hujjatlangan

### § 7.8.6 Muvofiqlik xulosasi (Statements of conformity)

- ✅ Spetsifikatsiya aniq belgilangan
- ✅ Qaror qabul qilish qoidasi hujjatlangan
- ✅ O'lchov noaniqliklarini hisobga olish
- ✅ Muvofiqlik bayonoti aniq va tushunarli

### § 7.8.7 Fikr va sharhlar (Opinions and interpretations)

- ✅ Tavsiyalar aniq asoslangan
- ✅ Cheklovlar ko'rsatilgan
- ✅ Mas'uliyat belgisini qo'yish

### § 8.3 Hujjatlarni boshqarish (Control of records)

- ✅ Noyob hujjat identifikatori
- ✅ Versiya nazorati (Git)
- ✅ Tasdiq va imzolar hujjatlangan
- ✅ Arxivlash va saqlash tartibi

---

## 🛠️ YORDAMCHI SCRIPT'LAR

### 1. YAML Validatsiya

```python
# scripts/validate_yaml.py
import yaml
import sys

def validate_markdown_yaml(filename):
    """Markdown ichidagi YAML bloklarini tekshirish"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # YAML bloklarni topish
    yaml_blocks = re.findall(r'```yaml\n(.*?)\n```', content, re.DOTALL)
    
    for i, block in enumerate(yaml_blocks):
        try:
            yaml.safe_load(block)
            print(f"✅ YAML blok #{i+1}: OK")
        except yaml.YAMLError as e:
            print(f"❌ YAML blok #{i+1}: XATO - {e}")
            sys.exit(1)
    
    print(f"\n✅ Jami {len(yaml_blocks)} YAML blok tekshirildi - hammasi to'g'ri")

if __name__ == "__main__":
    validate_markdown_yaml(sys.argv[1])
```

### 2. Muddatini tekshirish

```python
# scripts/check_expiry.py
from datetime import datetime, timedelta
import re
import sys

def check_expiry_dates(days_threshold=90):
    """Muddati tugaydigan uskunalarni topish"""
    files = glob.glob("XULOSALAR/*.md")
    today = datetime.now()
    threshold = today + timedelta(days=days_threshold)
    
    expiring_soon = []
    
    for file in files:
        with open(file, 'r') as f:
            content = f.read()
        
        # valid_until sanasini topish
        match = re.search(r'valid_until: "(\d{4}-\d{2}-\d{2})"', content)
        if match:
            expiry_date = datetime.strptime(match.group(1), "%Y-%m-%d")
            
            if expiry_date < threshold:
                days_left = (expiry_date - today).days
                expiring_soon.append({
                    'file': file,
                    'expiry_date': expiry_date,
                    'days_left': days_left
                })
    
    # Natijalarni chiqarish
    if expiring_soon:
        print(f"⚠️ DIQQAT: {len(expiring_soon)} uskuna kalibrovkani talab qiladi:\n")
        for item in sorted(expiring_soon, key=lambda x: x['days_left']):
            print(f"- {item['file']}")
            print(f"  Muddati: {item['expiry_date'].strftime('%Y-%m-%d')}")
            print(f"  Qolgan kunlar: {item['days_left']}\n")
    else:
        print(f"✅ Hech qanday uskuna {days_threshold} kun ichida kalibrovka talab qilmaydi")
```

---

## 📖 QOIDALAR VA KONVENTSIYALAR

### Fayl nomlash

```
[USKUNA_MODELI]_[SERIYA]_MUVOFIQLIK_[YIL].md

Misol:
- ISD3_2023387_MUVOFIQLIK_2026.md
- MEGAOMMETR_93753_MUVOFIQLIK_2024.md
- MULTIMETR_34465A_MUVOFIQLIK_2025.md
```

### Document ID formati

```
EPT-YYYY-XXX

EPT = EURO PROF TEST
YYYY = Yil (4 raqam)
XXX = Ketma-ket raqam (001, 002, ...)

Misol:
- EPT-2026-001
- EPT-2024-002
```

### Equipment ID formati

```
EPT-[CATEGORY]-[MODEL]-[SEQUENCE]

Categories:
- BT = Brake Tester
- MM = Megohmmeter
- VM = Voltmeter
- CM = Clamp Meter
- MT = Multimeter
- ...

Misol:
- EPT-BT-ISD3-001
- EPT-MM-CS0202-001
```

---

## 🔄 YANGILASH JARAYONI

### Kalibrovka tugagach

1. Yangi sertifikat qabul qilish
2. Eski hujjatni arxivlash (status: EXPIRED)
3. Yangi muvofiqlik xulosasi yaratish
4. Git commit va push

```bash
# Eski hujjatni arxivlash
mkdir -p ARXIV/2024/
mv MEGAOMMETR_93753_MUVOFIQLIK_2024.md ARXIV/2024/

# Yangi hujjat yaratish
cp MUVOFIQLIK_XULOSASI_TEMPLATE.md MEGAOMMETR_93753_MUVOFIQLIK_2026.md
# ... to'ldirish ...

git add .
git commit -m "feat: Update Megaommetr calibration (2026)"
git push
```

---

## 📞 ALOQA VA YORDAM

**Texnik savollar**:
- Email: info@europroftest.uz
- Telefon: +998 [TELEFON]

**GitHub Issues**:
- Bug report: [Create Issue](https://github.com/[REPO]/issues/new?template=bug_report.md)
- Feature request: [Create Issue](https://github.com/[REPO]/issues/new?template=feature_request.md)

---

## 📝 LITSENZIYA

© 2024-2026 EURO PROF TEST | Barcha huquqlar himoyalangan

Ushbu hujjatlar **maxfiy** hisoblanadi va faqat EURO PROF TEST xodimlari va tegishli regulyativ organlar uchun mo'ljallangan.

---

**Oxirgi yangilanish**: 2026-06-09  
**Versiya**: 1.0.0  
**Muallif**: [SIZNING ISMINGIZ]
