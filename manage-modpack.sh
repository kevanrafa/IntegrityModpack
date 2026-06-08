#!/bin/bash
# Integrity Modpack Manager (Bash version)
# Simple bash script to manage modpacks and API files

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
API_DIR="$REPO_ROOT/api"
ICONS_DIR="$REPO_ROOT/icons"
CHANGELOGS_DIR="$REPO_ROOT/changelogs"
MODPACKS_FILE="$API_DIR/modpacks.json"
FEATURED_FILE="$API_DIR/featured.json"

USERNAME="kevanrafa"
REPO_NAME="Integrity-Modpack"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Initialize folder structure
init_structure() {
    echo -e "${BLUE}Initializing folder structure...${NC}"
    mkdir -p "$API_DIR" "$ICONS_DIR" "$CHANGELOGS_DIR"
    
    # Create modpacks.json if it doesn't exist
    if [ ! -f "$MODPACKS_FILE" ]; then
        cat > "$MODPACKS_FILE" << 'EOF'
{
  "api_version": 1,
  "modpacks": []
}
EOF
        echo -e "${GREEN}✓ Created modpacks.json${NC}"
    fi
    
    # Create featured.json if it doesn't exist
    if [ ! -f "$FEATURED_FILE" ]; then
        cat > "$FEATURED_FILE" << 'EOF'
{
  "featured": []
}
EOF
        echo -e "${GREEN}✓ Created featured.json${NC}"
    fi
    
    echo -e "${GREEN}✓ Folder structure initialized${NC}"
}

# Add new modpack
add_modpack() {
    echo -e "\n${BLUE}ADD NEW MODPACK${NC}"
    echo "================================"
    
    read -p "Modpack ID (e.g., 'integrity'): " MODPACK_ID
    read -p "Modpack Name (e.g., 'Integrity'): " NAME
    read -p "Version (e.g., '1.0.0'): " VERSION
    read -p "Minecraft Version (e.g., '1.21.1'): " MINECRAFT
    read -p "Loader (fabric/forge/quilt): " LOADER
    read -p "Description: " DESCRIPTION
    read -p "Icon filename (e.g., 'integrity.png'): " ICON_FILE
    
    # Build URLs
    ICON_URL="https://raw.githubusercontent.com/$USERNAME/$REPO_NAME/main/icons/$ICON_FILE"
    DOWNLOAD_URL="https://github.com/$USERNAME/$REPO_NAME/releases/download/v$VERSION/$MODPACK_ID.mrpack"
    CHANGELOG_URL="https://raw.githubusercontent.com/$USERNAME/$REPO_NAME/main/changelogs/$MODPACK_ID-$VERSION.md"
    
    # Create changelog file
    create_changelog "$MODPACK_ID" "$VERSION"
    
    # Use Python to update JSON (for proper JSON handling)
    python3 << PYTHON_SCRIPT
import json

modpack_data = {
    "id": "$MODPACK_ID",
    "name": "$NAME",
    "version": "$VERSION",
    "minecraft": "$MINECRAFT",
    "loader": "$LOADER",
    "description": "$DESCRIPTION",
    "icon": "$ICON_URL",
    "download": "$DOWNLOAD_URL",
    "changelog": "$CHANGELOG_URL"
}

with open("$MODPACKS_FILE", "r", encoding="utf-8") as f:
    data = json.load(f)

# Check if modpack exists
found = False
for i, mp in enumerate(data["modpacks"]):
    if mp["id"] == "$MODPACK_ID":
        data["modpacks"][i] = modpack_data
        found = True
        break

if not found:
    data["modpacks"].append(modpack_data)

with open("$MODPACKS_FILE", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
PYTHON_SCRIPT
    
    echo -e "${GREEN}✓ Added modpack: $MODPACK_ID${NC}"
    
    read -p "Add to featured modpacks? (y/n): " ADD_FEATURED
    if [ "$ADD_FEATURED" = "y" ]; then
        add_to_featured "$MODPACK_ID"
    fi
}

# Create changelog
create_changelog() {
    local MODPACK_ID=$1
    local VERSION=$2
    local CHANGELOG_PATH="$CHANGELOGS_DIR/$MODPACK_ID-$VERSION.md"
    
    if [ ! -f "$CHANGELOG_PATH" ]; then
        cat > "$CHANGELOG_PATH" << EOF
# $MODPACK_ID v$VERSION Changelog

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
EOF
        echo -e "${GREEN}✓ Created changelog: $MODPACK_ID-$VERSION.md${NC}"
    fi
}

# Add to featured
add_to_featured() {
    local MODPACK_ID=$1
    
    python3 << PYTHON_SCRIPT
import json

with open("$FEATURED_FILE", "r", encoding="utf-8") as f:
    featured = json.load(f)

if "$MODPACK_ID" not in featured["featured"]:
    featured["featured"].append("$MODPACK_ID")
    with open("$FEATURED_FILE", "w", encoding="utf-8") as f:
        json.dump(featured, f, indent=2, ensure_ascii=False)
    print("✓ Added $MODPACK_ID to featured modpacks")
PYTHON_SCRIPT
}

# List modpacks
list_modpacks() {
    echo -e "\n${BLUE}MODPACKS${NC}"
    echo "================================"
    python3 << PYTHON_SCRIPT
import json

with open("$MODPACKS_FILE", "r", encoding="utf-8") as f:
    data = json.load(f)

if not data["modpacks"]:
    print("No modpacks found.")
else:
    for mp in data["modpacks"]:
        print(f"\n📦 {mp['name']} (ID: {mp['id']})")
        print(f"   Version: {mp['version']}")
        print(f"   Minecraft: {mp['minecraft']}")
        print(f"   Loader: {mp['loader']}")
PYTHON_SCRIPT
}

# Show release guide
show_release_guide() {
    echo -e "\n${BLUE}RELEASE GUIDE${NC}"
    cat << EOF
================================

1. Update your modpack files and test

2. Run this script to add/update modpack info:
   ./manage-modpack.sh add

3. Edit changelog in changelogs/ directory

4. Commit your changes:
   git add api/ changelogs/
   git commit -m "Release: Update modpack and changelog"

5. Create a GitHub release with tag v{version}:
   git tag -a v1.0.0 -m "Release v1.0.0"
   git push origin v1.0.0

6. Upload .mrpack file to GitHub Release:
   - Go to https://github.com/$USERNAME/$REPO_NAME/releases
   - Edit the v1.0.0 release
   - Attach your modpack.mrpack file

7. GitHub Actions will automatically:
   - Deploy API files to GitHub Pages
   - Validate JSON structure
   - Update GitHub Pages

Verify the API is accessible at:
   https://$USERNAME.github.io/$REPO_NAME/api/modpacks.json

EOF
}

# Main menu
show_menu() {
    echo -e "\n${BLUE}INTEGRITY MODPACK MANAGER${NC}"
    echo "================================"
    echo "1. Initialize folder structure"
    echo "2. Add/Update modpack"
    echo "3. List modpacks"
    echo "4. Show release guide"
    echo "5. Exit"
    echo ""
    read -p "Select option (1-5): " CHOICE
    
    case $CHOICE in
        1) init_structure ;;
        2) add_modpack ;;
        3) list_modpacks ;;
        4) show_release_guide ;;
        5) echo "Goodbye!"; exit 0 ;;
        *) echo "Invalid option" ;;
    esac
    
    show_menu
}

# Run menu
show_menu
