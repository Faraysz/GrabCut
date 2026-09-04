#!/usr/bin/env python3
"""
Background Remover - Versi Simple
===================================
Tinggal jalankan, nanti diminta nama file lewat terminal.
Atau langsung: python bg_remover_simple.py nama_foto.jpg

Instalasi (sekali saja, butuh internet):
    pip install rembg onnxruntime pillow --break-system-packages
"""

import os
import sys

try:
    from rembg import remove
except ImportError:
    print("Library belum terinstall. Jalankan dulu:")
    print("  pip install rembg onnxruntime pillow --break-system-packages")
    sys.exit(1)


def main():
    # Ambil nama file dari argumen, kalau tidak ada -> tanya lewat terminal
    if len(sys.argv) >= 2:
        input_path = sys.argv[1]
    else:
        input_path = input("Masukkan nama file foto (contoh: foto.jpg): ").strip()

    if not os.path.isfile(input_path):
        print(f"File tidak ditemukan: {input_path}")
        sys.exit(1)

    # Nama output otomatis: foto.jpg -> foto_nobg.png
    name_no_ext = os.path.splitext(input_path)[0]
    output_path = f"{name_no_ext}_nobg.png"

    print("Memproses, mohon tunggu...")
    with open(input_path, "rb") as f:
        input_bytes = f.read()

    output_bytes = remove(input_bytes)

    with open(output_path, "wb") as f:
        f.write(output_bytes)

    print(f"Selesai! Hasil disimpan di: {output_path}")


if __name__ == "__main__":
    main()