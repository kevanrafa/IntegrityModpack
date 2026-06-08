# 🚀 Quick Start Guide

Panduan cepat untuk mulai menggunakan Integrity Modpack Manager.

## ⚡ Instalasi 1 Menit

### 1. Clone Repository
```bash
git clone https://github.com/kevanrafa/Integrity-Modpack.git
cd Integrity-Modpack
```

### 2. Jalankan Script Manager (Pilih Salah Satu)

**Windows/Mac/Linux (Python):**
```bash
python manage-modpack.py
```

**Mac/Linux (Bash):**
```bash
chmod +x manage-modpack.sh
./manage-modpack.sh
```

### 3. Pilih Opsi 1: Initialize
Script akan membuat folder dan file yang diperlukan.

---

## 📦 Tambah Modpack dalam 2 Menit

### Langkah 1: Jalankan Script
```bash
python manage-modpack.py
```

### Langkah 2: Pilih Opsi 2 (Add/Update modpack)

### Langkah 3: Isi Data
```
Modpack ID: integrity
Modpack Name: Integrity
Version: 1.0.0
Minecraft Version: 1.21.1
Loader: fabric
Description: Official Integrity Modpack
Icon filename: integrity.png
```

### Langkah 4: Jawab (y) untuk Featured
```
Add to featured modpacks? (y/n): y
```

✅ Modpack berhasil ditambahkan!

---

## 🔄 Release dalam 5 Menit

### 1. Persiapkan File
```bash
# Copy .mrpack file ke local folder
# Test modpack lokal
```

### 2. Update Info
```bash
python manage-modpack.py
# Pilih 2, update modpack
```

### 3. Edit Changelog
Buka `changelogs/integrity-1.0.0.md` dan update dengan detail:
- ✨ New Features
- 🔄 Changes
- 🐛 Fixes
- ❌ Removed
- ⚠️ Known Issues

### 4. Push ke GitHub
```bash
git add api/ changelogs/
git commit -m "Release: Integrity v1.0.0"
git push origin main
```

### 5. Create GitHub Release
```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

### 6. Upload .mrpack
1. Buka: https://github.com/kevanrafa/Integrity-Modpack/releases
2. Edit release v1.0.0
3. Upload file `integrity.mrpack`

### 7. Done! ✅
GitHub Actions akan otomatis deploy API ke GitHub Pages.

---

## 🌐 Akses API

Setelah deployment selesai (tunggu ~2 menit), API siap digunakan:

```
https://kevanrafa.github.io/Integrity-Modpack/api/modpacks.json
```

### Test dengan cURL
```bash
curl https://kevanrafa.github.io/Integrity-Modpack/api/modpacks.json
```

### Test dengan Python
```python
import requests
response = requests.get(
    'https://kevanrafa.github.io/Integrity-Modpack/api/modpacks.json'
)
print(response.json())
```

---

## 📁 File Structure Quick Ref

```
project/
├── api/                           # API files (auto-deployed)
│   ├── modpacks.json             # ← Diupdate oleh script
│   ├── launcher.json
│   ├── news.json
│   └── featured.json
├── changelogs/                    # Changelog per release
│   └── integrity-1.0.0.md        # ← Edit di sini sebelum release
├── icons/                         # Icon files
│   └── integrity.png             # ← Upload icon di sini
├── manage-modpack.py             # Run: python manage-modpack.py
├── manage-modpack.sh             # Run: ./manage-modpack.sh
└── README.md                      # Dokumentasi lengkap
```

---

## ❓ Pertanyaan Umum

**Q: Berapa lama API di-deploy?**
A: ~1-2 menit setelah push/release

**Q: Bagaimana cara test API lokal?**
A: Gunakan `python -m http.server` di root folder, akses `http://localhost:8000/api/`

**Q: Format file .mrpack apa?**
A: ZIP file dengan structure spesifik (buat menggunakan Modrinth atau launcher lain)

**Q: Bisa multiple modpacks?**
A: Ya! Script support unlimited modpack. Setiap modpack punya unique ID.

**Q: GitHub Pages tidak update?**
A: Check Actions tab, lihat workflow status

---

## 🎯 Checklist Pre-Release

- [ ] Test modpack di Minecraft client
- [ ] Update versi di script (version field)
- [ ] Edit changelog dengan detail lengkap
- [ ] Pastikan icon file ada di `icons/`
- [ ] Verify JSON syntax: `python -m json.tool api/modpacks.json`
- [ ] Commit dan push changes
- [ ] Create git tag dengan format `v*.*.* `
- [ ] Upload .mrpack file ke release
- [ ] Test API endpoint setelah 2 menit

---

## 📞 Need Help?

1. Baca [README.md](README.md) untuk dokumentasi lengkap
2. Check [GitHub Issues](https://github.com/kevanrafa/Integrity-Modpack/issues)
3. Review script code dengan comments

---

**Happy Modpacking! 🎮**
