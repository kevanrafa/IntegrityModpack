# 📚 Dokumentasi Lengkap

Panduan lengkap untuk Integrity Modpack Repository dengan API statis dan GitHub Pages hosting.

## 📄 File Dokumentasi

Dokumentasi disediakan dalam beberapa file untuk kemudahan referensi:

| File | Deskripsi |
|------|-----------|
| **README.md** | Dokumentasi lengkap, setup, dan penggunaan |
| **QUICK_START.md** | Guide cepat untuk mulai dalam 5 menit |
| **GITHUB_PAGES_SETUP.md** | Setup GitHub Pages step-by-step |
| **CONFIGURATION.md** | Customize setup untuk repository Anda |
| **DOCUMENTATION.md** | File ini - Index lengkap |

## 🚀 Mulai Cepat (5 Menit)

```bash
# 1. Clone repository
git clone https://github.com/kevanrafa/Integrity-Modpack.git
cd Integrity-Modpack

# 2. Initialize struktur
python manage-modpack.py
# Pilih opsi 1

# 3. Tambah modpack
python manage-modpack.py
# Pilih opsi 2, isi data

# 4. Push & create release
git add api/ changelogs/
git commit -m "Release v1.0.0"
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin main v1.0.0

# 5. Upload .mrpack file ke GitHub Release

# 6. Akses API setelah 2 menit
curl https://kevanrafa.github.io/Integrity-Modpack/api/modpacks.json
```

## 📋 Fitur Utama

### ✅ File Manager Script
- **Python** (`manage-modpack.py`): Cross-platform, interactive menu
- **Bash** (`manage-modpack.sh`): Lightweight, Linux/Mac

### ✅ API Files
- `api/modpacks.json` - Daftar semua modpack
- `api/launcher.json` - Info launcher version
- `api/news.json` - Berita terbaru
- `api/featured.json` - Modpack featured

### ✅ GitHub Actions
- Automatic JSON validation
- GitHub Pages deployment
- Release trigger support

### ✅ Dokumentasi Lengkap
- Setup guide
- Quick start
- Configuration reference
- Troubleshooting

## 📁 Struktur Direktori

```
Integrity-Modpack/
├── api/                          # API files
│   ├── modpacks.json
│   ├── launcher.json
│   ├── news.json
│   └── featured.json
├── icons/                        # Modpack icons
│   └── integrity.png (upload manual)
├── changelogs/                   # Per-modpack changelogs
│   └── integrity-1.0.0.md
├── .github/workflows/
│   └── release-api.yml          # GitHub Actions
├── manage-modpack.py            # Manager script (Python)
├── manage-modpack.sh            # Manager script (Bash)
├── test-api.py                  # Test suite
├── README.md                    # Main documentation
├── QUICK_START.md               # Quick start guide
├── GITHUB_PAGES_SETUP.md        # Pages setup
├── CONFIGURATION.md             # Configuration guide
├── DOCUMENTATION.md             # This file
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore
└── .github/workflows/release-api.yml  # CI/CD
```

## 🛠 Script Features

### manage-modpack.py
```
1. Initialize/Check folder structure
2. Add/Update modpack
3. List modpacks
4. Add to featured
5. Remove from featured
6. Show release guide
7. Exit
```

### manage-modpack.sh
```
1. Initialize folder structure
2. Add new modpack
3. List modpacks
4. Show release guide
5. Exit
```

## 📝 API Endpoints

Setelah GitHub Pages setup:

```
https://kevanrafa.github.io/Integrity-Modpack/api/modpacks.json
https://kevanrafa.github.io/Integrity-Modpack/api/launcher.json
https://kevanrafa.github.io/Integrity-Modpack/api/news.json
https://kevanrafa.github.io/Integrity-Modpack/api/featured.json
```

## 🔄 Workflow Release Lengkap

### 1. Persiapan (10 menit)
- Test modpack lokal
- Siapkan icon PNG
- Buat .mrpack file

### 2. Update Info (2 menit)
```bash
python manage-modpack.py
# Pilih opsi 2, isi data
```

### 3. Edit Changelog (5 menit)
- Edit `changelogs/modpack-version.md`
- Isi features, changes, fixes, dll

### 4. Commit (1 menit)
```bash
git add api/ changelogs/
git commit -m "Release: Modpack v1.0.0"
```

### 5. Create Release (2 menit)
```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin main v1.0.0
```

### 6. Upload .mrpack (2 menit)
- Buka GitHub Releases
- Upload file .mrpack

### 7. Done! (0 menit)
- GitHub Actions auto-deploy
- API updated dalam 2 menit

## ✨ Fitur GitHub Actions

### Automatic Triggers:
- ✅ Push ke `main` dengan changes di `api/` atau `changelogs/`
- ✅ Create/publish release dengan tag v*.*.*
- ✅ Manual trigger via GitHub UI

### Actions:
- ✅ Validate JSON syntax
- ✅ Setup GitHub Pages
- ✅ Deploy to GitHub Pages
- ✅ Verify release format

## 🧪 Testing Setup

### Run Test Suite:
```bash
python test-api.py
```

Output akan menunjukkan:
- ✅ Folder structure check
- ✅ JSON validation
- ✅ Required fields check
- ✅ Data consistency check

## 🐛 Troubleshooting Guide

### Common Issues:

| Issue | Solution |
|-------|----------|
| API tidak accessible | Verify GitHub Pages enabled, tunggu 2 menit |
| JSON validation error | Run `python -m json.tool api/modpacks.json` |
| Script permission denied | `chmod +x manage-modpack.sh` |
| GitHub Actions failed | Check Actions tab, verify JSON syntax |
| Stale content | Hard refresh browser (Ctrl+Shift+R) |

Lihat **Troubleshooting** section di README.md untuk detail lengkap.

## 📚 Contoh Integrasi

### Python Launcher:
```python
import requests

response = requests.get(
    'https://kevanrafa.github.io/Integrity-Modpack/api/modpacks.json'
)
modpacks = response.json()
print(f"Available modpacks: {len(modpacks['modpacks'])}")
```

### JavaScript:
```javascript
fetch('https://kevanrafa.github.io/Integrity-Modpack/api/modpacks.json')
  .then(r => r.json())
  .then(data => console.log(data.modpacks))
```

### CURL:
```bash
curl https://kevanrafa.github.io/Integrity-Modpack/api/modpacks.json | jq
```

## 🎯 Best Practices

### Version Management:
- ✅ Use semantic versioning (v1.0.0)
- ✅ Create git tags untuk setiap release
- ✅ Document changelog lengkap

### API Management:
- ✅ Validate JSON sebelum commit
- ✅ Test API endpoint setelah deploy
- ✅ Monitor GitHub Actions workflow

### Repository:
- ✅ Keep documentation updated
- ✅ Use meaningful commit messages
- ✅ Backup important releases

## 📖 Learning Path

1. **Pemula**: Baca QUICK_START.md
2. **Setup**: Follow GITHUB_PAGES_SETUP.md
3. **Usage**: Refer ke README.md
4. **Advanced**: Check CONFIGURATION.md
5. **Integration**: Use API endpoints

## 🤝 Kontribusi

Untuk improve setup:
1. Fork repository
2. Create feature branch
3. Commit improvements
4. Submit pull request

## 📧 Support

- 📋 Check GitHub Issues
- 📖 Read documentation files
- 💬 Review code comments

## 🎓 Useful Resources

- [GitHub Pages Docs](https://docs.github.com/en/pages)
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [JSON Schema](https://json-schema.org/)
- [Semantic Versioning](https://semver.org/)
- [Markdown Guide](https://www.markdownguide.org/)

## 🔗 Quick Links

| Resource | Link |
|----------|------|
| Repository | https://github.com/kevanrafa/Integrity-Modpack |
| API | https://kevanrafa.github.io/Integrity-Modpack/api/ |
| Releases | https://github.com/kevanrafa/Integrity-Modpack/releases |
| Issues | https://github.com/kevanrafa/Integrity-Modpack/issues |

## 📊 Project Statistics

- **Total Files**: 8 main files
- **Scripts**: 2 (Python + Bash)
- **Documentation**: 5 guides
- **API Endpoints**: 4
- **GitHub Actions**: 1 workflow

## 🎉 Next Steps

1. **Setup**: Follow QUICK_START.md
2. **Test**: Run `python test-api.py`
3. **Deploy**: Push ke GitHub & create release
4. **Monitor**: Check GitHub Pages status
5. **Integrate**: Use API di aplikasi Anda

---

**Last Updated:** 2024-01-15

**Maintained by:** Integrity Modpack Team

Untuk pertanyaan atau suggestions, buka GitHub Issues!
