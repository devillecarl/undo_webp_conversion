# Image Extension Recovery Tool for WordPress

This simple Python tool helps you recover images that have been converted to the `.webp` format in a WordPress uploads folder. It's particularly useful in cases where the original images have been deleted, and you need to recover the images in their original formats (e.g., `.jpg`, `.jpeg`, `.png`, or `.svg`).

## How to Use

1. Clone this repository or download the `image_extension_recovery.py` script.
2. Place the script in the root directory of your WordPress uploads folder.
3. Run the script using Python 3. The script will traverse the folder and its subfolders, renaming files as needed, removing any extra extensions, and keeping only the original extensions (`.jpg`, `.jpeg`, `.png`, or `.svg`).

## Example

If you have a file named `image.jpg.webp`, the script will rename it to `image.jpg`.

## Requirements

- Python 3.x

## Author

Antony Ngigge  
Email: antonyngigge@iworldafric.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

