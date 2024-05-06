from bs4 import BeautifulSoup
import os
import glob


def convert_tags(tag):
    """
    Used to convert italics to md
    """
    if tag.name == "em":
        return f"*{tag.text.strip()}*"
    return tag.text


def parse_into_markdown(directory_path):
    """
    A function that takes in a directory path then parses every page of the Daily Stoic into
    Markdown that will then be used to render a webpage
    """
    # Create MD Directory
    markdown_directory = "Markdown_Files"
    os.makedirs(markdown_directory, exist_ok=True)

    # Create the file pattern to iterate over
    file_pattern = os.path.join(directory_path, "part0*.xhtml")
    # Indexes for Jan 1st to Dec 31st taken from the book
    file_paths = sorted(glob.glob(file_pattern))[9:388]

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

                    if not date or not title:
                        continue

                # Initialize Markdown Content
                markdown_content = f"# {date}\n## {title}\n\n"

                # Finding the quotes
                quote_element = entry.find("p", class_="x03-Chapter-Epigraph")
                if quote_element:
                    quote = quote_element.text.strip()
                else:
                    continue

                quote_2 = entry.find_all("p", class_="x03-Chapter-Epigraph-Verse")

                # Adding subquotations to the original quote as per the book
                if len(quote_2) > 0:
                    for n in range(len(quote_2)):
                        quote += " " + quote_2[n].text.strip()

                # Quote Source
                quote_source = entry.find(
                    "p", class_="x03-Chapter-Epigraph-Source"
                ).text.strip()
                markdown_content += f"> {quote}\n\n*{quote_source}*\n\n"

                # Parsing the Body of the pages
                body_text = entry.find_all(
                    "p", class_=lambda value: value and "-Body-Text" in value
                )

                for p in body_text:
                    paragraph_text = ""
                    for child in p.children:
                        if child.name:
                            paragraph_text += convert_tags(child)
                        else:
                            paragraph_text += child.string if child.string else ""

                    markdown_content += f"{paragraph_text}\n\n"

                # Saving Content to Markdown
                filename = f"{date.replace(' ', '_').replace('.', '')}.md"
                filepath = os.path.join(markdown_directory, filename)
                with open(filepath, "w", encoding="utf-8") as md_file:
                    md_file.write(markdown_content)
    print("MD files created successfully")


directory_path = "extracted_contents/OEBPS/Text"
parse_into_markdown(directory_path)
