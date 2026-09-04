#!/usr/bin/env python3
"""
GrabCut Background Remover - CLI Tool
Usage:
    python grabcut_bg.py <input_image> [output_image] [--bbox x,y,w,h] [--iter N]

Examples:
    python grabcut_bg.py foto.jpg
    python grabcut_bg.py foto.jpg hasil.png --bbox 100,50,300,400 --iter 5
"""

import cv2
import numpy as np
import argparse
import os
import sys
from pathlib import Path


def auto_bbox(image, padding=20):
    """
    Deteksi bounding box otomatis.
    Strategy: cari area foreground dengan edge detection + contour.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Canny edge detection
    edges = cv2.Canny(gray, 50, 150)

    # Dilate edges untuk mengisi gap
    kernel = np.ones((7, 7), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=2)
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, iterations=3)

    # Cari kontur
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Ambil kontur terbesar
        largest = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)
        img_area = image.shape[0] * image.shape[1]

        # Hanya pakai kalau kontur cukup besar (minimal 5% gambar)
        if area > img_area * 0.05:
            x, y, w, h = cv2.boundingRect(largest)
            img_h, img_w = image.shape[:2]
            x = max(0, x - padding)
            y = max(0, y - padding)
            w = min(img_w - x, w + 2*padding)
            h = min(img_h - y, h + 2*padding)
            return (x, y, w, h)

    # Fallback: area tengah 70% gambar
    h, w = image.shape[:2]
    margin_x = int(w * 0.15)
    margin_y = int(h * 0.15)
    return (margin_x, margin_y, w - 2*margin_x, h - 2*margin_y)


def remove_background(image_path, output_path=None, bbox=None, iterations=5, padding=20):
    """Hapus background menggunakan GrabCut OpenCV."""

    print(f"📂 Membaca: {image_path}")
    img = cv2.imread(str(image_path))
    if img is None:
        print(f"❌ Error: Tidak bisa membaca gambar '{image_path}'")
        sys.exit(1)

    h, w = img.shape[:2]
    print(f"📐 Ukuran gambar: {w}x{h}")

    # Tentukan bounding box
    if bbox:
        rect = tuple(bbox)
        print(f"📦 Bounding box manual: {rect}")
    else:
        print("🔍 Mendeteksi bounding box otomatis...")
        rect = auto_bbox(img, padding=padding)
        print(f"📦 Bounding box auto: {rect}")

    # Validasi bbox
    if rect[2] <= 0 or rect[3] <= 0:
        print("❌ Error: Bounding box tidak valid (width/height <= 0)")
        sys.exit(1)
    if rect[0] < 0 or rect[1] < 0 or rect[0]+rect[2] > w or rect[1]+rect[3] > h:
        print("❌ Error: Bounding box di luar area gambar")
        sys.exit(1)

    # Inisialisasi mask dan model
    mask = np.zeros(img.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    # Jalankan GrabCut
    print(f"⚙️  Menjalankan GrabCut ({iterations} iterasi)...")
    try:
        cv2.grabCut(img, mask, rect, bgdModel, fgdModel, iterations, cv2.GC_INIT_WITH_RECT)
    except cv2.error as e:
        print(f"❌ GrabCut gagal: {e}")
        print("💡 Tips: Coba gunakan --bbox manual, contoh: --bbox 50,50,300,300")
        sys.exit(1)

    # Buat mask final
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # Buat gambar RGBA dengan alpha channel
    rgba = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    rgba[:, :, 3] = mask2 * 255

    # Simpan hasil
    if output_path is None:
        stem = Path(image_path).stem
        output_path = f"{stem}_transparent.png"

    success = cv2.imwrite(str(output_path), rgba)
    if success:
        print(f"✅ Berhasil! Hasil disimpan: {output_path}")
        size_kb = os.path.getsize(output_path) / 1024
        print(f"📊 Ukuran file: {size_kb:.1f} KB")
    else:
        print(f"❌ Gagal menyimpan ke '{output_path}'")
        sys.exit(1)

    return output_path


def parse_bbox(s):
    """Parse string bbox 'x,y,w,h' ke tuple."""
    try:
        parts = [int(p.strip()) for p in s.split(',')]
        if len(parts) != 4:
            raise ValueError
        return tuple(parts)
    except ValueError:
        raise argparse.ArgumentTypeError("Format bbox harus: x,y,w,h (contoh: 100,50,300,400)")


def main():
    parser = argparse.ArgumentParser(
        description="Hapus background gambar menggunakan GrabCut OpenCV",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Contoh penggunaan:
  python grabcut_bg.py foto.jpg                    # Auto detect bbox
  python grabcut_bg.py foto.jpg hasil.png          # Output custom
  python grabcut_bg.py foto.jpg --bbox 50,30,200,250  # Bbox manual
  python grabcut_bg.py foto.jpg --iter 10          # Iterasi lebih banyak
        """
    )
    parser.add_argument("input", help="Path gambar input (jpg/png/webp)")
    parser.add_argument("output", nargs="?", help="Path output PNG (default: <input>_transparent.png)")
    parser.add_argument("--bbox", type=parse_bbox, metavar="X,Y,W,H",
                        help="Bounding box manual (format: x,y,w,h)")
    parser.add_argument("--iter", type=int, default=5, metavar="N",
                        help="Jumlah iterasi GrabCut (default: 5)")
    parser.add_argument("--padding", type=int, default=20, metavar="P",
                        help="Padding untuk auto bbox (default: 20)")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"❌ Error: File tidak ditemukan: {args.input}")
        sys.exit(1)

    remove_background(
        image_path=args.input,
        output_path=args.output,
        bbox=args.bbox,
        iterations=args.iter,
        padding=args.padding
    )


if __name__ == "__main__":
    main()
