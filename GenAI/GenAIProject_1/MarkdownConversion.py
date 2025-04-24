
#Importing libraries
import os
from GenAIProject_1 import FileExtraction

def markdown_output(text):
    # Define the subfolder path
    output_dir = os.path.join("Data", "Output")
    os.makedirs(output_dir, exist_ok=True)  # Create the folder if it doesn't exist

    # Define the markdown file path
    file_path = os.path.join(output_dir, "output.md")

    # Write the text to the markdown file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

    # Return the absolute path
    return os.path.abspath(file_path)

# Function to process files and convert to Markdown
def convert_to_markdown(filepath):
    if filepath.endswith(".pdf"):
        text = FileExtraction.extract_pdf_to_markdown(filepath)
    elif filepath.endswith(".docx"):
        text = FileExtraction.extract_docx_to_markdown(filepath)
    elif filepath.endswith(".txt"):
        text = FileExtraction.extract_txt_to_markdown(filepath)
    elif filepath.endswith(".wav") or filepath.endswith(".mp3"):
        text = FileExtraction.extract_text_from_audio(filepath)
    else:
        raise ValueError("Unsupported file format")

    # Performing Normalization
    text = FileExtraction.normalization(text)

    # Saving as Markdown file
    markdown_output(text)
