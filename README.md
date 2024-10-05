# HEIC to JPG Converter

This Python script converts HEIC image files to JPG format. It's designed to process multiple files in a batch, making it easy to convert photos from iOS devices to a more universally compatible format.

## Features

- Converts HEIC files to JPG format
- Processes multiple files in a batch
- Maintains original file names (with .jpg extension)
- Preserves directory structure
- Provides error handling and conversion status messages

## Requirements

- Python 3.6+
- Pillow (PIL Fork)
- pillow-heif

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/heic-to-jpg-converter.git
   cd heic-to-jpg-converter
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install pillow pillow-heif
   ```

## Usage

1. Place your HEIC files in the `files2convert` folder.

2. Run the script:
   ```
   python heic_to_jpg.py
   ```

3. Find your converted JPG files in the `converted` folder.

## Project Structure

```
heic-to-jpg-converter/
│
├── heic_to_jpg.py
├── README.md
├── .venv/
├── files2convert/
│   ├── image1.heic
│   ├── image2.heic
│   └── ...
│
└── converted/
    ├── image1.jpg
    ├── image2.jpg
    └── ...
```

## How It Works

1. The script scans the `files2convert` folder for HEIC files.
2. Each HEIC file is opened, converted to RGB format, and saved as a JPG in the `converted` folder.
3. The original filename is preserved, with the extension changed to .jpg.
4. Progress messages are printed for each conversion.
5. Any errors during conversion are caught and reported, allowing the script to continue with the next file.

## Customization

- To adjust the quality of the JPG output, modify the `quality` parameter in the `save()` function call within the script.
- You can change the input and output folder names by modifying the `input_folder` and `output_folder` variables in the script.

## Acknowledgements

- [Pillow](https://python-pillow.org/)
- [pillow-heif](https://github.com/bigcat88/pillow_heif)
