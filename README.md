<div align="center">

# ✂️ GrabCut Background Remover

**A powerful, lightweight Python CLI tool for removing image backgrounds using OpenCV GrabCut & AI (rembg/u2net)**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=opencv&logoColor=white)](https://opencv.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## 🎯 What is GrabCut Background Remover?

GrabCut Background Remover is a **versatile Python CLI tool** that offers two distinct approaches to remove image backgrounds: 
1. **AI-Powered**: Utilizes the lightweight `u2net` model (~176MB) via `rembg` for fast, high-quality, and hassle-free results.
2. **Classic Computer Vision**: Leverages OpenCV's GrabCut algorithm with an **auto-detect bounding box** feature (based on edge detection and contours) for environments where AI models are not preferred.

> ⚠️ **Note:** The first time you run the AI method, it will automatically download the `u2net` model (~176MB). Ensure you have a stable internet connection.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🧠 **AI-Powered (u2net)** | High-quality background removal using a lightweight, optimized model |
| 📐 **Classic GrabCut** | OpenCV-based removal with smart auto-detect bounding box |
| ⚡ **Zero-Config Output** | Automatically saves results as `[filename]_nobg.png` or `_transparent.png` |
| 💻 **Interactive CLI** | Supports both direct command-line arguments and interactive terminal prompts |
| 🚀 **Fast & Lightweight** | Minimal dependencies, designed for speed and low resource consumption |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git installed
- Basic knowledge of terminal/command prompt

### Installation

```bash
# Clone this repository
git clone https://github.com/Faraysz/GrabCut.git
cd GrabCut

# Install dependencies
pip install rembg onnxruntime pillow opencv-python numpy
