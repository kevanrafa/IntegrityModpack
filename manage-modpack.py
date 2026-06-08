#!/usr/bin/env python3
"""
Integrity Modpack Manager
Manage modpacks, API files, and automate GitHub releases.
"""

import json
import os
from datetime import datetime
from pathlib import Path


class ModpackManager:
    def __init__(self):
        self.repo_root = Path(__file__).parent
        self.api_dir = self.repo_root / "api"
        self.icons_dir = self.repo_root / "icons"
        self.changelogs_dir = self.repo_root / "changelogs"
        self.modpacks_file = self.api_dir / "modpacks.json"
        self.featured_file = self.api_dir / "featured.json"
        self.username = "kevanrafa"
        self.repo_name = "Integrity-Modpack"
        
    def initialize_structure(self):
        """Create folder structure if it doesn't exist."""
        for directory in [self.api_dir, self.icons_dir, self.changelogs_dir]:
            directory.mkdir(parents=True, exist_ok=True)
            print(f"✓ Folder ready: {directory.relative_to(self.repo_root)}")
        
        # Create initial files if they don't exist
        if not self.modpacks_file.exists():
            self._create_modpacks_file()
        if not self.featured_file.exists():
            self._create_featured_file()
        print("✓ API files initialized")
    
    def _create_modpacks_file(self):
        """Create initial modpacks.json."""
        data = {
            "api_version": 1,
            "modpacks": []
        }
        with open(self.modpacks_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def _create_featured_file(self):
        """Create initial featured.json."""
        data = {"featured": []}
        with open(self.featured_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def add_modpack(self):
        """Interactively add a new modpack."""
        print("\n" + "="*50)
        print("ADD NEW MODPACK")
        print("="*50)
        
        modpack_id = self._input("Modpack ID (e.g., 'integrity'): ").strip()
        name = self._input("Modpack Name (e.g., 'Integrity'): ").strip()
        version = self._input("Version (e.g., '1.0.0'): ").strip()
        minecraft = self._input("Minecraft Version (e.g., '1.21.1'): ").strip()
        loader = self._input("Loader (fabric/forge/quilt): ").strip().lower()
        description = self._input("Description: ").strip()
        icon_file = self._input("Icon filename (e.g., 'integrity.png'): ").strip()
        
        # Build URLs
        icon_url = f"https://raw.githubusercontent.com/{self.username}/{self.repo_name}/main/icons/{icon_file}"
        download_url = f"https://github.com/{self.username}/{self.repo_name}/releases/download/v{version}/{modpack_id}.mrpack"
        changelog_url = f"https://raw.githubusercontent.com/{self.username}/{self.repo_name}/main/changelogs/{modpack_id}-{version}.md"
        
        # Create new modpack entry
        new_modpack = {
            "id": modpack_id,
            "name": name,
            "version": version,
            "minecraft": minecraft,
            "loader": loader,
            "description": description,
            "icon": icon_url,
            "download": download_url,
            "changelog": changelog_url
        }
        
        # Load existing modpacks
        with open(self.modpacks_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check if modpack already exists
        existing_ids = [mp["id"] for mp in data["modpacks"]]
        if modpack_id in existing_ids:
            # Update existing modpack
            for i, mp in enumerate(data["modpacks"]):
                if mp["id"] == modpack_id:
                    data["modpacks"][i] = new_modpack
                    print(f"✓ Updated modpack: {modpack_id}")
                    break
        else:
            # Add new modpack
            data["modpacks"].append(new_modpack)
            print(f"✓ Added new modpack: {modpack_id}")
        
        # Save modpacks.json
        with open(self.modpacks_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        # Create changelog file if it doesn't exist
        self._create_changelog(modpack_id, version)
        
        # Ask to add to featured
        if self._input("\nAdd to featured modpacks? (y/n): ").lower() == 'y':
            self._add_to_featured(modpack_id)
        
        print("\n✓ Modpack added successfully!")
    
    def _create_changelog(self, modpack_id, version):
        """Create empty changelog markdown file."""
        changelog_path = self.changelogs_dir / f"{modpack_id}-{version}.md"
        if not changelog_path.exists():
            content = f"""# {modpack_id} v{version} Changelog

## New Features
- 

## Changes
- 

## Fixes
- 

## Removed
- 

## Known Issues
- 
"""
            with open(changelog_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Created changelog: changelogs/{modpack_id}-{version}.md")
    
    def _add_to_featured(self, modpack_id):
        """Add modpack to featured list."""
        with open(self.featured_file, 'r', encoding='utf-8') as f:
            featured = json.load(f)
        
        if modpack_id not in featured["featured"]:
            featured["featured"].append(modpack_id)
            with open(self.featured_file, 'w', encoding='utf-8') as f:
                json.dump(featured, f, indent=2, ensure_ascii=False)
            print(f"✓ Added {modpack_id} to featured modpacks")
    
    def remove_from_featured(self, modpack_id):
        """Remove modpack from featured list."""
        with open(self.featured_file, 'r', encoding='utf-8') as f:
            featured = json.load(f)
        
        if modpack_id in featured["featured"]:
            featured["featured"].remove(modpack_id)
            with open(self.featured_file, 'w', encoding='utf-8') as f:
                json.dump(featured, f, indent=2, ensure_ascii=False)
            print(f"✓ Removed {modpack_id} from featured modpacks")
    
    def list_modpacks(self):
        """List all modpacks."""
        with open(self.modpacks_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not data["modpacks"]:
            print("No modpacks found.")
            return
        
        print("\n" + "="*50)
        print("MODPACKS")
        print("="*50)
        
        for mp in data["modpacks"]:
            print(f"\n📦 {mp['name']} (ID: {mp['id']})")
            print(f"   Version: {mp['version']}")
            print(f"   Minecraft: {mp['minecraft']}")
            print(f"   Loader: {mp['loader']}")
            print(f"   Description: {mp['description']}")
    
    def show_release_guide(self):
        """Show steps to create a release."""
        print("\n" + "="*50)
        print("RELEASE GUIDE")
        print("="*50)
        print("""
1. Update your modpack files and test

2. Run this script to add/update modpack info:
   python manage-modpack.py --add

3. Edit changelog in changelogs/ directory

4. Commit your changes:
   git add api/ changelogs/
   git commit -m "Release: Update modpack and changelog"

5. Create a GitHub release with tag v{version}:
   git tag -a v1.0.0 -m "Release v1.0.0"
   git push origin v1.0.0

6. Upload .mrpack file to GitHub Release:
   - Go to https://github.com/{username}/{repo}/releases
   - Edit the v1.0.0 release
   - Attach your {modpack_id}.mrpack file

7. GitHub Actions will automatically:
   - Deploy API files to GitHub Pages
   - Update GitHub Pages with new modpack info

Verify the API is accessible at:
   https://{username}.github.io/{repo}/api/modpacks.json
""".format(username=self.username, repo=self.repo_name, version="1.0.0", modpack_id="integrity"))
    
    def _input(self, prompt):
        """Get user input."""
        return input(prompt)
    
    def run_menu(self):
        """Display interactive menu."""
        while True:
            print("\n" + "="*50)
            print("INTEGRITY MODPACK MANAGER")
            print("="*50)
            print("""
1. Initialize/Check folder structure
2. Add/Update modpack
3. List modpacks
4. Add to featured
5. Remove from featured
6. Show release guide
7. Exit
""")
            choice = input("Select option (1-7): ").strip()
            
            if choice == "1":
                self.initialize_structure()
            elif choice == "2":
                self.add_modpack()
            elif choice == "3":
                self.list_modpacks()
            elif choice == "4":
                modpack_id = input("Enter modpack ID: ").strip()
                self._add_to_featured(modpack_id)
            elif choice == "5":
                modpack_id = input("Enter modpack ID: ").strip()
                self.remove_from_featured(modpack_id)
            elif choice == "6":
                self.show_release_guide()
            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid option")


def main():
    manager = ModpackManager()
    manager.run_menu()


if __name__ == "__main__":
    main()
