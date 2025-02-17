import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from .mappings import SECTIONS, SUBJECTS
from .utils.file_utils import create_directories


def download_file(url, save_path):
    """Download a file and save it to the specified path."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"Downloaded and saved: {url} -> {save_path}")
        else:
            print(f"Failed to download {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


def extract_info_from_url(href):
    """Extract year, genre, and type from the URL."""
    genre = "enonce"
    if "corrige" in href or "_c" in href:
        genre = "correction"

    year = None
    for part in href.split("/"):
        if part.isdigit() and len(part) == 4:
            year = part
            break

    type_exam = "controle" if "controle" in href else "principale"

    return genre, type_exam, year


def process_exam_page(url, parent_folder):
    """Process an exam page and download files."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("a", href=True):
        href = link["href"]
        file_url = urljoin(url, href)
        parsed_url = urlparse(file_url)

        if parsed_url.path.endswith((".htm", ".html")):
            file_url = file_url.replace(".htm", ".pdf")
            parsed_url = urlparse(file_url)

        if parsed_url.path.endswith(".pdf"):
            genre, type_exam, year = extract_info_from_url(parsed_url.path)
            file_name = parsed_url.path.split("/")[-1]
            if year:
                file_name = f"{year}_{file_name}"
            dir_path = os.path.join(parent_folder, type_exam, genre)
            save_path = os.path.join(dir_path, file_name)

            create_directories(dir_path)
            download_file(file_url, save_path)


def main():
    """Main function to process the website and download exams."""
    main_page_url = "http://www.bacweb.tn/section.htm"
    response = requests.get(main_page_url)
    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all("a", href=True):
        href = link["href"]
        page_url = urljoin(main_page_url, href)
        parsed_url = urlparse(page_url)

        filename = os.path.basename(parsed_url.path)
        if len(filename) >= 3:
            section_code = filename[0]
            subject_code = filename[1:3]

            section = SECTIONS.get(section_code, "unknown_section")
            subject = SUBJECTS.get(subject_code, "unknown_subject")

            folder_path = os.path.join(section, subject)
            create_directories(folder_path)

            print(f"Processing page: {page_url}")
            process_exam_page(page_url, folder_path)


if __name__ == "__main__":
    main()
