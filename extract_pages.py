import zipfile
import os


def extract_epub_content(epub_path, output_folder):
    """
    A function used to turn the epub into a .zip file then read into a folder called extracted contents.
    This folder will contain the raw HTML that the epub file is in.
    """
    try:
        with zipfile.ZipFile(epub_path, "r") as zf:
            zf.extractall(output_folder)
            print("Files extracted successfully.")
    except zipfile.BadZipFile:
        print("Error: The file is not a zip file or it is corrupted.")
    except Exception as e:
        print("An error occurred:", e)


epub_path = "Ryan_Holiday_Stephen_Hanselman_The_Daily_Stoic.epub"
output_folder = "extracted_contents"
os.makedirs(output_folder, exist_ok=True)
extract_epub_content(epub_path, output_folder)
