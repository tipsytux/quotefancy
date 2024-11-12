# QuoteFancy Wallpaper Downloader

> Easily download 4K quote wallpapers from [QuoteFancy](https://quotefancy.com).

This tool allows you to download high-quality 4K wallpapers featuring quotes from a variety of categories available on QuoteFancy.

## Features

- Download 4K wallpapers in bulk from QuoteFancy.
- Choose specific quote categories to download.
- Customize the download directory.

## Installation

To use this tool, you'll need Python and a few packages installed. You can install them with:

```bash
pip install requests
pip install bs4
```

### Usage
1. Visit the QuoteFancy Website: Go to QuoteFancy and choose the categories of quotes you’d like to download as wallpapers.
2. Select Categories: In the script, add or remove categories (referred to as “roots”) according to your preferences.
3. Set the Download Directory: Specify the directory path where you want the wallpapers to be saved. An absolute path is recommended (e.g., /Users/YourName/QuoteWallpapers), but relative paths are also supported.
4. Run the Script: Execute the script, and it will download your chosen wallpapers to the specified directory.
5. Enjoy Your Wallpapers!

### Example
Here’s an example command to run the script after setting up your preferences:
```bash
python quotefancy.com
```

## Requirements
- Python 3.x
- requests library for handling HTTP requests
- BeautifulSoup (bs4) for parsing HTML

## Notes
- Ensure you have a stable internet connection to download wallpapers.
- If you encounter issues, check the website’s structure as it might have changed, requiring updates to the script.
