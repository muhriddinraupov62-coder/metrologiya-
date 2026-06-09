#!/usr/bin/env python3
"""
YAML Validatsiya Script
ISO 17025 muvofiqlik xulosalari uchun

Foydalanish:
    python3 scripts/validate_yaml.py XULOSALAR/ISD3_2023387_MUVOFIQLIK_2026.md
"""

import re
import sys
from pathlib import Path

# PyYAML o'rnatilmagan bo'lsa, oddiy tekshirish
try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False
    print("⚠️  PyYAML o'rnatilmagan - oddiy tekshirish rejimida ishlaymiz\n")


def simple_yaml_check(yaml_text):
    """
    Oddiy YAML tekshiruv (PyYAML o'rnatilmagan bo'lsa)
    """
    lines = yaml_text.split('\n')
    indent_stack = [0]
    
    for line_num, line in enumerate(lines, 1):
        # Bo'sh qatorlar va izohlarni o'tkazib yuborish
        stripped = line.lstrip()
        if not stripped or stripped.startswith('#'):
            continue
        
        # Indent tekshirish
        indent = len(line) - len(stripped)
        
        # Asosiy sintaksis tekshirish
        if ':' in line:
            # Key-value juftlik
            key_part = line.split(':')[0].strip()
            if not key_part:
                return False
        
        # Odatiy formatlangan list
        if stripped.startswith('- '):
            pass
    
    return True


def validate_markdown_yaml(filename):
    """
    Markdown faylidagi YAML bloklarni tekshirish
    
    Args:
        filename: Tekshiriladigan fayl nomi
        
    Returns:
        bool: True agar barcha YAML bloklar to'g'ri bo'lsa
    """
    filepath = Path(filename)
    
    if not filepath.exists():
        print(f"❌ XATO: Fayl topilmadi - {filename}")
        return False
    
    print(f"📄 Tekshirilmoqda: {filename}\n")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # YAML bloklarni topish
    yaml_blocks = re.findall(r'```yaml\n(.*?)\n```', content, re.DOTALL)
    
    if not yaml_blocks:
        print("⚠️  OGOHLANTIRISH: Hech qanday YAML blok topilmadi")
        return True
    
    print(f"🔍 Jami {len(yaml_blocks)} YAML blok topildi\n")
    
    errors = []
    
    for i, block in enumerate(yaml_blocks, 1):
        try:
            if YAML_AVAILABLE:
                # PyYAML bilan to'liq parsing
                parsed = yaml.safe_load(block)
                print(f"✅ YAML blok #{i}: OK")
                
                # Qo'shimcha tekshiruvlar
                if isinstance(parsed, dict):
                    print(f"   📊 {len(parsed)} ta kalit topildi")
            else:
                # Oddiy tekshirish - asosiy sintaksis xatolarini topish
                basic_check_passed = simple_yaml_check(block)
                if basic_check_passed:
                    print(f"✅ YAML blok #{i}: OK (basic check)")
                else:
                    raise ValueError("YAML sintaksis xatosi (basic check)")
                    
        except Exception as e:
            error_msg = f"YAML blok #{i}: SINTAKSIS XATOSI"
            print(f"❌ {error_msg}")
            print(f"   Tafsilot: {e}\n")
            errors.append((i, str(e)))
    
    print("\n" + "="*60)
    
    if errors:
        print(f"❌ XATO: {len(errors)} ta YAML blokda muammo topildi:")
        for block_num, error in errors:
            print(f"\n   Blok #{block_num}:")
            print(f"   {error}")
        return False
    else:
        print(f"✅ MUVAFFAQIYAT: Barcha {len(yaml_blocks)} YAML blok to'g'ri")
        return True


def validate_required_fields(filename):
    """
    Majburiy maydonlarni tekshirish
    """
    print(f"\n🔎 Majburiy maydonlarni tekshirish...\n")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    required_fields = {
        'document_id': r'document_id:\s*"([^"]+)"',
        'status': r'status:\s*"([^"]+)"',
        'issue_date': r'issue_date:\s*"(\d{4}-\d{2}-\d{2})"',
        'valid_until': r'valid_until:\s*"(\d{4}-\d{2}-\d{2})"',
        'equipment.serial_number': r'serial_number:\s*"([^"]+)"',
        'calibration.certificate_number': r'certificate_number:\s*"([^"]+)"',
    }
    
    missing = []
    found = []
    
    for field, pattern in required_fields.items():
        match = re.search(pattern, content)
        if match:
            value = match.group(1)
            found.append(f"   ✅ {field}: {value}")
        else:
            missing.append(f"   ❌ {field}: TOPILMADI")
    
    # Natijalarni chiqarish
    if found:
        print("Topilgan maydonlar:")
        for item in found:
            print(item)
    
    if missing:
        print("\n⚠️  Topilmagan majburiy maydonlar:")
        for item in missing:
            print(item)
    
    return len(missing) == 0


def main():
    if len(sys.argv) < 2:
        print("Foydalanish: python3 validate_yaml.py <fayl_nomi.md>")
        print("\nMisol:")
        print("  python3 scripts/validate_yaml.py XULOSALAR/ISD3_2023387_MUVOFIQLIK_2026.md")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    print("="*60)
    print("  ISO 17025 MUVOFIQLIK XULOSASI - YAML VALIDATOR")
    print("="*60)
    print()
    
    # YAML sintaksisini tekshirish
    yaml_valid = validate_markdown_yaml(filename)
    
    # Majburiy maydonlarni tekshirish
    fields_valid = validate_required_fields(filename)
    
    print("\n" + "="*60)
    print("  YAKUNIY NATIJA")
    print("="*60)
    
    if yaml_valid and fields_valid:
        print("✅ HAMMA TEKSHIRUVLAR O'TDI - Fayl to'g'ri!")
        sys.exit(0)
    else:
        print("❌ TEKSHIRUVLAR MUVAFFAQIYATSIZ - Tuzating va qaytadan urinib ko'ring")
        sys.exit(1)


if __name__ == "__main__":
    main()
