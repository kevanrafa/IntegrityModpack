# Integrity Modpack

Repository resmi untuk Integrity Modpack dengan API statis dan GitHub Pages hosting.

## 📋 Struktur Direktori

```
Integrity-Modpack/
├── api/
│   ├── modpacks.json      # Daftar semua modpack
│   ├── launcher.json      # Info launcher
│   ├── news.json          # Berita terbaru
│   └── featured.json      # Modpack featured
├── icons/                 # Icon modpack (PNG)
├── changelogs/            # Changelog per modpack
├── .github/workflows/     # GitHub Actions
│   └── release-api.yml
├── manage-modpack.py      # Script manager (Python)
├── manage-modpack.sh      # Script manager (Bash)
└── README.md
```

## 🚀 Setup Awal

### 1. Clone Repository
```bash
git clone https://github.com/kevanrafa/Integrity-Modpack.git
cd Integrity-Modpack
```

### 2. Inisialisasi Struktur
#### Menggunakan Python:
```bash
python manage-modpack.py
# Pilih opsi 1 untuk initialize
```

#### Menggunakan Bash:
```bash
chmod +x manage-modpack.sh
./manage-modpack.sh
# Pilih opsi 1 untuk initialize
```

### 3. Konfigurasi GitHub Pages
- Buka **Settings** → **Pages**
- Pilih **Branch: main** → **Directory: / (root)**
- GitHub Pages akan otomatis deploy setiap kali ada push

## 📦 Menambah Modpack Baru

### Menggunakan Python Script (Windows, Mac, Linux):
```bash
python manage-modpack.py
```

Menu interaktif:
```
1. Initialize/Check folder structure
2. Add/Update modpack
3. List modpacks
4. Add to featured
5. Remove from featured
6. Show release guide
7. Exit
```

**Pilih opsi 2** dan ikuti prompt:
- **Modpack ID**: identifier unik (cth: `integrity`)
- **Name**: nama tampilan (cth: `Integrity`)
- **Version**: versi semantic (cth: `1.0.0`)
- **Minecraft**: versi Minecraft (cth: `1.21.1`)
- **Loader**: `fabric`, `forge`, atau `quilt`
- **Description**: deskripsi singkat
- **Icon filename**: nama file icon PNG (disimpan di `icons/`)

Script akan otomatis:
- Membuat file changelog kosong di `changelogs/`
- Update `modpacks.json` dengan info modpack baru
- Menanya apakah ingin tambah ke featured modpacks

### Menggunakan Bash Script (Mac, Linux):
```bash
./manage-modpack.sh
```

Pilih opsi 2 untuk add modpack.

## 📝 File API Struktur

### `api/modpacks.json`
```json
{
  "api_version": 1,
  "modpacks": [
    {
      "id": "integrity",
      "name": "Integrity",
      "version": "1.0.0",
      "minecraft": "1.21.1",
      "loader": "fabric",
      "description": "Official Integrity Modpack",
      "icon": "https://raw.githubusercontent.com/kevanrafa/Integrity-Modpack/main/icons/integrity.png",
      "download": "https://github.com/kevanrafa/Integrity-Modpack/releases/download/v1.0.0/integrity.mrpack",
      "changelog": "https://raw.githubusercontent.com/kevanrafa/Integrity-Modpack/main/changelogs/integrity-1.0.0.md"
    }
  ]
}
```

### `api/launcher.json`
```json
{
  "latest": "1.2.0",
  "minimum": "1.0.0",
  "maintenance": false
}
```

### `api/news.json`
```json
{
  "news": [
    {
      "title": "Integrity Launcher Released",
      "content": "Initial public version.",
      "timestamp": "2024-01-15T00:00:00Z"
    }
  ]
}
```

### `api/featured.json`
```json
{
  "featured": ["integrity", "axixnull"]
}
```

## 🔄 Workflow Release

### 1. Persiapan
```bash
# Edit modpack di folder local
# Test modpack

# Jalankan script untuk update info
python manage-modpack.py
# Pilih opsi 2 (Add/Update modpack)
```

### 2. Edit Changelog
Edit file di `changelogs/` dengan detail perubahan:
- New Features
- Changes
- Fixes
- Removed
- Known Issues

### 3. Commit Changes
```bash
git add api/ changelogs/
git commit -m "Release: Integrity v1.0.0 - Initial release"
git push origin main
```

### 4. Buat GitHub Release
```bash
# Buat tag
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0

# Atau via GitHub UI:
# 1. Buka Releases
# 2. Create new release
# 3. Tag: v1.0.0
# 4. Upload .mrpack file
```

### 5. Upload .mrpack File
- Buka https://github.com/kevanrafa/Integrity-Modpack/releases
- Edit release v1.0.0
- Upload file `integrity.mrpack`

### 6. GitHub Actions Deployment
Workflow `release-api.yml` otomatis:
- Trigger saat push ke `main` dengan changes di `api/` atau `changelogs/`
- Trigger saat ada release baru
- Validate semua JSON files
- Deploy ke GitHub Pages

## 🌐 Akses API

API tersedia di GitHub Pages setelah deployment:

```
https://kevanrafa.github.io/Integrity-Modpack/api/modpacks.json
https://kevanrafa.github.io/Integrity-Modpack/api/launcher.json
https://kevanrafa.github.io/Integrity-Modpack/api/news.json
https://kevanrafa.github.io/Integrity-Modpack/api/featured.json
```

### Contoh Integration dengan Launcher:
```python
import requests

# Ambil semua modpacks
response = requests.get(
    'https://kevanrafa.github.io/Integrity-Modpack/api/modpacks.json'
)
modpacks = response.json()

# Ambil featured modpacks
featured_response = requests.get(
    'https://kevanrafa.github.io/Integrity-Modpack/api/featured.json'
)
featured = featured_response.json()
```

## 🛠 GitHub Actions Workflow

File: `.github/workflows/release-api.yml`

**Triggers:**
- Push ke branch `main` dengan changes di:
  - `api/`
  - `changelogs/`
  - `.github/workflows/release-api.yml`
- Release baru dibuat
- Manual trigger via GitHub UI

**Actions:**
1. Checkout code
2. Setup Python environment
3. Validate semua JSON files dengan `json.tool`
4. Setup GitHub Pages
5. Upload artifact
6. Deploy ke GitHub Pages

## 📋 Daftar Fitur Script

### manage-modpack.py (Python)
✅ Cross-platform (Windows, Mac, Linux)
✅ Menu interaktif
✅ Input validation
✅ JSON formatting otomatis
✅ Changelog creation
✅ Featured management
✅ Release guide

### manage-modpack.sh (Bash)
✅ Mac, Linux
✅ Simple & lightweight
✅ POSIX compatible
✅ Color output
✅ Integration dengan Python untuk JSON handling

## 🐛 Troubleshooting

### JSON validation error di GitHub Actions
- Check syntax JSON files dengan: `python -m json.tool api/modpacks.json`
- Ensure UTF-8 encoding

### API tidak tersedia di GitHub Pages
- Verify branch main dipilih di Pages settings
- Check workflow status di Actions tab
- Ensure file berada di root atau api/ folder

### Script permission denied (Bash)
```bash
chmod +x manage-modpack.sh
```

### Python not found
Ensure Python 3.6+ installed:
```bash
python --version
# atau
python3 --version
```

## 📖 Contoh Penggunaan Lengkap

```bash
# 1. Setup awal
python manage-modpack.py
# -> Pilih 1

# 2. Tambah modpack baru
python manage-modpack.py
# -> Pilih 2
# -> Input: integrity, Integrity, 1.0.0, 1.21.1, fabric, "Official Integrity", integrity.png

# 3. Edit changelog di changelogs/integrity-1.0.0.md

# 4. Commit
git add api/ changelogs/
git commit -m "Release: Integrity v1.0.0"
git push origin main

# 5. Create release
git tag -a v1.0.0 -m "v1.0.0"
git push origin v1.0.0

# 6. Upload .mrpack file via GitHub UI

# 7. Verify API (tunggu beberapa detik)
curl https://kevanrafa.github.io/Integrity-Modpack/api/modpacks.json
```

## 📄 Lisensi

MIT License - Silakan modifikasi sesuai kebutuhan

## 🤝 Kontribusi

Untuk menambah modpack baru atau fix, silakan:
1. Fork repository
2. Create branch baru
3. Commit changes
4. Push dan buat Pull Request

## 📧 Support

Untuk pertanyaan atau issue, buka GitHub Issues pada repository ini.

---

**Repository:** https://github.com/kevanrafa/Integrity-Modpack

**API Endpoint:** https://kevanrafa.github.io/Integrity-Modpack/api/

**Last Updated:** 2024-01-15
