# Importing the libraries
import pdfplumber
import os
import mimetypes
import shutil
from tkinter import filedialog
import Config


#Automatically detect file type
def detect_file_type(filepath):
    if filepath.endswith(".pdf"):
        print('The file type is PDF File')
    elif filepath.endswith(".docx"):
        print('The file type is word File')
    elif filepath.endswith(".txt"):
        print('The file type is Text File')
    elif filepath.endswith(".wav"):
        print('The file type is Audio File')
    elif filepath.endswith(".mp3"):
        print('The file type is Audio File')
    else:
        raise ValueError("Unsupported file format")

# Error handling
def check_file (filepath):
  """
  Validate the file by checking if it exists and if it is of a supported file type
  """
  SUPPORTED_FILE_TYPES = ['.txt','.docx', '.pdf','.mp3','.wav']
  # Check if file exists
  if not os.path.exists(filepath):
    raise FileNotFoundError(f" The File {filepath} does not exist or is not a valid file")
  # Check if file extension is not supported
  file_extension = os.path.splitext(filepath)[1].lower()
  if file_extension not in SUPPORTED_FILE_TYPES:
    raise ValueError(f"The File type {file_extension} is not supported")
  return True

def validate_file(filepath):
  """
  To process the file based on its type
  """
  try:
    if check_file(filepath):
      print(f"Processsing file: {filepath}.")
      msg = "Processing file...."
      return msg
  except FileNotFoundError as file_not_found_error:
                     print(file_not_found_error)
  except ValueError as value_error:
                     print(value_error)
  except Exception as e:
                     print(f"Unexepted error occured while processing the file: {e}")

