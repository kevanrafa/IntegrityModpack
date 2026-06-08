# ⚙️ Configuration Guide

Panduan untuk customize setup ke repository Anda sendiri.

## 1. Update GitHub Username & Repository Name

Edit file yang berikut dengan username dan repository Anda:

### 1a. manage-modpack.py

Di baris 15-17, ganti dengan info Anda:

```python
self.username = "kevanrafa"        # ← Ganti dengan GitHub username Anda
self.repo_name = "Integrity-Modpack"  # ← Ganti dengan nama repo
```

Contoh untuk repository lain:
```python
self.username = "mybUsername"
self.repo_name = "my-modpack"
```

### 1b. manage-modpack.sh

Di baris 10-11, ganti dengan info Anda:

```bash
USERNAME="kevanrafa"          # ← Ganti
REPO_NAME="Integrity-Modpack" # ← Ganti
```

### 1c. GITHUB_PAGES_SETUP.md

Replace semua referensi dengan info Anda:
- `kevanrafa` → your username
- `Integrity-Modpack` → your repo name

Contoh:
```
# Replace:
https://github.com/kevanrafa/Integrity-Modpack

# Dengan:
https://github.com/yourUsername/your-repo-name
```

### 1d. README.md

Replace di section README bagian setup GitHub Pages.

---

## 2. Custom Repository Setup dari Awal

Jika ingin setup di repository baru:

### Step 1: Fork atau Create Repository
```bash
# Option A: Clone dan setup di existing repo
git clone https://github.com/kevanrafa/Integrity-Modpack.git my-modpack
cd my-modpack
git remote set-url origin https://github.com/yourUsername/my-modpack.git

# Option B: Copy files ke repo baru Anda
```

### Step 2: Update Configuration Files
Ganti username dan repo name di:
- `manage-modpack.py`
- `manage-modpack.sh`
- Documentation files

### Step 3: Push & Setup GitHub Pages
```bash
git add .
git commit -m "Initial commit: Modpack API setup"
git push origin main

# Setup GitHub Pages (lihat GITHUB_PAGES_SETUP.md)
```

---

## 3. Customize JSON Templates

### 3a. Ubah launcher.json

Edit `api/launcher.json` untuk info launcher Anda:

```json
{
  "latest": "1.2.0",
  "minimum": "1.0.0",
  "maintenance": false
}
```

Fields:
- `latest`: Versi launcher terbaru
- `minimum`: Versi minimum yang support
- `maintenance`: Set `true` jika sedang maintenance

### 3b. Ubah news.json

Edit `api/news.json` untuk berita Anda:

```json
{
  "news": [
    {
      "title": "Your News Title",
      "content": "News content here",
      "timestamp": "2024-01-15T00:00:00Z"
    }
  ]
}
```

### 3c. Default featured list

Edit `api/featured.json` untuk featured modpack default:

```json
{
  "featured": ["modpack_id_1", "modpack_id_2"]
}
```

---

## 4. Customize Script Prompts

### Python Script (manage-modpack.py)

Untuk mengubah prompt atau behavior:

Contoh - Ubah prompt text (line 60):
```python
# Before:
modpack_id = self._input("Modpack ID (e.g., 'integrity'): ").strip()

# After:
modpack_id = self._input("Enter modpack ID: ").strip()
```

### Bash Script (manage-modpack.sh)

Ubah prompt text (line 49):
```bash
# Before:
read -p "Modpack ID (e.g., 'integrity'): " MODPACK_ID

# After:
read -p "Enter modpack ID: " MODPACK_ID
```

---

## 5. Add Custom Metadata

### Add Fields ke modpacks.json

Edit script untuk add custom fields:

**Python (manage-modpack.py, line 96-104):**

```python
# Tambah sebelum new_modpack = {...}
author = self._input("Author name: ").strip()
website = self._input("Project website: ").strip()

# Tambah di dalam new_modpack object:
new_modpack = {
    # ... existing fields ...
    "author": author,
    "website": website
}
```

**Bash (manage-modpack.sh, line 39-40):**

```bash
read -p "Author name: " AUTHOR
read -p "Project website: " WEBSITE

# Update Python section dengan:
"author": "$AUTHOR",
"website": "$WEBSITE"
```

---

## 6. Change GitHub Actions Trigger

Edit `.github/workflows/release-api.yml` untuk custom trigger:

### Trigger hanya pada release:
```yaml
on:
  release:
    types: [published, created]
```

### Trigger pada push ke specific branch:
```yaml
on:
  push:
    branches:
      - main
      - develop
```

### Trigger scheduled (daily):
```yaml
on:
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight
```

---

## 7. Environment Variables

Jika ingin setup CI/CD lebih kompleks:

### Add secrets di GitHub:
1. Repository → Settings → Secrets and variables → Actions
2. New repository secret
3. Name: `GITHUB_TOKEN` (auto-generated)

### Use dalam workflow:
```yaml
env:
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

---

## 8. Multi-Language Support

Untuk support multiple languages di API:

### Update modpacks.json structure:
```json
{
  "id": "integrity",
  "name": "Integrity",
  "description": "Official Integrity Modpack",
  "translations": {
    "id": "Integritas",
    "en": "Integrity",
    "fr": "Intégrité",
    "es": "Integridad"
  }
}
```

### Update news.json:
```json
{
  "news": [
    {
      "title": "Release",
      "content": "English content",
      "translations": {
        "id": "Indonesian content",
        "fr": "French content"
      }
    }
  ]
}
```

---

## 9. Performance Optimization

### Minimize JSON files:
```bash
python -c "
import json

# Load and minify
with open('api/modpacks.json') as f:
    data = json.load(f)

with open('api/modpacks.json', 'w') as f:
    json.dump(data, f, separators=(',', ':'))
"
```

### Compress files (optional):
```bash
gzip -k api/modpacks.json
```

---

## 10. Backup & Recovery

### Backup configuration:
```bash
# Backup semua files penting
git tag -a backup-v1.0.0 -m "Backup before changes"
git push origin backup-v1.0.0
```

### Recovery:
```bash
git checkout backup-v1.0.0
```

---

## Checklist Kustomisasi

- [ ] Update USERNAME & REPO_NAME di scripts
- [ ] Customize JSON templates (launcher.json, news.json)
- [ ] Update GitHub Pages URL di dokumentasi
- [ ] Test dengan `python test-api.py`
- [ ] Push ke repository Anda
- [ ] Setup GitHub Pages (GITHUB_PAGES_SETUP.md)
- [ ] Add custom metadata fields jika diperlukan
- [ ] Create first release dengan tag v1.0.0

---

## ❓ FAQ Kustomisasi

**Q: Bisa ganti server hosting selain GitHub Pages?**
A: Ya, copy file dari `api/` ke web server Anda (Apache, Nginx, etc.)

**Q: Support API versioning?**
A: Ya, ubah `api_version` di modpacks.json jika ada breaking changes

**Q: Bisa deploy ke multiple CDN?**
A: Ya, setup GitHub Actions untuk deploy ke multiple platforms

---

**Customization Complete! 🎉**

Sekarang repo Anda siap dengan API setup yang custom.
