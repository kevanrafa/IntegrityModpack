# 🔧 GitHub Pages Setup Guide

Panduan lengkap untuk setup GitHub Pages agar API dapat diakses secara publik.

## Step 1: Enable GitHub Pages

### Via GitHub Web UI:
1. Buka repository: https://github.com/kevanrafa/Integrity-Modpack
2. Klik **Settings** (gear icon)
3. Di sidebar kiri, klik **Pages**
4. Pilih:
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Directory**: `/ (root)`
5. Klik **Save**

### Screenshot lokasi:
```
Repository Settings
└── Pages (di sidebar kiri)
    └── Source: Deploy from a branch
        └── Branch: main / (root)
```

## Step 2: Tunggu Deployment

- GitHub Actions akan otomatis trigger
- Cek status di **Actions** tab
- Workflow: `Deploy API to GitHub Pages`
- Tunggu hingga status ✅ (hijau)
- Biasanya selesai dalam 1-2 menit

## Step 3: Verify GitHub Pages

Setelah deployment selesai, API siap diakses:

```
https://kevanrafa.github.io/Integrity-Modpack/
```

### Test Setiap Endpoint:

**modpacks.json:**
```
https://kevanrafa.github.io/Integrity-Modpack/api/modpacks.json
```

**launcher.json:**
```
https://kevanrafa.github.io/Integrity-Modpack/api/launcher.json
```

**news.json:**
```
https://kevanrafa.github.io/Integrity-Modpack/api/news.json
```

**featured.json:**
```
https://kevanrafa.github.io/Integrity-Modpack/api/featured.json
```

## Step 4: Custom Domain (Optional)

Jika ingin menggunakan custom domain (cth: api.integrity.com):

### 4a. Beli domain
- GoDaddy, Namecheap, atau provider lain
- Gunakan domain apapun

### 4b. Setup DNS
Di provider domain, tambah **CNAME record**:
- **Name**: api
- **Type**: CNAME
- **Value**: kevanrafa.github.io

### 4c. Setup di GitHub
1. Repository Settings → Pages
2. Di **Custom domain**, masukkan: `api.integrity.com`
3. Centang **Enforce HTTPS**
4. Klik **Save**

### 4d. Verify
Tunggu beberapa menit, kemudian akses:
```
https://api.integrity.com/modpacks.json
```

## Step 5: Automated Workflow

Setiap kali ada **push** atau **release** ke repo, GitHub Actions otomatis:

1. ✅ Validate JSON files
2. 📦 Build GitHub Pages artifact
3. 🚀 Deploy ke GitHub Pages
4. 🌐 Update API endpoints

### Trigger Points:
- Push ke `main` dengan changes di `api/` atau `changelogs/`
- Create/publish release
- Manual trigger (Actions tab)

## 📋 Checklist GitHub Pages Setup

- [ ] Repository accessible (public)
- [ ] Buka Settings → Pages
- [ ] Source set ke `main` branch, `/ (root)` directory
- [ ] Save dan tunggu deployment (~2 menit)
- [ ] Cek status di Actions tab
- [ ] Test modpacks.json endpoint
- [ ] Semua JSON endpoints accessible

## 🐛 Troubleshooting

### API tidak accessible

**Problem:** 404 Not Found ketika akses API
**Solution:**
- Verify GitHub Pages enabled di Settings → Pages
- Check branch adalah `main`
- Verify directory adalah `/ (root)`
- Tunggu 2-3 menit setelah setup
- Hard refresh browser (Ctrl+Shift+R atau Cmd+Shift+R)

### Deployment failed di GitHub Actions

**Problem:** Red ❌ status di Actions
**Solution:**
- Klik workflow untuk lihat error
- Common issues:
  - JSON syntax error: `python -m json.tool api/modpacks.json`
  - Missing required fields
  - Encoding bukan UTF-8

### Stale content

**Problem:** API menunjukkan data lama
**Solution:**
- Browser cache: Hard refresh (Ctrl+Shift+R)
- CDN cache: Tunggu 5-10 menit atau clear cache manually
- Verify latest push deployed: check Actions status

## 📊 Monitor Deployment

### Via GitHub Web UI:
1. Repository → **Actions** tab
2. Klik workflow: **Deploy API to GitHub Pages**
3. Lihat history executions:
   - ✅ Green = Success
   - 🔴 Red = Failed
   - ⏳ Yellow = Running

### Via CLI:
```bash
# Check recent pushes
git log --oneline -10

# Check git tags (releases)
git tag -l

# Local test dengan Python server
python -m http.server 8000
# Akses: http://localhost:8000/api/
```

## 🚀 Next Steps

Setelah GitHub Pages setup:

1. **Add Modpack:**
   ```bash
   python manage-modpack.py
   # Pilih 2 (Add/Update modpack)
   ```

2. **Test API:**
   ```bash
   curl https://kevanrafa.github.io/Integrity-Modpack/api/modpacks.json
   ```

3. **Create Release:**
   ```bash
   git tag -a v1.0.0 -m "Release v1.0.0"
   git push origin v1.0.0
   ```

## 📚 Resource Links

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Configuring custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)

---

**GitHub Pages Setup Complete! 🎉**

Sekarang API Anda accessible via GitHub Pages.
