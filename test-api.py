#!/usr/bin/env python3
"""
Test script untuk verify Integrity Modpack API setup
Jalankan: python test-api.py
"""

import json
import sys
from pathlib import Path

def validate_json_file(filepath, description):
    """Validate JSON file exists dan punya syntax yang benar."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"✅ {description}: Valid")
        return data
    except FileNotFoundError:
        print(f"❌ {description}: File not found - {filepath}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ {description}: Invalid JSON - {e}")
        return None

def validate_modpacks(modpacks_data):
    """Validate modpacks.json structure."""
    if not modpacks_data:
        return False
    
    issues = []
    
    if "api_version" not in modpacks_data:
        issues.append("Missing 'api_version'")
    
    if "modpacks" not in modpacks_data:
        issues.append("Missing 'modpacks' array")
        return False
    
    modpacks = modpacks_data["modpacks"]
    if not isinstance(modpacks, list):
        issues.append("'modpacks' is not an array")
        return False
    
    required_fields = ["id", "name", "version", "minecraft", "loader", 
                       "description", "icon", "download", "changelog"]
    
    for i, mp in enumerate(modpacks):
        for field in required_fields:
            if field not in mp:
                issues.append(f"Modpack {i} ({mp.get('id', 'unknown')}): Missing '{field}'")
    
    if issues:
        print("\n⚠️ Modpacks Issues:")
        for issue in issues:
            print(f"   - {issue}")
        return False
    
    print(f"   • Modpacks found: {len(modpacks)}")
    for mp in modpacks:
        print(f"   • {mp['name']} (v{mp['version']}, {mp['loader']})")
    
    return True

def validate_launcher(launcher_data):
    """Validate launcher.json structure."""
    if not launcher_data:
        return False
    
    required = ["latest", "minimum", "maintenance"]
    missing = [f for f in required if f not in launcher_data]
    
    if missing:
        print(f"⚠️ Launcher Issues: Missing {missing}")
        return False
    
    print(f"   • Latest: {launcher_data['latest']}")
    print(f"   • Minimum: {launcher_data['minimum']}")
    print(f"   • Maintenance: {launcher_data['maintenance']}")
    
    return True

def validate_news(news_data):
    """Validate news.json structure."""
    if not news_data:
        return False
    
    if "news" not in news_data:
        print("⚠️ News Issues: Missing 'news' array")
        return False
    
    news_items = news_data["news"]
    if not isinstance(news_items, list):
        print("⚠️ News Issues: 'news' is not an array")
        return False
    
    print(f"   • News items: {len(news_items)}")
    for i, item in enumerate(news_items[:3]):  # Show first 3
        print(f"   • {item.get('title', f'News {i}')}")
    
    return True

def validate_featured(featured_data):
    """Validate featured.json structure."""
    if not featured_data:
        return False
    
    if "featured" not in featured_data:
        print("⚠️ Featured Issues: Missing 'featured' array")
        return False
    
    featured_list = featured_data["featured"]
    if not isinstance(featured_list, list):
        print("⚠️ Featured Issues: 'featured' is not an array")
        return False
    
    print(f"   • Featured modpacks: {featured_list if featured_list else 'None'}")
    
    return True

def check_folders():
    """Check if folder structure exists."""
    root = Path(__file__).parent
    folders = ["api", "icons", "changelogs"]
    
    print("\n📁 Folder Structure:")
    all_ok = True
    for folder in folders:
        path = root / folder
        if path.exists():
            print(f"✅ {folder}/")
        else:
            print(f"❌ {folder}/ - Not found")
            all_ok = False
    
    return all_ok

def main():
    """Main test function."""
    print("="*60)
    print("🧪 INTEGRITY MODPACK API - TEST SUITE")
    print("="*60)
    
    root = Path(__file__).parent
    
    # Check folders
    folders_ok = check_folders()
    
    # Validate JSON files
    print("\n📄 JSON Files Validation:")
    
    modpacks = validate_json_file(
        root / "api/modpacks.json",
        "modpacks.json"
    )
    
    launcher = validate_json_file(
        root / "api/launcher.json",
        "launcher.json"
    )
    
    news = validate_json_file(
        root / "api/news.json",
        "news.json"
    )
    
    featured = validate_json_file(
        root / "api/featured.json",
        "featured.json"
    )
    
    # Detailed validation
    print("\n🔍 Detailed Validation:")
    
    print("\n📦 Modpacks:")
    modpacks_ok = validate_modpacks(modpacks)
    
    print("\n🚀 Launcher:")
    launcher_ok = validate_launcher(launcher)
    
    print("\n📰 News:")
    news_ok = validate_news(news)
    
    print("\n⭐ Featured:")
    featured_ok = validate_featured(featured)
    
    # Summary
    print("\n" + "="*60)
    print("📊 SUMMARY")
    print("="*60)
    
    all_valid = (folders_ok and modpacks_ok and launcher_ok and 
                 news_ok and featured_ok)
    
    if all_valid:
        print("✅ All checks passed! Setup is ready.")
        print("\nNext steps:")
        print("1. Push to GitHub: git add . && git commit && git push")
        print("2. Create release: git tag -a v1.0.0 && git push origin v1.0.0")
        print("3. Upload .mrpack to GitHub Release")
        print("4. Wait 2 minutes for GitHub Pages deployment")
        print("5. Access API: https://kevanrafa.github.io/Integrity-Modpack/api/")
        return 0
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        print("\nRun manage-modpack.py and select option 1 to initialize.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
