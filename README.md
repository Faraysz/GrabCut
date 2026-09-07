<div align="center">

  <!-- Tech Stack Badges -->
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/rembg-FF6F61?style=for-the-badge&logo=python&logoColor=white" alt="rembg">
  <img src="https://img.shields.io/badge/ONNX%20Runtime-005CED?style=for-the-badge&logo=onnx&logoColor=white" alt="ONNX Runtime">

  <br><br>

  <!-- Project Title -->
  <h1>✂️ GrabCut Background Remover</h1>

  <p><strong>Tool CLI Python Cepat & Ringan untuk Menghapus Background Gambar</strong></p>

  <p>
    <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=flat-square">
    <img src="https://img.shields.io/badge/Status-Stable-green?style=flat-square">
    <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square">
  </p>

</div>

---

## 🚀 Tentang Project

**GrabCut Background Remover** adalah koleksi tool CLI Python untuk menghapus background gambar secara otomatis. Tersedia **tiga metode** yang bisa dipilih sesuai kebutuhan: AI-powered dengan model ringan, AI dengan model default, atau klasik computer vision menggunakan OpenCV GrabCut.

Cocok untuk:
- 🖼️ Editing foto produk e-commerce
- 🎨 Desain grafis & digital art
- 📸 Fotografi & portrait editing
- 🤖 Preprocessing dataset machine learning

---

## ✨ Fitur Utama

| Fitur | Deskripsi |
|-------|-----------|
| 🤖 **AI-Powered (u2net)** | Model ringan ~176MB, hasil presisi tinggi, cocok untuk objek kompleks |
| 🤖 **AI-Powered (default)** | Model rembg default, otomatis download, hasil optimal |
| 🎯 **OpenCV GrabCut** | Metode klasik tanpa download model, auto-detect bounding box |
| 📦 **Auto Bounding Box** | Deteksi area foreground otomatis via edge detection & contour |
| 🖱️ **Interaktif CLI** | Support argumen command-line + prompt terminal |
| 💾 **Output Otomatis** | Simpan hasil sebagai `[nama]_nobg.png` atau `[nama]_transparent.png` |
| ⚡ **Cepat & Ringan** | Minimal dependencies, tidak perlu GPU |

---

## 🛠️ Tech Stack

| Layer | Teknologi |
|-------|-----------|
| **Language** | Python 3.8+ |
| **AI Engine** | rembg (u2net / bria-rmbg) |
| **Computer Vision** | OpenCV (GrabCut algorithm) |
| **ML Runtime** | ONNX Runtime |
| **Image Processing** | Pillow, NumPy |

---

## 📂 Struktur File

```
GrabCut/
├── 📄 removee.py                 # 🤖 AI Simple - rembg default
├── 📄 bg_remover_simple.py       # 🤖 AI Ringan - paksa u2net (~176MB)
├── 📄 grabcut_bg.py              # 🎯 OpenCV GrabCut + auto bbox
├── 📁 demo/
│   ├── demo_test.jpg             # Gambar demo
│   ├── vario.jpg                 # Gambar demo
│   ├── hasil.png                 # Hasil contoh
│   ├── test_nobg.png             # Hasil contoh
│   └── vario_nobg.png            # Hasil contoh
└── README.md
```

---

## ⚙️ Cara Kerja

### Metode 1: AI-Powered (rembg)
```
┌─────────────┐     ┌─────────────────┐     ┌─────────────┐
│  🖼️ Input   │────▶│  AI Model       │────▶│ 🖼️ Output   │
│   Gambar    │     │  (u2net/bria)   │     │  PNG Alpha  │
└─────────────┘     └─────────────────┘     └─────────────┘
```

### Metode 2: OpenCV GrabCut
```
┌─────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────┐
│  🖼️ Input   │────▶│ Auto BBox       │────▶│ GrabCut         │────▶│ 🖼️ Output   │
│   Gambar    │     │ (Edge+Contour)  │     │ (5 iterasi)     │     │  PNG Alpha  │
└─────────────┘     └─────────────────┘     └─────────────────┘     └─────────────┘
```

---

## 🚀 Cara Install

### Prerequisites
- Python 3.8+
- pip

### 1. Clone Repository
```bash
git clone https://github.com/Faraysz/GrabCut.git
cd GrabCut
```

### 2. Install Dependencies

**Untuk AI (rembg):**
```bash
pip install rembg onnxruntime pillow --break-system-packages
```

**Untuk OpenCV GrabCut:**
```bash
pip install opencv-python numpy
```

**Semua sekaligus:**
```bash
pip install rembg onnxruntime pillow opencv-python numpy --break-system-packages
```

> 💡 **Catatan:** Model `u2net` (~176MB) akan otomatis didownload saat pertama kali menjalankan script AI.

---

## 📖 Cara Penggunaan

### 🤖 Metode 1: AI Simple (rembg default)
```bash
# Interaktif (diminta nama file)
python removee.py

# Langsung dengan argumen
python removee.py foto.jpg
```

### 🤖 Metode 2: AI Ringan (u2net, ~176MB)
```bash
# Interaktif
python bg_remover_simple.py

# Langsung dengan argumen
python bg_remover_simple.py foto.jpg
```

### 🎯 Metode 3: OpenCV GrabCut
```bash
# Auto detect bounding box
python grabcut_bg.py foto.jpg

# Output custom
python grabcut_bg.py foto.jpg hasil.png

# Bounding box manual
python grabcut_bg.py foto.jpg --bbox 100,50,300,400

# Iterasi lebih banyak (lebih rapi)
python grabcut_bg.py foto.jpg --iter 10

# Padding auto bbox lebih besar
python grabcut_bg.py foto.jpg --padding 30
```

---

## 📋 Perbandingan Metode

| Aspek | `removee.py` | `bg_remover_simple.py` | `grabcut_bg.py` |
|-------|-------------|------------------------|-----------------|
| **Metode** | AI (rembg default) | AI (u2net) | OpenCV GrabCut |
| **Download Model** | Otomatis (~1GB) | Otomatis (~176MB) | Tidak perlu |
| **Kualitas** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Kecepatan** | Sedang | Cepat | Sangat Cepat |
| **Offline** | ❌ (pertama kali) | ❌ (pertama kali) | ✅ Full offline |
| **Kompleksitas Objek** | Sangat baik | Sangat baik | Cukup baik |
| **Cocok untuk** | Semua gambar | Semua gambar | Objek jelas, cepat |

---

## 📸 Demo

| Input | Output AI | Output GrabCut |
|-------|-----------|----------------|
| `demo_test.jpg` | `test_nobg.png` | `hasil.png` |
| `vario.jpg` | `vario_nobg.png` | — |

> Lihat folder repo untuk contoh hasil!

---

## 🤝 Kontribusi

Kontribusi sangat diterima! Silakan:
1. Fork repository ini
2. Buat branch fitur (`git checkout -b fitur-anda`)
3. Commit perubahan (`git commit -m 'Tambah fitur X'`)
4. Push ke branch (`git push origin fitur-anda`)
5. Buat Pull Request

---

## 📄 Lisensi

Project ini dilisensikan di bawah [MIT License](LICENSE).

---

<div align="center">
  <sub>Dibuat dengan ❤️ oleh <a href="https://github.com/Faraysz">@Faraysz</a></sub>
</div>
