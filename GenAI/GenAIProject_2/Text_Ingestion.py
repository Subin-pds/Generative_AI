import markdown
import re
from bs4 import BeautifulSoup

file_path = r"C:\Users\subin\OneDrive\Desktop\GenAI\Data\Output\output.md"

def extract_text(file_path):
    with open(file_path, 'r', encoding='utf-8',errors='replace') as file:
        md_content = file.read()
    # Convert Markdown to HTML
    html = markdown.markdown(md_content)
    # Strip HTML and get plain text
    soup = BeautifulSoup(html, features='html.parser')
    plain_text = soup.get_text(separator="\n")
    return plain_text

def clean_text(text):
    # Remove special characters except alphanumerics, spaces, and basic punctuation
    cleaned = re.sub(r"[^a-zA-Z0-9.,;:'\"()\-\s]", '', text)

    # Remove brackets, commas, punctuation (keep only letters, numbers, and spaces)
    cleaned = re.sub(r"[\[\]{}(),.;:'\"!?<>@#$%^&*_+=~`|\\/-]", '', text)

    # Replace multiple spaces with a single space
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned