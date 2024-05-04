from bs4 import BeautifulSoup
import os
import glob


def parse_into_markdown(directory_path):
    # Create MD Directory
    os.makedirs("Markdown_Files", exist_ok=True)

    # Create the file pattern to iterate over
    file_pattern = os.path.join(directory_path, "part0*.xhtml")
    file_paths = sorted(glob.glob(file_pattern))[9:10]

    # Iterate over the file_paths
    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            # Parse contents
            soup = BeautifulSoup(content, "html.parser")

            # Find all divs with element class 'P0'
            entries = soup.find_all("div", class_="PO")

            for entry in entries:
                # Finding the title and dates
                h3 = entry.find("h3")
                if h3:
                    # Extracting from h3 element array
                    date = h3.contents[1].strip()
                    title = h3.contents[3].text.strip()

                # Finding the quotes
                quote = entry.find("p", class_="x03-Chapter-Epigraph").text.strip()
                quote_2 = entry.find_all("p", class_="x03-Chapter-Epigraph-Verse")

                # Adding subquotations to the original quote as per the book
                if len(quote_2) > 0:
                    for n in range(len(quote_2)):
                        quote += " " + quote_2[n].text.strip()

                # Quote Source
                quote_source = entry.find(
                    "p", class_="x03-Chapter-Epigraph-Source"
                ).text.strip()


directory_path = "extracted_contents/OEBPS/Text"
parse_into_markdown(directory_path)
