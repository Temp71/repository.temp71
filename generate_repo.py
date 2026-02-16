#!/usr/bin/env python3
"""
Addon Repository Generator for Kodi

This script scans the repository directory for addon folders and generates:
- addons.xml: List of all available addons
- addons.xml.md5: MD5 checksum of addons.xml

Usage:
    python generate_repo.py
"""

import os
import hashlib
import xml.etree.ElementTree as ET
from pathlib import Path


def generate_addons_xml():
    """Generate addons.xml from all addon.xml files in subdirectories"""
    repo_dir = Path(__file__).parent
    addons_root = ET.Element("addons")
    
    # Find all addon.xml files (exclude the repository's own addon.xml)
    for addon_dir in repo_dir.iterdir():
        if addon_dir.is_dir() and addon_dir.name.startswith(("plugin.", "script.", "skin.", "repository.", "service.")):
            addon_xml_path = addon_dir / "addon.xml"
            if addon_xml_path.exists():
                try:
                    tree = ET.parse(addon_xml_path)
                    addon_element = tree.getroot()
                    addons_root.append(addon_element)
                    print(f"Added addon: {addon_element.get('id')}")
                except Exception as e:
                    print(f"Error parsing {addon_xml_path}: {e}")
    
    # Always include the repository itself
    repo_addon_xml = repo_dir / "addon.xml"
    if repo_addon_xml.exists():
        try:
            tree = ET.parse(repo_addon_xml)
            addon_element = tree.getroot()
            addons_root.append(addon_element)
            print(f"Added repository: {addon_element.get('id')}")
        except Exception as e:
            print(f"Error parsing repository addon.xml: {e}")
    
    # Write addons.xml
    tree = ET.ElementTree(addons_root)
    ET.indent(tree, space="    ")
    
    addons_xml_path = repo_dir / "addons.xml"
    tree.write(addons_xml_path, encoding="UTF-8", xml_declaration=True)
    print(f"\nGenerated: {addons_xml_path}")
    
    return addons_xml_path


def generate_md5(file_path):
    """Generate MD5 checksum for a file"""
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        md5_hash.update(f.read())
    
    md5_file = file_path.with_suffix(".xml.md5")
    with open(md5_file, "w") as f:
        f.write(md5_hash.hexdigest())
    
    print(f"Generated: {md5_file}")
    return md5_file


def main():
    """Main function"""
    print("=" * 50)
    print("Kodi Repository Generator")
    print("=" * 50)
    
    # Generate addons.xml
    addons_xml = generate_addons_xml()
    
    # Generate MD5 checksum
    generate_md5(addons_xml)
    
    print("\n" + "=" * 50)
    print("Repository files generated successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
