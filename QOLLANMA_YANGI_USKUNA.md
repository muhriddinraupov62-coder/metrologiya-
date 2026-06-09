# 📘 QO'LLANMA: YANGI USKUNA UCHUN MUVOFIQLIK XULOSASI YARATISH

> **EURO PROF TEST | ISO/IEC 17025:2019**

---

## 🎯 MAQSAD

Ushbu qo'llanma yangi kalibrovka qilingan uskuna uchun **muvofiqlik xulosasi** yaratish jarayonini bosqichma-bosqich tushuntiradi.

---

## 📋 KERAKLI HUJJATLAR

Muvofiqlik xulosasi yaratishdan oldin quyidagilarni tayyorlab oling:

- ✅ **Kalibrovka sertifikati** (PDF format, akkreditatsiyalangan laboratoriyadan)
- ✅ **Uskuna pasporti** (tehnik spetsifikatsiyalar, model ma'lumotlari)
- ✅ **Metod hujjati** (GOST, ISO, JJG, yoki boshqa standart)
- ✅ **Oldingi kalibrovka tarixi** (agar mavjud bo'lsa)

---

## 🚀 BOSQICHMA-BOSQICH JARAYON

### 📥 BOSQICH 1: Kalibrovka sertifikatini qabul qilish

```bash
# 1. certificates/ papkasiga sertifikatni saqlang
cd metrologiya-
mkdir -p certificates/2026/
cp ~/Downloads/ZD202601020251.pdf certificates/2026/

# 2. Sertifikatni o'qing va asosiy ma'lumotlarni yozib oling:
# - Sertifikat raqami
# - Kalibrovka sanasi
# - Keyingi kalibrovka sanasi
# - Laboratoriya nomi va akkreditatsiya raqami
# - Metod/standart hujjat
# - Kalibrovka natijalari (jadvallar)
```

---

### 📝 BOSQICH 2: Shablon nusxasini yaratish

```bash
# 1. Shablon faylni nusxalash
cd XULOSALAR/
cp MUVOFIQLIK_XULOSASI_TEMPLATE.md [USKUNA]_[SERIYA]_MUVOFIQLIK_[YIL].md

# Misol:
cp MUVOFIQLIK_XULOSASI_TEMPLATE.md MULTIMETR_34465A_MUVOFIQLIK_2026.md
```

---

### 🔧 BOSQICH 3: Metadata ni to'ldirish

Fayl boshidagi **DOCUMENT METADATA** bo'limini to'ldiring:

```yaml
document_id: "EPT-2026-003"  # Ketma-ket raqam
revision: "1.0"
status: "DRAFT"  # Keyinchalik APPROVED ga o'zgaradi
issue_date: "2026-06-10"  # Bugungi sana
valid_until: "2027-06-10"  # Kalibrovka sertifikatidan
classification: "CONFIDENTIAL - Client Use Only"
standard_compliance: "ISO/IEC 17025:2019 § 7.8.6, § 8.3"
```

**Document ID qoidasi:**
- `EPT-YYYY-XXX`
- `YYYY` = Yil (4 raqam)
- `XXX` = Ketma-ket raqam (001, 002, 003, ...)

---

### 🏢 BOSQICH 4: Bo'lim 1 - Tashkilot va buyurtmachi

```yaml
laboratory:
  name: "EURO PROF TEST"
  address: "House 37A, Olimlar Street, Mirzo Ulugbek, Tashkent, Uzbekistan"
  accreditation:
    standard: "ISO/IEC 17025:2019"
    scope: "Kalibrovka laboratoriyasi"
    certificate_number: "[AKKREDITATSIYA RAQAMI]"
    valid_until: "[SANA]"
  contact:
    email: "info@europroftest.uz"
    phone: "+998 [TELEFON]"

client:
  name: "EURO PROF TEST (Internal Equipment)"  # yoki boshqa mijoz
  address: "Same as laboratory"
  contact_person: "[XODIM F.I.SH.]"
  request_date: "2026-06-01"
  delivery_date: "2026-06-10"
```

---

### 🔧 BOSQICH 5: Bo'lim 2 - Uskuna identifikatsiyasi

**Uskuna passportidan olgan ma'lumotlar:**

```yaml
equipment:
  # Asosiy identifikatsiya
  name: "Multimeter 34465A"  # Sertifikatdan
  model: "34465A"
  type: "Digital Multimeter"
  manufacturer: "Keysight Technologies"
  country: "USA"
  serial_number: "MY12345678"  # ❗ MUHIM: To'g'ri yozing
  manufacturing_date: "2023"
  
  # Ichki kuzatuv
  internal_id: "EPT-MM-34465A-001"  # O'zingiz yarating
  asset_number: "A-MY12345678"
  location: "Electrical Lab, Room 3"
  responsible_person: "[MAS'UL XODIM F.I.SH.]"
  
  # Tehnik spetsifikatsiyalar (passportdan)
  measurement_parameters:
    - parameter: "DC Voltage"
      range: "0.1 V – 1000 V"
      resolution: "0.001 mV"
      
    - parameter: "AC Voltage"
      range: "0.1 V – 750 V"
      resolution: "0.001 mV"
      
    - parameter: "Resistance"
      range: "100 Ω – 100 MΩ"
      resolution: "0.01 Ω"
```

**Equipment ID yaratish qoidasi:**
```
EPT-[CATEGORY]-[MODEL]-[SEQUENCE]

Categories (ikki harf):
- MM = Multimeter
- VM = Voltmeter
- CM = Clamp Meter
- BT = Brake Tester
- TH = Thermometer
- ...

Misol:
- EPT-MM-34465A-001
- EPT-VM-FLUKE87-001
```

---

### 📊 BOSQICH 6: Bo'lim 3 - Kalibrovka ma'lumotlari

**Sertifikatdan ma'lumotlarni ko'chirish:**

```yaml
calibration:
  # Sertifikat ma'lumotlari
  certificate_number: "CAL-2026-1234"  # Sertifikatdan
  issue_date: "2026-06-05"
  calibration_date: "2026-06-05"
  next_calibration_date: "2027-06-05"  # Odatda 12 oy
  calibration_interval: "12 months"
  pages: 8
  
  # Kalibrovka laboratoriyasi
  laboratory:
    name: "Milliy Metrologiya Instituti"
    address: "Tashkent, Uzbekistan"
    accreditation:
      body: "O'zbekiston Akkreditatsiya Agentligi"
      number: "UZ-CAL-12345"
      scope: "Elektr o'lchov asboblari"
    competence: "ISO/IEC 17025:2017"
    
  # Metod hujjati
  reference_standard:
    document: "GOST 8.027-2001"  # yoki boshqa
    title: "ГСИ. Мультиметры цифровые. Методика поверки"
    country: "Russia/Uzbekistan"
    authority: "Gosstandart"
    status: "Current"
    
  # Muhit sharoitlari (sertifikatdan)
  environment:
    temperature:
      value: 23.0
      unit: "°C"
      tolerance: "±2°C"
      
    humidity:
      value: 50
      unit: "%RH"
      tolerance: "30-70%"
      
    location: "Indoor Laboratory (Controlled Environment)"
```

---

### 📐 BOSQICH 7: Bo'lim 4 - Kalibrovka natijalari

**Sertifikatdagi jadvaldan ma'lumotlarni ko'chirish:**

#### Misol: DC Voltage o'lchash

```yaml
dc_voltage_measurement:
  parameter: "DC Voltage"
  measurement_range: "0.1 V – 1000 V"
  unit: "V"
  
  acceptance_criteria:
    accuracy: "0.05% + 2 digits"  # Passportdan
    source: "Manufacturer specification"
    
  expanded_uncertainty:
    value: 0.02  # Sertifikatdan
    unit: "%"
    coverage_factor: 2
    confidence_level: "95%"
    
  calibration_results:
    # Nuqta 1
    - point_id: "V-DC-01"
      nominal_value: 1.0  # Sertifikatdan
      measured_value: 1.0001  # Sertifikatdan
      indication_error: 0.0001  # Hisoblash: measured - nominal
      relative_error_percent: 0.01  # Hisoblash: (error/nominal)*100
      mpe: 0.0005  # Maximum Permissible Error (±0.05% dan)
      within_tolerance: true  # |error| <= mpe
      result: "PASS"
      notes: "1V diapazon"
      
    # Nuqta 2
    - point_id: "V-DC-02"
      nominal_value: 10.0
      measured_value: 10.0003
      indication_error: 0.0003
      relative_error_percent: 0.003
      mpe: 0.005
      within_tolerance: true
      result: "PASS"
      notes: "10V diapazon"
      
    # ... boshqa nuqtalar
      
  statistical_analysis:
    number_of_points: 6
    passed_points: 6
    failed_points: 0
    pass_rate: 100.0
    
    max_positive_error: +0.0003
    max_negative_error: -0.0002
    max_absolute_error: 0.0003
    
  conclusion: "✅ MUVOFIQ - Barcha nuqtalarda spetsifikatsiya ichida"
```

**HISOBLASH FORMULALARI:**

```python
# Indication Error (Ko'rsatuv xatosi)
indication_error = measured_value - nominal_value

# Relative Error (Nisbiy xato, %)
relative_error_percent = (indication_error / nominal_value) * 100

# MPE (Maximum Permissible Error)
# Passportdan yoki standartdan olinadi
# Misol: ±0.05% + 2 digits
mpe = (0.05 / 100) * nominal_value + 2 * resolution

# Muvofiqlik tekshiruvi
if abs(indication_error) <= mpe:
    result = "PASS" (MUVOFIQ)
else:
    result = "FAIL" (MOS EMAS)
```

---

### ✅ BOSQICH 8: Bo'lim 5 - Muvofiqlik xulosasi

```yaml
conformity_assessment:
  assessment_id: "CA-2026-003"
  assessment_date: "2026-06-10"
  assessed_by: "[TEKSHIRUVCHI F.I.SH.]"
  
  specification:
    document: "Manufacturer Specification + GOST 8.027-2001"
    requirements:
      dc_voltage_accuracy: "±0.05% + 2 digits"
      ac_voltage_accuracy: "±0.1% + 2 digits"
      resistance_accuracy: "±0.1%"
      
  decision_rule:
    method: "Simple Acceptance"
    description: |
      O'lchash xatosi MPE (Maximum Permissible Error) ichida bo'lsa,
      uskuna MUVOFIQ deb baholanadi.
      
      Qaror qabul qilish qoidasi:
      - |Indication Error| ≤ MPE → MUVOFIQ
      - |Indication Error| > MPE → MOS EMAS
      
      ISO/IEC 17025:2019 § 7.8.6.2 bo'yicha
    
  results:
    dc_voltage:
      status: "✅ MUVOFIQ"
      passed_points: 6
      total_points: 6
      pass_rate: "100%"
      max_error: "0.01%"
      tolerance: "±0.05%"
      margin: "0.04% (80% margin)"
      remarks: "Barcha nuqtalarda spetsifikatsiya ichida"
      
    # ... boshqa parametrlar
      
  overall_conclusion:
    status: "✅ MUVOFIQ (CONFORMING)"
    decision: "FOYDALANISHGA RUXSAT ETILADI (APPROVED FOR USE)"
    confidence_level: "HIGH"
    
    validity_period:
      start_date: "2026-06-10"
      end_date: "2027-06-10"
      duration_days: 365
      
    limitations:
      - "Faqat ko'rsatilgan o'lchov diapazonlari ichida"
      - "Belgilangan kalibrovka intervali (12 oy) saqlanadi"
      - "Mexanik zarba yoki ta'mirdan keyin qayta kalibrovka"
      
    recommendations:
      - "Oylik vizual tekshiruv"
      - "6 oylik oraliq tekshiruv (intermediate check)"
      - "Sertifikatni uskuna yonida saqlash"
```

---

### 🔐 BOSQICH 9: Bo'lim 6 - Imzolar

```yaml
document_control:
  prepared_by:
    role: "Kalibrovka texniki"
    name: "[SIZNING ISMINGIZ]"
    signature: "________________"
    date: "2026-06-10"
    
  reviewed_by:
    role: "Texnik rahbar"
    name: "[RAHBAR ISMI]"
    signature: "________________"
    date: "2026-06-10"
    
  approved_by:
    role: "Sifat rahbari"
    name: "[SIFAT RAHBAR ISMI]"
    signature: "________________"
    date: "2026-06-10"
    
  seal:
    required: true
    applied: false  # Chop bosilganidan keyin true
    location: "[MUHR UCHUN JOY]"
```

---

### 🔍 BOSQICH 10: Validatsiya

Fayl to'ldirilganidan keyin, tekshirish:

```bash
# 1. YAML sintaksisini tekshirish
python3 scripts/validate_yaml.py XULOSALAR/MULTIMETR_34465A_MUVOFIQLIK_2026.md

# Natija (agar to'g'ri bo'lsa):
# ✅ HAMMA TEKSHIRUVLAR O'TDI - Fayl to'g'ri!

# 2. Muddatni tekshirish
python3 scripts/check_expiry.py --days 90
```

---

### 💾 BOSQICH 11: Git'ga commit qilish

```bash
# 1. Status tekshirish
git status

# 2. Faylni qo'shish
git add XULOSALAR/MULTIMETR_34465A_MUVOFIQLIK_2026.md
git add certificates/2026/CAL-2026-1234.pdf

# 3. Commit
git commit -m "feat: Add conformity assessment for Multimeter 34465A (№MY12345678)

- ✅ Kalibrovka sertifikati: CAL-2026-1234
- ✅ Muvofiqlik xulosasi: EPT-2026-003
- ✅ Amal qilish muddati: 2027-06-10
- ✅ Barcha parametrlar MUVOFIQ"

# 4. Push
git push origin main
```

---

### 📄 BOSQICH 12: Status o'zgartirish

Hujjat tasdiqlangandan keyin:

```yaml
# Fayl boshida
status: "APPROVED"  # DRAFT → APPROVED

# Bo'lim 6 da
seal:
  applied: true  # false → true
```

Yana commit:

```bash
git add XULOSALAR/MULTIMETR_34465A_MUVOFIQLIK_2026.md
git commit -m "docs: Approve conformity assessment EPT-2026-003"
git push origin main
```

---

## 🎯 TEZKOR TEKSHIRUV RO'YXATI (CHECKLIST)

Hujjat yaratishda quyidagilarni tekshiring:

### ✅ Metadata
- [ ] Document ID to'g'ri formatda (EPT-YYYY-XXX)
- [ ] Issue date va valid_until to'g'ri
- [ ] Status belgilangan (DRAFT/APPROVED)

### ✅ Uskuna ma'lumotlari
- [ ] Seriya raqami to'g'ri ko'chirilgan
- [ ] Model va ishlab chiqaruvchi to'g'ri
- [ ] Equipment ID yaratilgan (EPT-XX-XXX-XXX)

### ✅ Kalibrovka ma'lumotlari
- [ ] Sertifikat raqami to'g'ri
- [ ] Laboratoriya va akkreditatsiya ma'lumotlari to'liq
- [ ] Metod hujjat ko'rsatilgan

### ✅ Kalibrovka natijalari
- [ ] Barcha kalibrovka nuqtalari kiritilgan
- [ ] Hisoblashlar to'g'ri (indication_error, relative_error)
- [ ] Muvofiqlik xulosasi har bir nuqta uchun (PASS/FAIL)

### ✅ Muvofiqlik xulosasi
- [ ] Decision rule aniq belgilangan
- [ ] Overall conclusion berilgan
- [ ] Limitations va recommendations yozilgan

### ✅ Imzolar
- [ ] Barcha rol egalarining ismlari kiritilgan
- [ ] Sanalar to'g'ri

### ✅ Validatsiya
- [ ] YAML syntax tekshirilgan
- [ ] Majburiy maydonlar to'ldirilgan
- [ ] Git'ga commit qilingan

---

## 📞 YORDAM VA SAVOLLAR

**Agar qiyinchilik tug'ilsa:**

1. **Shablon faylni ko'ring**: `MUVOFIQLIK_XULOSASI_TEMPLATE.md`
2. **Namuna fayllarni ko'ring**:
   - `XULOSALAR/ISD3_2023387_MUVOFIQLIK_2026.md`
   - `XULOSALAR/MEGAOMMETR_93753_MUVOFIQLIK_2024.md`
3. **README ni o'qing**: `XULOSALAR/README.md`

**Texnik yordam:**
- Email: info@europroftest.uz
- Telegram: [TELEGRAM KANAL]

---

## 🔄 KEYINGI QADAMLAR

Muvofiqlik xulosasi yaratilganidan keyin:

1. **Arxivlash**: Sertifikat va xulosani papkaga saqlash
2. **Label yapish**: Uskuna ustiga kalibrovka label'ini yopishtirish
3. **Ro'yxatga kiritish**: Laboratoriya ro'yxatiga qo'shish
4. **Monitoring**: Muddatni kuzatish (check_expiry.py)

---

**© 2026 EURO PROF TEST | ISO/IEC 17025:2019**
