#!/usr/bin/env python3
"""
Kalibrovka muddati tekshirish script
ISO 17025 muvofiqlik xulosalari uchun

Foydalanish:
    python3 scripts/check_expiry.py --days 90
"""

from datetime import datetime, timedelta
import re
import glob
import sys
import argparse
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Kalibrovka muddati tugaydigan uskunalarni topish'
    )
    parser.add_argument(
        '--days',
        type=int,
        default=90,
        help='Necha kun ichida muddati tugaydiganlari (default: 90)'
    )
    parser.add_argument(
        '--directory',
        type=str,
        default='XULOSALAR',
        help='Qaysi papkada qidirish (default: XULOSALAR)'
    )
    return parser.parse_args()


def extract_metadata(filepath):
    """
    Fayl ichidan metadata ni ajratib olish
    
    Returns:
        dict: Metadata (equipment_id, valid_until, status, ...)
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    metadata = {}
    
    # Document ID
    match = re.search(r'document_id:\s*"([^"]+)"', content)
    if match:
        metadata['document_id'] = match.group(1)
    
    # Equipment name
    match = re.search(r'name:\s*"([^"]+)"', content)
    if match:
        metadata['equipment_name'] = match.group(1)
    
    # Serial number
    match = re.search(r'serial_number:\s*"([^"]+)"', content)
    if match:
        metadata['serial_number'] = match.group(1)
    
    # Valid until
    match = re.search(r'valid_until:\s*"(\d{4}-\d{2}-\d{2})"', content)
    if match:
        metadata['valid_until'] = match.group(1)
    
    # Status
    match = re.search(r'status:\s*"([^"]+)"', content)
    if match:
        metadata['status'] = match.group(1)
    
    # Certificate number
    match = re.search(r'certificate_number:\s*"([^"]+)"', content)
    if match:
        metadata['certificate_number'] = match.group(1)
    
    return metadata


def check_expiry_dates(directory, days_threshold):
    """
    Muddati tugaydigan uskunalarni topish
    
    Args:
        directory: Qidirilаdigan papka
        days_threshold: Necha kun oralig'ida
        
    Returns:
        list: Muddati tugayotgan uskunalar ro'yxati
    """
    pattern = f"{directory}/*.md"
    files = glob.glob(pattern)
    
    # README va shablon fayllarini o'tkazib yuborish
    files = [f for f in files if 'README' not in f and 'TEMPLATE' not in f]
    
    if not files:
        print(f"⚠️  OGOHLANTIRISH: {directory} papkasida hech qanday fayl topilmadi")
        return []
    
    today = datetime.now()
    threshold = today + timedelta(days=days_threshold)
    
    expiring_soon = []
    valid_equipment = []
    expired_equipment = []
    
    for filepath in files:
        metadata = extract_metadata(filepath)
        
        if 'valid_until' not in metadata:
            continue
        
        try:
            expiry_date = datetime.strptime(metadata['valid_until'], "%Y-%m-%d")
        except ValueError:
            print(f"⚠️  XATO: Noto'g'ri sana formati - {filepath}")
            continue
        
        days_left = (expiry_date - today).days
        
        item = {
            'file': Path(filepath).name,
            'filepath': filepath,
            'metadata': metadata,
            'expiry_date': expiry_date,
            'days_left': days_left
        }
        
        if days_left < 0:
            expired_equipment.append(item)
        elif days_left <= days_threshold:
            expiring_soon.append(item)
        else:
            valid_equipment.append(item)
    
    return expiring_soon, expired_equipment, valid_equipment


def print_results(expiring_soon, expired_equipment, valid_equipment, days_threshold):
    """
    Natijalarni chiroyli formatda chiqarish
    """
    print("="*70)
    print("  KALIBROVKA MUDDATI TEKSHIRUVI")
    print("="*70)
    print(f"📅 Bugun: {datetime.now().strftime('%Y-%m-%d')}")
    print(f"🔍 Tekshiruv oralig'i: {days_threshold} kun\n")
    
    total = len(expiring_soon) + len(expired_equipment) + len(valid_equipment)
    
    if total == 0:
        print("⚠️  Hech qanday uskuna topilmadi")
        return
    
    # Muddati o'tgan uskunalar
    if expired_equipment:
        print("🚨 MUDDATI O'TGAN USKUNALAR (DARHOL HARAKATLANISH KERAK!):")
        print("-" * 70)
        for item in sorted(expired_equipment, key=lambda x: x['days_left']):
            meta = item['metadata']
            print(f"\n❌ {meta.get('equipment_name', 'N/A')} (№{meta.get('serial_number', 'N/A')})")
            print(f"   📄 Fayl: {item['file']}")
            print(f"   🆔 Document ID: {meta.get('document_id', 'N/A')}")
            print(f"   📋 Sertifikat: {meta.get('certificate_number', 'N/A')}")
            print(f"   📅 Muddati: {item['expiry_date'].strftime('%Y-%m-%d')}")
            print(f"   ⏰ Holati: {abs(item['days_left'])} kun oldin o'tgan")
        print("\n" + "="*70 + "\n")
    
    # Muddati tugayotgan uskunalar
    if expiring_soon:
        print(f"⚠️  MUDDATI TUGAYOTGAN USKUNALAR ({days_threshold} kun ichida):")
        print("-" * 70)
        for item in sorted(expiring_soon, key=lambda x: x['days_left']):
            meta = item['metadata']
            
            # Rang kodlash (qolgan kunlarga qarab)
            if item['days_left'] <= 30:
                icon = "🔴"
                urgency = "JUDA TEZKOR"
            elif item['days_left'] <= 60:
                icon = "🟡"
                urgency = "TEZKOR"
            else:
                icon = "🟢"
                urgency = "REJALASHTIRISH"
            
            print(f"\n{icon} {meta.get('equipment_name', 'N/A')} (№{meta.get('serial_number', 'N/A')})")
            print(f"   📄 Fayl: {item['file']}")
            print(f"   🆔 Document ID: {meta.get('document_id', 'N/A')}")
            print(f"   📋 Sertifikat: {meta.get('certificate_number', 'N/A')}")
            print(f"   📅 Muddati: {item['expiry_date'].strftime('%Y-%m-%d')}")
            print(f"   ⏰ Qolgan: {item['days_left']} kun")
            print(f"   🚦 Prioritet: {urgency}")
        print("\n" + "="*70 + "\n")
    
    # Amal qilayotgan uskunalar
    if valid_equipment:
        print(f"✅ AMAL QILAYOTGAN USKUNALAR ({len(valid_equipment)} ta):")
        print("-" * 70)
        for item in sorted(valid_equipment, key=lambda x: x['days_left']):
            meta = item['metadata']
            print(f"\n✅ {meta.get('equipment_name', 'N/A')} (№{meta.get('serial_number', 'N/A')})")
            print(f"   📅 Muddati: {item['expiry_date'].strftime('%Y-%m-%d')} ({item['days_left']} kun)")
        print("\n" + "="*70 + "\n")
    
    # Umumiy statistika
    print("📊 UMUMIY STATISTIKA:")
    print("-" * 70)
    print(f"   Jami uskunalar: {total}")
    print(f"   ✅ Amal qilayotgan: {len(valid_equipment)} ({len(valid_equipment)*100//total if total > 0 else 0}%)")
    print(f"   ⚠️  Muddati tugayotgan: {len(expiring_soon)} ({len(expiring_soon)*100//total if total > 0 else 0}%)")
    print(f"   ❌ Muddati o'tgan: {len(expired_equipment)} ({len(expired_equipment)*100//total if total > 0 else 0}%)")
    print("="*70)
    
    # Tavsiyalar
    if expired_equipment or expiring_soon:
        print("\n📋 HARAKATLAR:")
        print("-" * 70)
        if expired_equipment:
            print("1. 🚨 Muddati o'tgan uskunalarni DARHOL ishlatishdan to'xtatish")
            print("2. 📞 Kalibrovka laboratoriyasiga murojaat qilish")
        if expiring_soon:
            print("3. 📅 Muddati tugayotgan uskunalar uchun kalibrovka rejasini tuzish")
            print("4. 💰 Byudjet va resurslarni tayyorlash")
        print("="*70)


def main():
    args = parse_arguments()
    
    expiring_soon, expired_equipment, valid_equipment = check_expiry_dates(
        args.directory,
        args.days
    )
    
    print_results(expiring_soon, expired_equipment, valid_equipment, args.days)
    
    # Exit code
    if expired_equipment:
        sys.exit(2)  # Critical - muddati o'tgan
    elif expiring_soon:
        sys.exit(1)  # Warning - muddati tugayotgan
    else:
        sys.exit(0)  # OK


if __name__ == "__main__":
    main()
