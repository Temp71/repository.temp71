# Setup Instructions for Kodi Repository

## Quick Start Guide

### Step 1: Customize Repository Information

1. Open `addon.xml` and update:
   - `provider-name="Your Name"` - Replace with your name
   - URLs: Replace `yourusername` with your GitHub username
   - Summary and description

2. Open `addons.xml` and make the same updates

### Step 2: Add Images

Create the following image files:

- **icon.png**: 256x256 pixels - Repository icon
- **fanart.jpg**: 1920x1080 pixels - Background image

You can use image editing software like GIMP, Photoshop, or online tools.

### Step 3: Create Repository Zip for Installation

Run this command to create the installable zip file:

```bash
zip -r repository.temp71-1.0.0.zip addon.xml icon.png fanart.jpg
```

This zip file is what users will install in Kodi.

### Step 4: Add Your First Addon

1. Create your addon folder (e.g., `plugin.video.myvideos`)
2. Place the addon folder in this repository directory
3. Create a zip file of your addon:
   ```bash
   cd plugin.video.myvideos
   zip -r ../plugin.video.myvideos-1.0.0.zip *
   cd ..
   ```

4. Regenerate repository files:
   ```bash
   python3 generate_repo.py
   ```

### Step 5: Publish to GitHub

1. Initialize git repository:
   ```bash
   git init
   git add .
   git commit -m "Initial repository setup"
   ```

2. Create a new repository on GitHub named `repository.temp71`

3. Push to GitHub:
   ```bash
   git remote add origin https://github.com/yourusername/repository.temp71.git
   git branch -M master
   git push -u origin master
   ```

### Step 6: Share with Users

Share this installation URL with your users:
```
https://github.com/yourusername/repository.temp71/raw/master/repository.temp71-1.0.0.zip
```

Users can install it by selecting "Install from zip file" in Kodi and entering this URL.

## Maintaining the Repository

### Adding New Addons

1. Add the addon folder to the repository
2. Create a zip file: `addon.id-version.zip`
3. Run `python3 generate_repo.py`
4. Commit and push changes to GitHub

### Updating Existing Addons

1. Update the addon folder with new version
2. Update version number in the addon's `addon.xml`
3. Create new zip file with updated version number
4. Run `python3 generate_repo.py`
5. Commit and push changes to GitHub

## Testing

Before sharing with users:

1. Test the repository zip installation in a clean Kodi instance
2. Verify all addons appear in the repository
3. Test installing an addon from the repository
4. Check that updates work correctly

## Troubleshooting

### Repository not appearing in Kodi
- Check that addon.xml is valid XML
- Verify all URLs are accessible
- Check Kodi log for error messages

### Addons not showing up
- Run `python3 generate_repo.py` to regenerate addons.xml
- Verify addon.xml files are valid in each addon folder
- Check that zip files are named correctly: `addon.id-version.zip`

### Updates not working
- Increment version number in addon.xml
- Regenerate with generate_repo.py
- Clear Kodi cache if needed

## Additional Resources

- [Kodi Addon Development](https://kodi.wiki/view/Add-on_development)
- [Kodi Repository Structure](https://kodi.wiki/view/HOW-TO:Create_addon_repositories)
- [Kodi Forum](https://forum.kodi.tv/)
