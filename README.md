# Temp71 Kodi Repository

A custom Kodi addon repository for hosting and distributing Kodi addons.

## Installation

To install this repository in Kodi:

1. Download the repository zip file: `repository.temp71-1.0.0.zip`
2. In Kodi, go to **Settings** > **Add-ons**
3. Select **Install from zip file**
4. Navigate to the location where you downloaded the zip file
5. Select `repository.temp71-1.0.0.zip`
6. Wait for the "Repository installed" notification

Once installed, you can browse and install addons from this repository through the Kodi addon browser.

## Adding Addons to This Repository

To add your own addons to this repository:

1. Create your addon following Kodi addon development guidelines
2. Package your addon as a zip file: `addon.id-version.zip`
3. Place the zip file in the root directory of this repository
4. Update `addons.xml` to include your addon's information
5. Regenerate the MD5 checksum:
   ```bash
   md5 -q addons.xml > addons.xml.md5
   ```
   (On Linux, use: `md5sum addons.xml | cut -d ' ' -f 1 > addons.xml.md5`)

## Repository Structure

```
repository.temp71/
├── addon.xml              # Repository addon definition
├── addons.xml             # List of all available addons
├── addons.xml.md5         # MD5 checksum of addons.xml
├── icon.png               # Repository icon (256x256)
├── fanart.jpg             # Repository fanart (1920x1080)
├── README.md              # This file
└── [addon-zips]           # Your addon zip files go here
```

## Configuration

Before using this repository, update the following in `addon.xml` and `addons.xml`:

1. Replace `yourusername` with your GitHub username (or update URLs to match your hosting)
2. Replace `Your Name` with your actual name or organization
3. Update the repository description and summary
4. Add icon.png and fanart.jpg images

## Hosting

This repository is designed to be hosted on GitHub. The URLs in the addon.xml file point to the raw GitHub URLs.

Alternative hosting options:
- GitLab
- Your own web server
- Any service that provides direct file access

Make sure to update all URLs in `addon.xml` and `addons.xml` to match your hosting location.

## Creating the Repository Zip

To create the installable repository zip file:

```bash
zip -r repository.temp71-1.0.0.zip addon.xml icon.png fanart.jpg
```

This creates a zip file that users can install directly in Kodi.

## License

Update this section with your chosen license.

## Support

Update this section with support information or links to issue trackers.
